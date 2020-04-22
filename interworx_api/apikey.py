from .controller import Controller

class ApiKey(Controller):
    def __init__(self, server):
        super().__init__(server)
        self.controller = '/nodeworx/apikey'

    def list_api_key(self):
        """Displays the current API key on the server.

        Args: 
            None

        Returns: 
           str: a new API Key
        """
        return self._api_request('listApikey')

    def generate(self):
        """Generates a new API key on the server.

        Args: 
            None

        Returns: 
            Something.

        TODO: Work on other authentication methods so generate API Key can be useful.
        """
        return self._api_request('generate')

    def delete(self):
        """Deletes the currently authorized API key from server.

        Args: 
            None

        Returns: 
            str: generic success message
        """
        return self._api_request('delete')
