class ApiKey:
    def __init__(self, server):
        self.server = server
        self.key = server.key
        self.controller = '/nodeworx/apikey'

    def _xmlrpc_query(self, action):
        return self.server.get(self.key, self.controller, action)

    def list_api_key(self):
        return self._xmlrpc_query('listApikey')

    def generate(self):
        return self._xmlrpc_query('generate')

    def delete(self):
        return self._xmlrpc_query('delete')
