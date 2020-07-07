from .controller import Controller


class ApiKey(Controller):
    def __init__(self, server):
        super().__init__(server)
        self.controller = "/nodeworx/apikey"

    def list_api_key(self):
        """Displays the current API key on the server.

        :returns: API Key as a string
        :rtype: str
        """
        return self._xmlrpc_query("listApikey")

    # def generate(self):
    #    """Generates a new API key on the server.
    #
    #    TODO: Work on other authentication methods so generate API Key can be useful.
    #    """
    #    return self._xmlrpc_query('generate')

    def delete(self):
        """Deletes the currently authorized API key from server.

        :returns: generic success message
        :rtype: str
        """
        return self._xmlrpc_query("delete")
