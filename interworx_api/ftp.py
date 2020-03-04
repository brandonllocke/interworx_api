class FTP:
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
    
class NodeWorxFTP(FTP):
    def __init__(self, server):
        super().__init__(server)
        self.controller = '/nodeworx/ftp'

    def auto_restart(self, **attributes):
        return self._xmlrpc_query('autoRestart', **attributes)
    
    def is_running(self):
        return self._xmlrpc_query('isRunning')

    def kill_sessions(self, **attributes):
        return self._xmlrpc_query('killSessions', **attributes)

    def list_ftp_sessions(self):
        return self._xmlrpc_query('listFtpSessions')

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
        return self._xmlrpc_query('listServicePage')

    def query_auto_restart(self):
        response = self._xmlrpc_query('queryAutoRestart')
        if response['ftp_autorestart'] == 0:
            return True
        return False

    def query_edit_conf(self):
        response = self._xmlrpc_query('queryEditConf')
        path = response['file']
        file_content = response['file_content']
        return path, file_content

    def query_server_options(self):
        return self._xmlrpc_query('queryServerOptions')

    def query_sftp_options(self):
        return self._xmlrpc_query('querySftpOptions')

    def restart(self, **attributes):
        return self._xmlrpc_query('restart', **attributes)

    def rrd_graph(self, **attributes):
        return self._xmlrpc_query('rrdGraph', **attributes)
    
    def server_options(self, **attributes):
        return self._xmlrpc_query('serverOptions', **attributes)
    
    def sftp_options(self, **attributes):
        return self._xmlrpc_query('sftpOptions', **attributes)

    def start(self, **attributes):
        return self._xmlrpc_query('start', **attributes)

    def start_on_boot(self, **attributes):
        return self._xmlrpc_query('startOnBoot', **attributes)

    def stop(self, **attributes):
        return self._xmlrpc_query('stop', **attributes)