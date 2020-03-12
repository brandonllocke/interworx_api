from .controller import Controller

class ApiKey(Controller):
    def __init__(self, server):
        super().__init__(server)
        self.controller = '/nodeworx/apikey'

    def list_api_key(self):
        return self._api_request('listApikey')

    def generate(self):
        return self._api_request('generate')

    def delete(self):
        return self._api_request('delete')
