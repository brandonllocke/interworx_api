from .controller import Controller


class Index(Controller):
    def __init__(self, server):
        super().__init__(server)
        self.controller = "/nodeworx/index"

    def get_session(self):
        return self._xmlrpc_query('getSession')

    def get_websetup_status(self):
        return self._xmlrpc_query('getWebsetupStatus')