from .fields import Fields

class Controller:
    def __init__(self, server):
        self.server = server
        self.key = server.key
    
    def _modify_key(self, working_domain=None):
        if working_domain is not None:
            key = {'apikey': self.key, 'domain': working_domain}
            return key
        return self.key

    def _xmlrpc_query(self, action, working_domain=None, **attributes):
        key = self._modify_key(working_domain)
        return self.server.get(key, self.controller, action, attributes)
    
    def _parse_fields(self, possible_fields, **attributes):
        fields = Fields(possible_fields, **attributes)
        reqs_met = fields.check_required_fields()
        validated = fields.validate_fields()
        if reqs_met and validated:
            return True
        return False