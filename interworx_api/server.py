import ssl
import sys
import xmlrpc.client

from .users import NodeWorxUsers
from .users import SiteWorxUsers
from .apikey import ApiKey
from .backups import NodeWorxBackups
from .backups import SiteWorxBackups
from .firewall import Firewall

class Server():
    def __init__(self, server_url, key):
        self.url = server_url
        self.key = key
        self.nodeworx = NodeWorx(self)
        self.siteworx = SiteWorx(self)
        context = ssl.SSLContext()
        self.server = xmlrpc.client.ServerProxy('https://%s:2443/xmlrpc' % self.url, context=context)

    def get(self, key, path, cmd, params=None):
        params = params or {}
        response = self.server.iworx.route(
            key, path, cmd, params)
        try:
            assert(response['status'] == 0)
            return response['payload']
        except AssertionError as e:
            pparams = '{' + ''.join(['{0}={1},'.format(k, v) for k,v in params.items()]) + '}'
            request_attributes = ('url=%s, path=%s, cmd=%s, params=%s' % (str(self.url), str(path), str(cmd), str(pparams)))
            print(request_attributes)
            sys.exit('Error: ' + str(response['status']) + ' - ' + response['payload'])


class NodeWorx():
    def __init__(self, server):
        self.url = server.url
        self.key = server.key
        self.users = NodeWorxUsers(server)
        self.apikey = ApiKey(server)
        self.backup = NodeWorxBackups(server)
        self.firewall = Firewall(server)


class SiteWorx():
    def __init__(self, server):
        self.url = server.url
        self.key = server.key
        self.users = SiteWorxUsers(server)
        self.backup = SiteWorxBackups(server)
