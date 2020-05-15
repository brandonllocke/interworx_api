class Controller:
    def __init__(self, server):
        self.server = server
        self.key = server.key
    
    def _modify_key(self, wd=None):
        if wd is not None:
            key = {'apikey': self.key, 'domain': wd}
            return key
        return self.key

    def _xmlrpc_query(self, action, wd=None, **kwargs):
        key = self._modify_key(wd)
        return self.server.get(key, self.controller, action, kwargs)