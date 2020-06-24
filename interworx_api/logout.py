from .controller import Controller


class Logout(Controller):
    def __init__(self, server):
        super().__init__(server)
        self.controller = '/nodeworx/logout'

    def logout(self):
        return self._xmlrpc_query('logout')