from .fields import Fields

class Controller:
    def __init__(self, server):
        self.server = server
        self.key = server.key
    
    def _modify_key(self, wd=None):
        if wd is not None:
            key = {'apikey': self.key, 'domain': wd}
            return key
        return self.key

    def _xmlrpc_query(self, action, wd=None, **attributes):
        key = self._modify_key(wd)
        return self.server.get(key, self.controller, action, attributes)
    
    def _parse_fields(self, fields, **attributes):
        fields = Fields(fields, **attributes)
        reqs_met = fields.check_required_fields()
        validated = fields.validate_fields()
        if reqs_met and validated:
            return True
        return False
    
    def _api_request(self, action, fields=None, wd=None, **attributes):
        if fields is not None:
            if self._parse_fields(fields, **attributes):
                return self._xmlrpc_query(action, wd=wd, **attributes)
        else:
            return self._xmlrpc_query(action, wd=wd, **attributes)