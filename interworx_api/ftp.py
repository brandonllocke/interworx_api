from .controller import Controller

class NodeWorxFTP(Controller):
    def __init__(self, server):
        super().__init__(server)
        self.controller = '/nodeworx/ftp'

    def auto_restart(self, **kwargs):
        """ Sets the FTP server autostart status.

        Args:
            ftp_autorestart (int): (0/1) whether FTP restarts automatically
                if FTP goes down unexpectedly
            cascade_to_nodes (int): (0/1) whether this change should be made
                on all nodes

        Returns:
            str: generic success message
        """
        return self._xmlrpc_query('autoRestart', **kwargs)
    
    def is_running(self):
        """ Checks if the service is running or not.

        Args:
            None
        
        Returns:
            bool: whether service is running (True) or not (False)
        """
        return self._xmlrpc_query('isRunning')
    
    def is_running_on_node(self, **kwargs):
        """ Checks if service is running on a specific node.

        Args:
            node_id (int): the id number of the node

        Returns:
            bool: whether service is running (True) or not (False)
        """
        return self._xmlrpc_query('isRunningOnNode', **kwargs)

    def kill_sessions(self, *, sessions):
        """ Kill a running FTP session.

        Args:
            sessions (str/list): (required) a string or list of session pids

        Returns:
            str: generic success message
        """
        return self._xmlrpc_query('killSessions', sessions=sessions)

    def list_ftp_sessions(self):
        """ Lists currently active FTP sessions.

        Args:
            None

        Returns:
            list: list of dictionaries containing session information
        """
        return self._xmlrpc_query('listFtpSessions')

    def list_general_name(self):
        """ List the services' general name.

        Args:
            None
            
        Returns:
            str: the generic service name
        """
        return self._xmlrpc_query('listGeneralName')

    def list_port_numbers(self):
        """ List the ports used by the service.

        Args:
            None

        Returns:
            str: comma separated port numbers
        """
        return self._xmlrpc_query('listPortNumbers')
    
    def list_port_numbers_array(self):
        """ List the ports used by the service in a list

        Args:
            None

        Returns:
            list: list of integers containing port numbers
        """
        return self._xmlrpc_query('listPortNumbersArray')

    def list_required_permissions(self):
        """ List required permissions for FTP management.

        Args:
            None
        
        Returns:
            list: list of strings containing required permissions
        """
        return self._xmlrpc_query('listRequiredPermissions')

    def list_service_info(self):
        """ List service information for FTP.

        Args:
            None

        Returns:
            dict: dictionary of information about FTP server.
        """
        return self._xmlrpc_query('listServiceInfo')
    
    def list_service_name(self):
        """ List the service name for the FTP server.

        Args:
            None

        Returns:
            str: the service name
        """
        return self._xmlrpc_query('listServiceName')
    
    def list_service_page(self):
        """ List the service page for the FTP server.

        Args:
            None

        Returns:
            str: the service page
        """
        return self._xmlrpc_query('listServicePage')

    def query_auto_restart(self):
        """ Query the restart status of the FTP server.

        Args:
            None
        
        Returns:
            bool: whether service will autorestart (True) or not (False)
        """
        response = self._xmlrpc_query('queryAutoRestart')
        if response['ftp_autorestart'] == 0:
            return True
        return False

    def query_edit_conf(self):
        """ Query editable options for the FTP server.

        Args:
            None
        
        Returns:
            tuple: a tuple with the file path and file contents
        """
        response = self._xmlrpc_query('queryEditConf')
        path = response['file']
        file_content = response['file_content']
        return path, file_content

    def query_server_options(self):
        """ Query the server options for the FTP server.

        Args:
            None

        Returns:
            dict: dictionary of all server options
        """
        return self._xmlrpc_query('queryServerOptions')

    def query_sftp_options(self):
        """ Query the server's SFTP options.

        Args:
            None

        Returns:
            dict: a dictionary of all sftp options
        """
        return self._xmlrpc_query('querySftpOptions')

    def restart(self, **kwargs):
        """ Restart the FTP service.

        Args:
            cascade_to_nodes (int): (0/1) whether to repeat on all nodes

        Returns:
            str: generic success message
        """
        return self._xmlrpc_query('restart', **kwargs)
    
    def restart_on_node(self, **kwargs):
        """ Restart FTP service on a particular node.

        Args:
            node_id (str): the id of the node
        
        Returns:
            str: generic success message
        """
        return self._xmlrpc_query('restartOnNode', **kwargs)

    def rrd_graph(self, **kwargs):
        """ Enables/disables the RRD graph for FTP activity.

        Args:
            rrd (int): (0/1) whether to display the graph

        Returns:
            str: generic success message
        """
        return self._xmlrpc_query('rrdGraph', **kwargs)
    
    def server_options(self, **kwargs):
        """ Set server options for FTP server.

        Args:
            maxinstances (int):
            maxclients (int):
            maxclientsperuser (int):
            timeoutlogin (int):
            timeoutidle (int):
            timeoutnottransfer (int):
            timeoutstalled (int):
            timeoutsession (int):
            maxloginattempts (int):
            tlsrequired (int):
            showsymlinks (int):
            allowretrieverestart (int):
            allowstorerestart (int):
            cascade_to_nodes (int):

        Returns:
            str: generic success message
        """
        return self._xmlrpc_query('serverOptions', **kwargs)
    
    def sftp_options(self, **kwargs):
        fields = {
            'required': {},
            'optional': {
                'port': int,
                'maxloginattempts': int,
                'sftpengine': int,
                'cascade_to_nodes': int
            }
        }
        return self._api_request('sftpOptions', fields=fields, **kwargs)

    def start(self, **kwargs):
        fields = {
            'required': {},
            'optional': {
                'cascade_to_nodes': int
            }
        }
        return self._api_request('start', fields=fields, **kwargs)

    def start_on_boot(self, **kwargs):
        fields = {
            'required': {},
            'optional': {
                'ftp_startonboot': int,
                'cascade_to_nodes': int
            }
        }
        return self._api_request('startOnBoot', fields=fields, **kwargs)
    
    def start_on_node(self, **kwargs):
        fields = {
            'required': {},
            'optional': {
                'node_id': str
            }
        }
        return self._api_request('startOnNode', fields=fields, **kwargs)

    def stop(self, **kwargs):
        fields = {
            'required': {},
            'optional': {
                'cascade_to_nodes': int
            }
        }
        return self._api_request('stop', fields=fields, **kwargs)
    
    def stop_on_node(self, **kwargs):
        fields = {
            'required': {},
            'optional': {
                'node_id': str
            }
        }
        return self._api_request('stopOnNode', fields=fields, **kwargs)


class SiteWorxFTP(Controller):
    def __init__(self, server):
        super().__init__(server)
        self.controller = '/siteworx/ftp'

    def add(self, wd, **kwargs):
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
        return self._api_request('add', fields=fields, wd=wd, **kwargs)

    def delete(self, wd, **kwargs):
        fields = {
            'required': {'user': list},
            'optional': {}
        }
        return self._api_request('delete', fields=fields, wd=wd, **kwargs)
    
    def edit(self, wd, **kwargs):
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
        return self._api_request('edit', fields=fields, wd=wd, **kwargs)

    def list_ftp_accounts(self, wd, **kwargs):
        return self._api_request('listFtpAccounts', wd=wd, **kwargs)

    def query_edit(self, wd, **kwargs):
        fields = {
            'required': {'user': str},
            'optional': {}
        }
        return self._api_request('queryEdit', fields=fields, wd=wd, **kwargs)

    def suspend(self, wd, **kwargs):
        fields = {
            'required': {'user': list},
            'optional': {}
        }
        return self._api_request('suspend', fields=fields, wd=wd, **kwargs)
    
    def unsuspend(self, wd, **kwargs):
        fields = {
            'required': {'user': list},
            'optional': {}
        }
        return self._api_request('unsuspend', fields=fields, wd=wd, **kwargs)