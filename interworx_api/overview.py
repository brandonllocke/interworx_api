from .controller import Controller

class Overview(Controller):
    def __init__(self, server):
        super().__init__(server)
        self.controller = "/nodeworx/overview"

    def edit_profile(self, *, theme='calliope', language='en-us', menu_style='big', **kwargs):
        return self._xmlrpc_query('editProfile', theme=theme, language=language, menu_style=menu_style, **kwargs)

    def list_hostname(self):
        return self._xmlrpc_query('listHostname')

    def list_is_clusterable(self):
        return self._xmlrpc_query('listIsClusterable')

    def list_license_key(self):
        return self._xmlrpc_query('listLicenseKey')

    def list_load_average(self):
        return self._xmlrpc_query('listLoadAverage')

    def list_service_status(self):
        return self._xmlrpc_query('listServiceStatus')

    def list_version(self):
        return self._xmlrpc_query('listVersion')

    def list_vps_status(self):
        return self._xmlrpc_query('listVPSStatus')