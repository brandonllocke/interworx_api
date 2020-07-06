from .controller import Controller


class MySQL(Controller):
    def __init__(self, server):
        super().__init__(server)
        self.controller = '/nodeworx/mysql'

    def auto_restart(self, **kwargs):
        return self._xmlrpc_query('autoRestart', **kwargs)

    def is_running(self):
        return self._xmlrpc_query('isRunning')
    
    def is_running_on_node(self, **kwargs):
        return self._xmlrpc_query('isRunningOnNode', **kwargs)

    def list_general_name(self):
        return self._xmlrpc_query('listGeneralName')

    def list_port_numbers(self):
        return self._xmlrpc_query('listPortNumbers')

    def list_port_numbers_array(self):
        return self._xmlrpc_query('listPortNumbersArray')

    def list_required_permissions(self):
        return self._xmlrpc_query('listRequiredPermissions')

    def list_service_info(self):
        return self._xmlrpc_query('listServiceInfo')

    def list_service_name(self):
        return self._xmlrpc_query('listServiceName')

    def list_service_page(self):
        return self._xmlrpc_query('listServicePage')

    def options(self, **kwargs):
        return self._xmlrpc_query('options', **kwargs)

    def query_auto_restart(self):
        return self._xmlrpc_query('queryAutoRestart')

    def query_options(self):
        return self._xmlrpc_query('queryOptions')

    def query_process(self):
        return self._xmlrpc_query('queryProcesses')

    def restart(self, **kwargs):
        return self._xmlrpc_query('restart', **kwargs)

    def restart_on_node(self, **kwargs):
        return self._xmlrpc_query('restartOnNode', **kwargs)

    def rootpass(self, *, password, confirm_password):
        return self._xmlrpc_query('rootpass', password=password, confirm_password=confirm_password)

    def rrd_graph(self, **kwargs):
        return self._xmlrpc_query('rrdGraph', **kwargs)

    def start(self, **kwargs):
        return self._xmlrpc_query('start', **kwargs)

    def start_on_boot(self, **kwargs):
        return self._xmlrpc_query('startOnBoot', **kwargs)

    def start_on_node(self, **kwargs):
        return self._xmlrpc_query('startOnNode', **kwargs)