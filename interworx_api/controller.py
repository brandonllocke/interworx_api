class Controller:
    def __init__(self, server):
        self.server = server
        self.key = server.key

    def _modify_key(self, wd=None):
        if wd is not None:
            return {"apikey": self.key, "domain": wd}
        return self.key

    def _xmlrpc_query(self, action, wd=None, **kwargs):
        key = self._modify_key(wd)
        return self.server.get(key, self.controller, action, kwargs)

    def falsey(self, input):
        if input:
            return 1
        return 0

    def fail(self):
        return self._xmlrpc_query('fail')

    def reroute(self, *, controller='Index'):
        return self._xmlrpc_query('reroute', controller=controller)

    def win(self):
        return self._xmlrpc_query('win')