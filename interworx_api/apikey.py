from .controller import Controller

class ApiKey(Controller):
    def __init__(self, server):
        super().__init__(server)
        self.controller = '/nodeworx/apikey'

    def list_api_key(self):
        return self._xmlrpc_query('listApikey')

    def generate(self):
        return self._xmlrpc_query('generate')

    def delete(self):
        return self._xmlrpc_query('delete')
