from .controller import Controller

class FTP(Controller):
    def __init__(self, server):
        super().__init__(server)

class NodeWorxFTP(FTP):
    def __init__(self, server):
        super().__init__(server)
        self.controller = '/nodeworx/ftp'

    def auto_restart(self, **attributes):
        fields = {
            'required': {},
            'optional': {
                'ftp_autorestart': str,
                'cascade_to_nodes': int
            }
        }
        return self._api_request('autoRestart', fields=fields, **attributes)
    
    def is_running(self):
        return self._api_request('isRunning')
    
    def is_running_on_node(self, **attributes):
        fields = {
            'required': {},
            'optional': {
                'node_id': int
            }
        }
        return self._api_request('isRunningOnNode', fields=fields, **attributes)

    def kill_sessions(self, **attributes):
        fields = {
            'required': {'sessions': list},
            'optional': {}
        }
        return self._api_request('killSessions', fields=fields, **attributes)

    def list_ftp_sessions(self):
        return self._api_request('listFtpSessions')

    def list_general_name(self):
        return self._api_request('listGeneralName')

    def list_port_numbers(self):
        return self._api_request('listPortNumbers')
    
    def list_port_numbers_array(self):
        return self._api_request('listPortNumbersArray')

    def list_required_permissions(self):
        return self._api_request('listRequiredPermissions')

    def list_service_info(self):
        return self._api_request('listServiceInfo')
    
    def list_service_name(self):
        return self._api_request('listServicePage')

    def query_auto_restart(self):
        response = self._api_request('queryAutoRestart')
        if response['ftp_autorestart'] == 0:
            return True
        return False

    def query_edit_conf(self):
        response = self._api_request('queryEditConf')
        path = response['file']
        file_content = response['file_content']
        return path, file_content

    def query_server_options(self):
        return self._api_request('queryServerOptions')

    def query_sftp_options(self):
        return self._api_request('querySftpOptions')

    def restart(self, **attributes):
        fields = {
            'required': {},
            'optional': {
                'cascade_to_nodes': int
            }
        }
        return self._api_request('restart', fields=fields, **attributes)
    
    def restart_on_node(self, **attributes):
        fields = {
            'required': {},
            'optional': {
                'node_id': str
            }
        }
        return self._api_request('restartOnNode', fields=fields, **attributes)

    def rrd_graph(self, **attributes):
        fields = {
            'required': {},
            'optional': {
                'rrd': int
            }
        }
        return self._api_request('rrdGraph', fields=fields, **attributes)
    
    def server_options(self, **attributes):
        fields = {
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
        return self._api_request('serverOptions', fields=fields, **attributes)
    
    def sftp_options(self, **attributes):
        fields = {
            'required': {},
            'optional': {
                'port': int,
                'maxloginattempts': int,
                'sftpengine': int,
                'cascade_to_nodes': int
            }
        }
        return self._api_request('sftpOptions', fields=fields, **attributes)

    def start(self, **attributes):
        fields = {
            'required': {},
            'optional': {
                'cascade_to_nodes': int
            }
        }
        return self._api_request('start', fields=fields, **attributes)

    def start_on_boot(self, **attributes):
        fields = {
            'required': {},
            'optional': {
                'ftp_startonboot': int,
                'cascade_to_nodes': int
            }
        }
        return self._api_request('startOnBoot', fields=fields, **attributes)
    
    def start_on_node(self, **attributes):
        fields = {
            'required': {},
            'optional': {
                'node_id': str
            }
        }
        return self._api_request('startOnNode', fields=fields, **attributes)

    def stop(self, **attributes):
        fields = {
            'required': {},
            'optional': {
                'cascade_to_nodes': int
            }
        }
        return self._api_request('stop', fields=fields, **attributes)
    
    def stop_on_node(self, **attributes):
        fields = {
            'required': {},
            'optional': {
                'node_id': str
            }
        }
        return self._api_request('stopOnNode', fields=fields, **attributes)


class SiteWorxFTP(FTP):
    def __init__(self, server):
        super().__init__(server)
        self.controller = '/siteworx/ftp'

    def add(self, wd, **attributes):
        fields = {
            'required': {
                'user': str,
                'password': str,
                'confirm_password': str
            },
            'optional': {
                'homedir': str
            }
        }
        return self._api_request('add', fields=fields, wd=wd, **attributes)

    def delete(self, wd, **attributes):
        fields = {
            'required': {'user': list},
            'optional': {}
        }
        return self._api_request('delete', fields=fields, wd=wd, **attributes)
    
    def edit(self, wd, **attributes):
        fields = {
            'required': {
                'user': str,
                'homedir': str
            },
            'optional': {
                'password': str,
                'confirm_password': str,
            }
        }
        return self._api_request('edit', fields=fields, wd=wd, **attributes)

    def list_ftp_accounts(self, wd, **attributes):
        accounts = []
        response = self._api_request('listFtpAccounts', wd=wd, **attributes)
        for account in response:
            accounts.append(FTPAccount(account))
        return accounts

    def query_edit(self, wd, **attributes):
        fields = {
            'required': {'user': str},
            'optional': {}
        }
        return self._api_request('queryEdit', fields=fields, wd=wd, **attributes)

    def suspend(self, wd, **attributes):
        fields = {
            'required': {'user': list},
            'optional': {}
        }
        return self._api_request('suspend', fields=fields, wd=wd, **attributes)
    
    def unsuspend(self, wd, **attributes):
        fields = {
            'required': {'user': list},
            'optional': {}
        }
        return self._api_request('unsuspend', fields=fields, wd=wd, **attributes)


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