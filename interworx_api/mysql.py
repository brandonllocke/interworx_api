from .controller import Controller


class MySQL(Controller):
    def __init__(self, server):
        super().__init__(server)
        self.controller = "/nodeworx/mysql"
        self.phpmyadmin = PHPMyAdmin(server)
        self.remote = Remote(server)

    def auto_restart(self, **kwargs):
        return self._xmlrpc_query("autoRestart", **kwargs)

    def is_running(self):
        return self._xmlrpc_query("isRunning")

    def is_running_on_node(self, **kwargs):
        return self._xmlrpc_query("isRunningOnNode", **kwargs)

    def list_general_name(self):
        return self._xmlrpc_query("listGeneralName")

    def list_port_numbers(self):
        return self._xmlrpc_query("listPortNumbers")

    def list_port_numbers_array(self):
        return self._xmlrpc_query("listPortNumbersArray")

    def list_required_permissions(self):
        return self._xmlrpc_query("listRequiredPermissions")

    def list_service_info(self):
        return self._xmlrpc_query("listServiceInfo")

    def list_service_name(self):
        return self._xmlrpc_query("listServiceName")

    def list_service_page(self):
        return self._xmlrpc_query("listServicePage")

    def options(self, **kwargs):
        return self._xmlrpc_query("options", **kwargs)

    def query_auto_restart(self):
        return self._xmlrpc_query("queryAutoRestart")

    def query_options(self):
        return self._xmlrpc_query("queryOptions")

    def query_process(self):
        return self._xmlrpc_query("queryProcesses")

    def restart(self, **kwargs):
        return self._xmlrpc_query("restart", **kwargs)

    def restart_on_node(self, **kwargs):
        return self._xmlrpc_query("restartOnNode", **kwargs)

    def rootpass(self, *, password, confirm_password):
        return self._xmlrpc_query(
            "rootpass", password=password, confirm_password=confirm_password
        )

    def rrd_graph(self, **kwargs):
        return self._xmlrpc_query("rrdGraph", **kwargs)

    def start(self, **kwargs):
        return self._xmlrpc_query("start", **kwargs)

    def start_on_boot(self, **kwargs):
        return self._xmlrpc_query("startOnBoot", **kwargs)

    def start_on_node(self, **kwargs):
        return self._xmlrpc_query("startOnNode", **kwargs)


class PHPMyAdmin(Controller):
    def __init__(self, server):
        super().__init__(server)
        self.controller = "/nodeworx/mysql/phpmyadmin"


class Remote(Controller):
    def __init__(self, server):
        super().__init__(server)
        self.controller = "/nodeworx/mysql/remote"

    def activate(self, *, server, root_username, root_password):
        return self._xmlrpc_query(
            "activate",
            server=server,
            root_username=root_username,
            root_password=root_password,
        )

    def add(self, *, host, root_username, root_password):
        return self._xmlrpc_query(
            "add", host=host, root_username=root_username, root_password=root_password
        )

    def default(self, *, server):
        return self._xmlrpc_query("default", server=server)

    def list_active_servers(self):
        return self._xmlrpc_query("listActiveServers")

    def list_deleteable_servers(self):
        return self._xmlrpc_query("listDeleteableServers")

    def list_inactive_servers(self):
        return self._xmlrpc_query("listInactiveServers")

    def list_servers(self):
        return self._xmlrpc_query("listServers")

    def nickname(self, *, server):
        return self._xmlrpc_query("nickname", server=server)

    def query_default(self, *, server):
        return self._xmlrpc_query("queryDefault", server=server)

    def query_processes(self, *, server):
        return self._xmlrpc_query("queryProcesses", server=server)

    def rootpass(self, *, server, password, confirm_password):
        return self._xmlrpc_query(
            "rootpass",
            server=server,
            password=password,
            confirm_password=confirm_password,
        )

