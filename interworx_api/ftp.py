from .controller import Controller


class NodeWorxFTP(Controller):
    def __init__(self, server):
        super().__init__(server)
        self.controller = "/nodeworx/ftp"

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
        return self._xmlrpc_query("autoRestart", **kwargs)

    def is_running(self):
        """ Checks if the service is running or not.

        Args:
            None
        
        Returns:
            bool: whether service is running (True) or not (False)
        """
        return self._xmlrpc_query("isRunning")

    def is_running_on_node(self, **kwargs):
        """ Checks if service is running on a specific node.

        Args:
            node_id (int): the id number of the node

        Returns:
            bool: whether service is running (True) or not (False)
        """
        return self._xmlrpc_query("isRunningOnNode", **kwargs)

    def kill_sessions(self, *, sessions):
        """ Kill a running FTP session.

        Args:
            sessions (str/list): (required) a string or list of session pids

        Returns:
            str: generic success message
        """
        return self._xmlrpc_query("killSessions", sessions=sessions)

    def list_ftp_sessions(self):
        """ Lists currently active FTP sessions.

        Args:
            None

        Returns:
            list: list of dictionaries containing session information
        """
        return self._xmlrpc_query("listFtpSessions")

    def list_general_name(self):
        """ List the services' general name.

        Args:
            None
            
        Returns:
            str: the generic service name
        """
        return self._xmlrpc_query("listGeneralName")

    def list_port_numbers(self):
        """ List the ports used by the service.

        Args:
            None

        Returns:
            str: comma separated port numbers
        """
        return self._xmlrpc_query("listPortNumbers")

    def list_port_numbers_array(self):
        """ List the ports used by the service in a list

        Args:
            None

        Returns:
            list: list of integers containing port numbers
        """
        return self._xmlrpc_query("listPortNumbersArray")

    def list_required_permissions(self):
        """ List required permissions for FTP management.

        Args:
            None
        
        Returns:
            list: list of strings containing required permissions
        """
        return self._xmlrpc_query("listRequiredPermissions")

    def list_service_info(self):
        """ List service information for FTP.

        Args:
            None

        Returns:
            dict: dictionary of information about FTP server.
        """
        return self._xmlrpc_query("listServiceInfo")

    def list_service_name(self):
        """ List the service name for the FTP server.

        Args:
            None

        Returns:
            str: the service name
        """
        return self._xmlrpc_query("listServiceName")

    def list_service_page(self):
        """ List the service page for the FTP server.

        Args:
            None

        Returns:
            str: the service page
        """
        return self._xmlrpc_query("listServicePage")

    def query_auto_restart(self):
        """ Query the restart status of the FTP server.

        Args:
            None
        
        Returns:
            bool: whether service will autorestart (True) or not (False)
        """
        response = self._xmlrpc_query("queryAutoRestart")
        if response["ftp_autorestart"] == 0:
            return True
        return False

    def query_edit_conf(self):
        """ Query editable options for the FTP server.

        Args:
            None
        
        Returns:
            tuple: a tuple with the file path and file contents
        """
        response = self._xmlrpc_query("queryEditConf")
        path = response["file"]
        file_content = response["file_content"]
        return path, file_content

    def query_server_options(self):
        """ Query the server options for the FTP server.

        Args:
            None

        Returns:
            dict: dictionary of all server options
        """
        return self._xmlrpc_query("queryServerOptions")

    def query_sftp_options(self):
        """ Query the server's SFTP options.

        Args:
            None

        Returns:
            dict: a dictionary of all sftp options
        """
        return self._xmlrpc_query("querySftpOptions")

    def restart(self, **kwargs):
        """ Restart the FTP service.

        Args:
            cascade_to_nodes (int): (0/1) whether to repeat on all nodes

        Returns:
            str: generic success message
        """
        return self._xmlrpc_query("restart", **kwargs)

    def restart_on_node(self, **kwargs):
        """ Restart FTP service on a particular node.

        Args:
            node_id (str): the id of the node
        
        Returns:
            str: generic success message
        """
        return self._xmlrpc_query("restartOnNode", **kwargs)

    def rrd_graph(self, **kwargs):
        """ Enables/disables the RRD graph for FTP activity.

        Args:
            rrd (int): (0/1) whether to display the graph

        Returns:
            str: generic success message
        """
        return self._xmlrpc_query("rrdGraph", **kwargs)

    def server_options(self, **kwargs):
        """ Set server options for FTP server.

        Args:
            maxinstances (int): maximum child processes to spawn
            maxclients (int): total number of FTP clients allowed to connect
            maxclientsperuser (int): total number of FTP clients allowed for
                one user id
            timeoutlogin (int): set login timeout
            timeoutidle (int): set the idle timeout
            timeoutnottransfer (int): sets connection without transfer
                timeout
            timeoutstalled (int): sets the timeout on stalled downloads
            timeoutsession (int): set a timeout for entire session
            maxloginattempts (int): set how many password attempts allowed
                before disconnection
            tlsrequired (int): require TLS (FTPS)
            showsymlinks (int): toggle the display of symlinks
            allowretrieverestart (int): allow clients to resume uploads
            allowstorerestart (int): allow clients to resume downloads
            cascade_to_nodes (int): replay on all nodes?

        Returns:
            str: generic success message
        """
        return self._xmlrpc_query("serverOptions", **kwargs)

    def sftp_options(self, **kwargs):
        """ Update SFTP server settings.

        Args:
            port (int): the port used for SFTP service
            maxloginattempts (int): sets how many password attempts are
                allowed before disconnection
            sftpengine (int): (0/1) current status of sftp engine
            cascade_to_nodes (int): replay on all nodes?
        
        Returns:
            str: generic success message
        """
        return self._xmlrpc_query("sftpOptions", **kwargs)

    def start(self, **kwargs):
        """ Starts the FTP service.

        Args:
            cascade_to_nodes (int): replay on all nodes?

        Returns:
            str: generic success message
        """
        return self._xmlrpc_query("start", **kwargs)

    def start_on_boot(self, **kwargs):
        """ Set the FTP server start-on-boot status.

        Args:
            ftp_startonboot (int): (0/1) whether FTP is automatically started
                on server start up
            cascade_to_nodes (int): replay on all nodes?

        Returns:
            str: generic success message
        """
        return self._xmlrpc_query("startOnBoot", **kwargs)

    def start_on_node(self, **kwargs):
        """ Starts the service on a specific node.

        Args:
            node_id (str): the id of the node to start on

        Retuns:
            str: generic success message
        """
        return self._xmlrpc_query("startOnNode", **kwargs)

    def stop(self, **kwargs):
        """ Stops the FTP service.

        Args:
            cascade_to_nodes (int): replay on all nodes?

        Returns:
            str: generic success message
        """
        return self._xmlrpc_query("stop", **kwargs)

    def stop_on_node(self, **kwargs):
        """ Stops the service on a specific node.

        Args:
            node_id (str): the id of the node to start on
        
        Returns:
            str: generic success message
        """
        return self._xmlrpc_query("stopOnNode", **kwargs)


class SiteWorxFTP(Controller):
    def __init__(self, server):
        super().__init__(server)
        self.controller = "/siteworx/ftp"

    def add(self, *, wd, user, password, confirm_password, **kwargs):
        """ Add an FTP account.

        Args:
            wd (str): (required) the working domain being edited
            user (str): (required) username of ftp user
            password (str): (required) password for account
            confirm_password (str): (required) password for account
            homedir (str): highest dirpath user can access
        
        Returns:
            str: generic success message
        """
        return self._xmlrpc_query(
            "add",
            wd=wd,
            user=user,
            password=password,
            confirm_password=confirm_password,
            **kwargs
        )

    def delete(self, *, wd, user):
        """ Delete an FTP account.

        Args:
            wd (str): (required) the working domain being edited
            user (str): (required) username of ftp user

        Returns:
            str: generic success message
        """
        return self._xmlrpc_query("delete", wd=wd, user=user)

    def edit(self, *, wd, user, homedir, **kwargs):
        """ Edit an FTP account.

        Args:
            wd (str): (required) the working domain being edited
            user (str): (required) username of ftp user
            homedir (str): (required) highest dirpath user can access
            password (str): password for account
            confirm_password (str): password for account
        
        Returns:
            str: generic success message
        """
        return self._xmlrpc_query("edit", wd=wd, user=user, homedir=homedir, **kwargs)

    def list_ftp_accounts(self, *, wd):
        """ List FTP Accounts.

        Args:
            wd (str): (required) the working domain being edited
        
        Returns:
            list: list of dictionaries containing FTP account info
        """
        return self._xmlrpc_query("listFtpAccounts", wd=wd)

    def query_edit(self, *, wd, user):
        """ Display the information available to the account "edit".

        Args:
            wd (str): (required) the working domain being edited
            user (str): (required) username of ftp user

        Returns:
            dict: dictionary containing info that can be edited
        """
        return self._xmlrpc_query("queryEdit", wd=wd, user=user)

    def suspend(self, *, wd, user):
        """ Suspend an FTP account.

        Args:
            wd (str): (required) the working domain being edited
            user (str): (required) username of ftp user

        Returns:
            str: generic success message
        """
        return self._xmlrpc_query("suspend", wd=wd, user=user, **kwargs)

    def unsuspend(self, wd, user):
        """ Unsuspend an FTP account.

        Args:
            wd (str): (required) the working domain being edited
            user (str): (required) username of ftp user

        Returns:
            str: generic success message
        """
        return self._xmlrpc_query("unsuspend", wd=wd, user=user)

