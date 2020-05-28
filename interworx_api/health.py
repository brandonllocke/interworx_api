from .controller import Controller


class Health(Controller):
    def __init__(self, server):
        super().__init__(server)
        self.controller = "/nodeworx/health"

    def edit(self, *, code, **kwargs):
        return self._xmlrpc_query('edit', code=code, **kwargs)

    def edit_recipients(self, *, code, **kwargs):
        return self._xmlrpc_query('editRecipients', code=code, **kwargs)

    def query_code_history(self, *, code):
        return self._xmlrpc_query('queryCodeHistory', code=code)

    def query_code_by_email(self, *, email):
        return self._xmlrpc_query('queryCodesByEmail', email=email)

    def query_edit(self):
        return self._xmlrpc_query('queryEdit')

    def query_edit_recipients(self, *, code):
        return self._xmlrpc_query('queryEditRecipients')

    def query_health_status(self):
        return self._xmlrpc_query('queryHealthStatus')
    
    def remove_target_from_code(self, *, code, target):
        return self._xmlrpc_query('removeTargetFromCode', 
                                  code=code,
                                  target=target)