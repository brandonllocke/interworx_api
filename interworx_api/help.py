from .controller import Controller


class Help(Controller):
    def __init__(self, server):
        super().__init__(server)
        self.controller = "/nodeworx/help"
    
    def query_ssh(self):
        return self._xmlrpc_query('querySsh')
    
    def ssh(self, **kwargs):
        return self._xmlrpc_query('ssh', **kwargs)