from .controller import Controller


class Logs(Controller):
    def __init__(self, server):
        super().__init__(server)
        self.controller = '/nodeworx/logs'

    def view(self, *, group):
        return self._xmlrpc_query('view', group=group)