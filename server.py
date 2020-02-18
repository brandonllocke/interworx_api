import ssl
import xmlrpc.client

from .users import Users

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
        return self.server.iworx.route(
            key, path, cmd, params)


class NodeWorx():
    def __init__(self, server, ctrl_prefix='/nodeworx'):
        self.url = server.url
        self.key = server.key
        self.ctrl_prefix = ctrl_prefix
        self.users = Users(server, self.ctrl_prefix)


class SiteWorx():
    def __init__(self, server, ctrl_prefix='/siteworx'):
        self.url = server.url
        self.key = server.key
        self.ctrl_prefix = ctrl_prefix
        self.users = Users(server, self.ctrl_prefix)
