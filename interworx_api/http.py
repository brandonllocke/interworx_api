from .controller import Controller

class Http(Controller):
    def __init__(self, server):
        super().__init__(server)
        self.controller = '/nodeworx/http'

    def _edit_module(self, action=None, **attributes):
        fields = {
            'required': {},
            'optional': {
                'name': list,
            }
        }
        return self._api_request(action, fields=fields, **attributes)

    def apache_update(self, **attributes):
        fields = {
            'required': {},
            'optional': {
                'http_port': int,
                'https_port': int,
                'serverlimit': int,
                'maxclients': int,
                'startservers': int,
                'minspareservers': int,
                'maxspareservers': int,
                'maxrequestsperchild': int,
                'timeout': int,
                'keepalive': int,
                'maxkeepaliverequests': int,
                'keepalivetimeout': int,
                'adddefaultcharset': str,
                'force_graceful': int,
                'cascade_to_nodes': int
            }
        }
        return self._api_request('apacheUpdate', fields=fields, **attributes)
    
    def auto_restart(self, **attributes):
        fields = {
            'required': {},
            'optional': {
                'apache_autorestart': int,
                'cascade_to_nodes': int,
            }
        }
        return self._api_request('autoRestart', fields=fields, **attributes)

    def disable(self, **attributes):
        return self._edit_modules(action='disable', **attributes)

    def enabled(self, **attributes):
        return self._edit_modules(action='enable', **attributes)

    def enable_multiple_php(self):
        return self._api_request('enableMultiplePhp')

    def is_running(self):
        return self._api_request('isRunning')

    def is_running_on_node(self, **attributes):
        fields = {
            'required': {},
            'optional': {'node_id': str}
        }
        return self._api_request('isRunningOnNode', fields=fields, **attributes)

    def list_available_php_versions(self):
        return self._api_request('listAvailablePhpVersions')

    def list_enabled_php_versions(self):
        return self._api_request('listEnabledPhpVersions')

    def list_general_name(self):
        return self._api_request('listGeneralName')

    def list_modules(self):
        return self._api_request('listModules')

    def list_php_install_mode(self):
        return self._api_request('listPhpInstallMode')

    def list_port_numbers(self):
        return self._api_request('listPortNumbers')
    
    def list_port_numbers_array(self):
        return self._api_request('listPortNumbersArray')

    def list_required_permissions(self):
        return self._api_request('listRequiredPermissions')

    def list_service_info(self):
        return self._api_request('listServiceInfo')

    def list_service_name(self):
        return self._api_request('listServiceName')

    def list_service_page(self):
        return self._api_request('listServicePage')

    def multiple_php_options(self, **attributes):
        fields = {
            'optional': {
                'enabled_php_versions': list,
                'default_php_version': str
            }
        }
        return self._api_request('multiplePhpOptions', fields=fields, **attributes)

    def query_apache_update(self):
        return self._api_request('queryApacheUpdate')

    def query_auto_restart(self):
        return bool(self._api_request('queryAutoRestart')['apache_autorestart'])

    def query_edit_conf(self):
        return self._api_request('queryEditConf')

    def query_multiple_php_options(self):
        return self._api_request('queryMultiplePhpOptions')

    def query_update_php_mode(self):
        return self._api_request('queryUpdatePhpMode')

    def refresh_available_php_versions(self):
        self._api_request('refreshAvailablePhpVersions')

    def remove(self, **attributes):
        return self._edit_modules(action='remove', **attributes)

    def reset_php_fpm_files(self):
        return self._api_request('resetPhpFpmFiles')

    def restart(self, **attributes):
        fields = {
            'optional': {
                'cond': int,
                'cascade_to_nodes': int
            }
        }
        return self._api_request('restart', fields=fields, **attributes)

    def restart_on_node(self, **attributes):
        fields = {'optional': {'node_id': str}}
        return self._api_request('restartOnNode', fields=fields, **attributes)

    def restart_php_fpm(self, **attributes):
        fields = {'optional': {'cascade_to_nodes': int}}
        return self._api_request('restartPhpFpm', fields=fields, **attributes)

    def start(self, **attributes):
        fields = {'optional': {'cascade_to_nodes': int}}
        return self._api_request('start', fields=fields, **attributes)

    def start_on_boot(self, **attributes):
        fields = {'optional': {
            'startonboot': int,
            'cascade_to_nodes': int
            }
        }
        return self._api_request('startOnBoot', fields=fields, **attributes)

    def start_on_node(self, **attributes):
        fields = {'optional': {'node_id': str}}
        return self._api_request('startOnNode', fields=fields, **attributes)

    def stop(self, **attributes):
        fields = {'optional': {'cascade_to_nodes': int}}
        return self._api_request('stop', fields=fields, **attributes)

    def stop_on_node(self, **attributes):
        fields = {'optional': {'node_id': str}}
        return self._api_request('stopOnNode', fields=fields, **attributes)

    def sync_all_config_files(self):
        return self._api_request('syncAllConfigFiles')

    def sync_config_files(self, **attributes):
        fields = {'required': {'domain': str}}
        return self._api_request('syncConfigFiles', fields=fields, **attributes)

    def sync_redirects(self):
        return self._api_request('syncRedirects')

    def update_php_mode(self, **attributes):
        fields = {'optional': {'php_mode': str}}
        return self._api_request('updatePhpMode', fields=fields, **attributes)

    def update_rrd(self, **attributes):
        fields = {'optional': {'updateRrd': int}}
        return self._api_request('updateRrd', fields=fields, **attributes)