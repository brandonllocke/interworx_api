class SWAccounts:
    def __init__(self, server):
        self.server = server
        self.key = server.key
        self.controller = '/nodeworx/siteworx'

    def _xmlrpc_query(self, action, **attributes):
        return self.server.get(self.key, self.controller, action, attributes)

    def add(self, **attributes):
        return self._xmlrpc_query('add', **attributes)

    def add_ip(self, **attributes):
        return self._xmlrpc_query('addIp', **attributes)

    def delete(self, **attributes):
        return self._xmlrpc_query('delete', **attributes)
    
    def delete_config(self, **attributes):
        return self._xmlrpc_query('deleteConfig', **attributes)

    def edit(self, **attributes):
        return self._xmlrpc_query('edit', **attributes)

    def list_accounts(self, **attributes):
        return self._xmlrpc_query('listAccounts', **attributes)