from .controller import Controller

class Http(Controller):
    def __init__(self, server):
        super().__init__(server)
        self.controller = '/nodeworx/http'

    def apache_update(self, *, **kwargs):
        """ Update common apache web server settings.

        Args:
            http_port (int): the port for http use
            https_port (int): the port for https use
            serverlimit (int): sets the maximum configured value for
                MaxClients for the lifetime of the web server process.
            maxclients (int): sets the limit on the number of simultaneous
                requests that will be served.
            startservers (int): sets the number of child server processes
                created on startup. As the number of processes is dynamically
                controlled depending on the load, there is usually little
                reason to adjust this parameter.
            minspareserver (int): Minimum number of idle threads to handle
                request spikes.
            maxspareservers (int): monitors the number of idle threads on a
                per-child basis. If there are too many idle threads in that
                child, the server will begin to kill threads within that
                child.
            maxrequestperchild (int): sets the limit on the number of
                requests that an individual child server process will handle.
            timeout (int): the length of time before the web server kills the
                thread handling your connection.
            keepalive (int): Turn Keepalive on or off.
            maxkeepaliverequests (int): The Keep-Alive extension to HTTP/1.0
                and the persistent connection feature of HTTP/1.1 provide
                long-lived HTTP sessions which allow multiple requests to be
                sent over the same TCP connection.
            keepalivetimeout (int): he number of seconds the web server will
                wait for a subsequent request before closing the connection.
                Once a request has been received, the timeout value specified
                by the timeout directive applies.
            adddefaultcharset (str): Default value for the media type charset
                parameter (the name of a character encoding) to be added to a
                response if and only if the response’s content-type is either
                text/plain or text/html.
            force_graceful (int): force restart of apache upon change?
            cascade_to_nodes (int): Selecting this option causes the action
                to be replayed on all nodes of the cluster automatically, as
                if you had logged in to each node manually
        
        Returns:
            str: generic success message
        """
        return self._xmlrpc_query('apacheUpdate', **kwargs)
    
    def auto_restart(self, *, **kwargs):
        return self._xmlrpc_query('autoRestart', **kwargs)

    def enable_multiple_php(self):
        return self._xmlrpc_query('enableMultiplePhp')

    def is_running(self):
        return self._xmlrpc_query('isRunning')

    def is_running_on_node(self, *, **kwargs):
        return self._xmlrpc_query('isRunningOnNode', **kwargs)

    def list_available_php_versions(self):
        return self._xmlrpc_query('listAvailablePhpVersions')

    def list_enabled_php_versions(self):
        return self._xmlrpc_query('listEnabledPhpVersions')

    def list_general_name(self):
        return self._xmlrpc_query('listGeneralName')

    def list_modules(self):
        return self._xmlrpc_query('listModules')

    def list_php_install_mode(self):
        return self._xmlrpc_query('listPhpInstallMode')

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

    def multiple_php_options(self, *, **kwargs):
        return self._xmlrpc_query('multiplePhpOptions', **kwargs)

    def query_apache_update(self):
        return self._xmlrpc_query('queryApacheUpdate')

    def query_auto_restart(self):
        return bool(self._xmlrpc_query('queryAutoRestart')['apache_autorestart'])

    def query_edit_conf(self):
        return self._xmlrpc_query('queryEditConf')

    def query_multiple_php_options(self):
        return self._xmlrpc_query('queryMultiplePhpOptions')

    def query_update_php_mode(self):
        return self._xmlrpc_query('queryUpdatePhpMode')

    def refresh_available_php_versions(self):
        self._xmlrpc_query('refreshAvailablePhpVersions')

    def reset_php_fpm_files(self):
        return self._xmlrpc_query('resetPhpFpmFiles')

    def restart(self, *, **kwargs):
        return self._xmlrpc_query('restart', **kwargs)

    def restart_on_node(self, *, **kwargs):
        return self._xmlrpc_query('restartOnNode', **kwargs)

    def restart_php_fpm(self, *, **kwargs):
        return self._xmlrpc_query('restartPhpFpm', **kwargs)

    def start(self, *, **kwargs):
        return self._xmlrpc_query('start', **kwargs)

    def start_on_boot(self, *, **kwargs):
        return self._xmlrpc_query('startOnBoot', **kwargs)

    def start_on_node(self, *, **kwargs):
        return self._xmlrpc_query('startOnNode', **kwargs)

    def stop(self, *, **kwargs):
        return self._xmlrpc_query('stop', **kwargs)

    def stop_on_node(self, *, **kwargs):
        return self._xmlrpc_query('stopOnNode', **kwargs)

    def sync_all_config_files(self):
        return self._xmlrpc_query('syncAllConfigFiles')

    def sync_config_files(self, *, domain, **kwargs):
        return self._xmlrpc_query('syncConfigFiles', domain=domain, **kwargs)

    def sync_redirects(self):
        return self._xmlrpc_query('syncRedirects')

    def update_php_mode(self, *, **kwargs):
        return self._xmlrpc_query('updatePhpMode', **kwargs)

    def update_rrd(self, *, **kwargs):
        return self._xmlrpc_query('updateRrd', **kwargs)