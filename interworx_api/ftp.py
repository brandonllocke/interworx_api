from .controller import Controller

class FTP(Controller):
    def __init__(self, server):
        super().__init__(server)

class NodeWorxFTP(FTP):
    def __init__(self, server):
        super().__init__(server)
        self.controller = '/nodeworx/ftp'

    def auto_restart(self, **attributes):
        possible_fields = {
            'required': {},
            'optional': {
                'ftp_autorestart': str,
                'cascade_to_nodes': int
            }
        }
        if self._parse_fields(possible_fields, **attributes):
             return self._xmlrpc_query('autoRestart', **attributes)
    
    def is_running(self):
        return self._xmlrpc_query('isRunning')
    
    def is_running_on_node(self, **attributes):
        possible_fields = {
            'required': {},
            'optional': {
                'node_id': int
            }
        }
        if self._parse_fields(possible_fields, **attributes):
             return self._xmlrpc_query('isRunningOnNode', **attributes)

    def kill_sessions(self, **attributes):
        possible_fields = {
            'required': {},
            'optional': {
                'sessions': list
            }
        }
        if self._parse_fields(possible_fields, **attributes):
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
        possible_fields = {
            'required': {},
            'optional': {
                'cascade_to_nodes': int
            }
        }
        if self._parse_fields(possible_fields, **attributes):
            return self._xmlrpc_query('restart', **attributes)
    
    def restart_on_node(self, **attributes):
        possible_fields = {
            'required': {},
            'optional': {
                'node_id': str
            }
        }
        if self._parse_fields(possible_fields, **attributes):
            return self._xmlrpc_query('restartOnNode', **attributes)

    def rrd_graph(self, **attributes):
        possible_fields = {
            'required': {},
            'optional': {
                'rrd': int
            }
        }
        if self._parse_fields(possible_fields, **attributes):
            return self._xmlrpc_query('rrdGraph', **attributes)
    
    def server_options(self, **attributes):
        possible_fields = {
            'required': {},
            'optional': {
                'maxinstances': int,
                'maxclients': int,
                'maxclientsperuser': int,
                'timeoutlogin': int,
                'timeoutidle': int,
                'timeoutnottransfer': int,
                'timeoutstalled': int,
                'timeoutsession': int,
                'maxloginattempts': int,
                'tlsrequired': int,
                'showsymlinks': int,
                'allowretrieverestart': int,
                'allowstorerestart': int,
                'cascade_to_nodes': int
            }
        }
        if self._parse_fields(possible_fields, **attributes):
            return self._xmlrpc_query('serverOptions', **attributes)
    
    def sftp_options(self, **attributes):
        possible_fields = {
            'required': {},
            'optional': {
                'port': int,
                'maxloginattempts': int,
                'sftpengine': int,
                'cascade_to_nodes': int
            }
        }
        if self._parse_fields(possible_fields, **attributes):
            return self._xmlrpc_query('sftpOptions', **attributes)

    def start(self, **attributes):
        possible_fields = {
            'required': {},
            'optional': {
                'cascade_to_nodes': int
            }
        }
        if self._parse_fields(possible_fields, **attributes):
            return self._xmlrpc_query('start', **attributes)

    def start_on_boot(self, **attributes):
        possible_fields = {
            'required': {},
            'optional': {
                'ftp_startonboot': int,
                'cascade_to_nodes': int
            }
        }
        if self._parse_fields(possible_fields, **attributes):
            return self._xmlrpc_query('startOnBoot', **attributes)
    
    def start_on_node(self, **attributes):
        possible_fields = {
            'required': {},
            'optional': {
                'node_id': str
            }
        }
        if self._parse_fields(possible_fields, **attributes):
            return self._xmlrpc_query('startOnNode', **attributes)

    def stop(self, **attributes):
        possible_fields = {
            'required': {},
            'optional': {
                'cascade_to_nodes': int
            }
        }
        if self._parse_fields(possible_fields, **attributes):
            return self._xmlrpc_query('stop', **attributes)
    
    def stop_on_node(self, **attributes):
        possible_fields = {
            'required': {},
            'optional': {
                'node_id': str
            }
        }
        if self._parse_fields(possible_fields, **attributes):
            return self._xmlrpc_query('stopOnNode', **attributes)


class SiteWorxFTP(FTP):
    def __init__(self, server):
        super().__init__(server)
        self.controller = '/siteworx/ftp'

    def add(self, working_domain, **attributes):
        possible_fields = {
            'required': {
                'user': str,
                'password': str,
                'confirm_password': str
            },
            'optional': {
                'homedir': str
            }
        }
        if self._parse_fields(possible_fields, **attributes):
            return self._xmlrpc_query('add', working_domain, **attributes)

    def delete(self, working_domain, **attributes):
        possible_fields = {
            'required': {'user': list},
            'optional': {}
        }
        if self._parse_fields(possible_fields, **attributes):
            return self._xmlrpc_query('delete', working_domain, **attributes)
    
    def edit(self, working_domain, **attributes):
        possible_fields = {
            'required': {'user': str},
            'optional': {
                'password': str,
                'confirm_password': str,
                'homedir': str
            }
        }
        if self._parse_fields(possible_fields, **attributes):
            return self._xmlrpc_query('edit', working_domain, **attributes)

    def list_ftp_accounts(self, working_domain, **attributes):
        accounts = []
        response = self._xmlrpc_query('listFtpAccounts', working_domain, **attributes)
        for account in response:
            accounts.append(FTPAccount(account))
        return accounts

    def query_edit(self, working_domain, **attributes):
        possible_fields = {
            'required': {'user': str},
            'optional': {}
        }
        if self._parse_fields(possible_fields, **attributes):
            return self._xmlrpc_query('queryEdit', working_domain, **attributes)

    def suspend(self, working_domain, **attributes):
        possible_fields = {
            'required': {'user': list},
            'optional': {}
        }
        if self._parse_fields(possible_fields, **attributes):
            return self._xmlrpc_query('suspend', working_domain, **attributes)
    
    def unsuspend(self, working_domain, **attributes):
        possible_fields = {
            'required': {'user': list},
            'optional': {}
        }
        if self._parse_fields(possible_fields, **attributes):
            return self._xmlrpc_query('unsuspend', working_domain, **attributes)


class FTPAccount:
    def __init__(self, info):
        self.username = info.get('username')
        self.homedir = info.get('homedir')
        self.login_count = info.get('login_count')
        self.fulluser = info.get('fulluser')
        self.status = info.get('status')

    def __str__(self):
        return self.username

    def __repr__(self):
        return self.username