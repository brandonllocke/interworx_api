import ssl
import sys
import traceback
import xmlrpc.client

from .users import NodeWorxUsers
from .users import SiteWorxUsers
from .apikey import ApiKey
from .backups import NodeWorxBackups
from .backups import SiteWorxBackups
from .firewall import Firewall
from .ftp import NodeWorxFTP
from .ftp import SiteWorxFTP
from .siteworx import SWAccounts
from .cron import NodeWorxCron
from .cron import SiteWorxCron

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
            if response['status'] == 0:
                return response['payload']
            else:
                raise ValidationError(response['status'], response['payload'])
        except ValidationError as e:
            sys.exit(e)


class NodeWorx():
    def __init__(self, server):
        self.url = server.url
        self.key = server.key
        self.users = NodeWorxUsers(server)
        self.apikey = ApiKey(server)
        self.backup = NodeWorxBackups(server)
        self.firewall = Firewall(server)
        self.ftp = NodeWorxFTP(server)
        self.siteworx = SWAccounts(server)
        self.cron = NodeWorxCron(server)


class SiteWorx():
    def __init__(self, server):
        self.url = server.url
        self.key = server.key
        self.users = SiteWorxUsers(server)
        self.backup = SiteWorxBackups(server)
        self.ftp = SiteWorxFTP(server)
        self.cron = SiteWorxCron(server)


class ValidationError(Exception):
    def __init__(self, status, payload):
        super().__init__(payload)
        self.status = status
        self.payload = payload

    def __str__(self):
        return f'''Server responded with an exit code of: {self.status}.
The server's response was: {self.payload}.'''            