class SWAccounts:
    def __init__(self, server):
        self.server = server
        self.key = server.key
        self.controller = '/nodeworx/siteworx'

    def _modify_key(self, working_domain=None):
        if working_domain is not None:
            key = {'apikey': self.key, 'domain': working_domain}
            return key
        return self.key

    def _xmlrpc_query(self, action, working_domain=None, **attributes):
        key = self._modify_key(working_domain)
        return self.server.get(key, self.controller, action, attributes)

    def add(self, working_domain=None, **attributes):
        return self._xmlrpc_query('add', working_domain, **attributes)