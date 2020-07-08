from .controller import Controller


class NodeWorxFTP(Controller):
    def __init__(self, server):
        super().__init__(server)
        self.controller = "/nodeworx/ftp"

    def auto_restart(self, *, ftp_autorestart=False, cascade_to_nodes=True):
        """ Sets the FTP server autostart status.

        :param ftp_autorestart: whether FTP restarts automatically if FTP goes down unexpectedly (default: False)
        :type ftp_autorestart: bool
        :param cascade_to_nodes: replay change on nodes (default: True)
        :type cascade_to_nodes: bool
        :returns: generic success message
        :rtype: str
        """
        return self._xmlrpc_query(
            "autoRestart",
            ftp_autorestart=self.falsey(ftp_autorestart),
            cascade_to_nodes=self.falsey(cascade_to_nodes),
        )

    def is_running(self):
        """ Checks if the service is running or not.

        :returns: whether service is running (True) or not (False)
        :rtype: bool
        """
        return self._xmlrpc_query("isRunning")

    def is_running_on_node(self, **kwargs):
        """ Checks if service is running on a specific node.

        :param node_id: the id number of the node
        :type node_id: str
        :returns: whether service is running (True) or not (False)
        :rtype: bool
        """
        return self._xmlrpc_query("isRunningOnNode", **kwargs)

    def kill_sessions(self, *, sessions):
        """ Kill a running FTP session.

        :param sessions: a string or list of session pids (required)
        :type sessions: str/list
        :returns: generic success message
        :rtype: str
        """
        return self._xmlrpc_query("killSessions", sessions=sessions)

    def list_ftp_sessions(self):
        """ Lists currently active FTP sessions.

        :returns: list of dictionaries containing session information
        :rtype: list
        """
        return self._xmlrpc_query("listFtpSessions")

    def list_general_name(self):
        """ List the services' general name.

        :returns: the generic service name
        :rtype: str
        """
        return self._xmlrpc_query("listGeneralName")

    def list_port_numbers(self):
        """ List the ports used by the service.

        :returns: comma separated port numbers
        :rtype: str
        """
        return self._xmlrpc_query("listPortNumbers")

    def list_port_numbers_array(self):
        """ List the ports used by the service in a list

        :returns: list of integers containing port numbers
        :rtype: list
        """
        return self._xmlrpc_query("listPortNumbersArray")

    def list_required_permissions(self):
        """ List required permissions for FTP management.

        :returns: list of strings containing required permissions
        :rtype: list
        """
        return self._xmlrpc_query("listRequiredPermissions")

    def list_service_info(self):
        """ List service information for FTP.

        :returns: dictionary of information about FTP server
        :rtype: dict
        """
        return self._xmlrpc_query("listServiceInfo")

    def list_service_name(self):
        """ List the service name for the FTP server.

        :returns: the service name
        :rtype: str
        """
        return self._xmlrpc_query("listServiceName")

    def list_service_page(self):
        """ List the service page for the FTP server.

        :returns: the service page
        :rtype: str
        """
        return self._xmlrpc_query("listServicePage")

    def query_auto_restart(self):
        """ Query the restart status of the FTP server.

        :returns: whether service will autorestart (True) or not (False)
        :rtype: bool
        """
        response = self._xmlrpc_query("queryAutoRestart")
        return response["ftp_autorestart"] == 0

    def query_edit_conf(self):
        """ Query editable options for the FTP server.

        :returns: a tuple with the file path and file contents
        :rtype: tuple
        """
        response = self._xmlrpc_query("queryEditConf")
        return response["file"], response["file_content"]

    def query_server_options(self):
        """ Query the server options for the FTP server.

        :returns: dictionary of all server options
        :rtype: dict
        """
        return self._xmlrpc_query("queryServerOptions")

    def query_sftp_options(self):
        """ Query the server's SFTP options.

        :returns: a dictionary of all sftp options
        :rtype: dict
        """
        return self._xmlrpc_query("querySftpOptions")

    def restart(self, *, cascade_to_nodes=True):
        """ Restart the FTP service.

        :param cascade_to_nodes: repeat on all nodes (default: True)
        :type cascade_to_nodes: bool
        :returns: generic success message
        :rtype: str
        """
        return self._xmlrpc_query(
            "restart", cascade_to_nodes=self.falsey(cascade_to_nodes)
        )

    def restart_on_node(self, **kwargs):
        """ Restart FTP service on a particular node.

        :param node_id: the id of the node
        :type node_id: str
        :returns: generic success message
        :rtype: str
        """
        return self._xmlrpc_query("restartOnNode", **kwargs)

    def rrd_graph(self, *, rrd=False):
        """ Enables/disables the RRD graph for FTP activity.

        :param rrd: whether to display the graph
        :type rrd: bool
        :returns: generic success message
        :rtype: str
        """
        return self._xmlrpc_query("rrdGraph", rrd=self.falsey(rrd))

    def server_options(
        self,
        *,
        maxinstances=30,
        maxclients=25,
        maxclientsperuser=999999999,
        timeoutlogin=120,
        timeoutidle=600,
        timeoutnotransfer=900,
        timeoutstalled=3600,
        timeoutsessions=0,
        maxloginattempts=3,
        tlsrequired=False,
        showsymlinks=True,
        allowretrieverestart=True,
        allowstorerestart=True,
        cascade_to_nodes=True
    ):
        """ Set server options for FTP server.

        :param maxinstances: maximum child processes to spawn (default: 30)
        :type maxinstances: int
        :param maxclients: total number of FTP clients allowed to connect (default: 25)
        :type maxclients: int
        :param maxclientsperuser: total number of FTP clients allowed for one user id (default: 999999999)
        :type maxclientsperuser: int
        :param timeoutlogin: set login timeout (default: 120)
        :type timeoutlogin: int
        :param timeoutidle: set the idle timeout (default: 600)
        :type timeoutidle: int
        :param timeoutnotransfer: sets connection without transfer timeout (default: 900)
        :type timeoutnotransfer: int
        :param timeoutstalled: sets the timeout on stalled downloads (default: 3600)
        :type timeoutstalled: int
        :param timeoutsession: set a timeout for entire session (default: 0)
        :type timeoutsession: int
        :param maxloginattempts: set how many password attempts allowed
            before disconnection (default: 3)
        :type maxloginattempts: int
        :param tlsrequired: require TLS (FTPS)
        :type tlsrequired: bool
        :param showsymlinks: toggle the display of symlinks (default: True)
        :type showsymlinks: bool
        :param allowretrieverestart: allow clients to resume uploads (default: True)
        :type allowretrieverestart: bool
        :param allowstorerestart: allow clients to resume downloads (default: True)
        :type allowstorerestart: bool
        :param cascade_to_nodes: replay on all nodes (default: True)
        :type cascade_to_nodes: bool
        :returns: generic success message
        :rtype: str
        """
        return self._xmlrpc_query(
            "serverOptions",
            maxinstances=maxinstances,
            maxclients=maxclients,
            maxclientsperuser=maxclientsperuser,
            timeoutlogin=timeoutlogin,
            timeoutidle=timeoutidle,
            timeoutnotransfer=timeoutnotransfer,
            timeoutstalled=timeoutstalled,
            timeoutsessions=timeoutsessions,
            maxloginattempts=maxloginattempts,
            tlsrequired=self.falsey(tlsrequired),
            showsymlinks=self.falsey(showsymlinks),
            allowretrieverestart=self.falsey(allowretrieverestart),
            allowstorerestart=self.falsey(allowstorerestart),
            cascade_to_nodes=self.falsey(cascade_to_nodes),
        )

    def sftp_options(
        self, *, port=24, maxloginattempts=6, sftpengine=True, cascade_to_nodes=True
    ):
        """ Update SFTP server settings.

        :param port: the port used for SFTP service (default: 24)
        :type port: int
        :param maxloginattempts: sets how many password attempts are
            allowed before disconnection (default: 6)
        :type maxloginattempts: int
        :param sftpengine: current status of sftp engine (default: True)
        :type sftpengine: bool
        :param cascade_to_nodes: replay on all nodes (default: True)
        :type cascade_to_nodes: bool
        :returns: generic success message
        :rtype: str
        """
        return self._xmlrpc_query(
            "sftpOptions",
            port=port,
            maxloginattempts=maxloginattempts,
            sftpengine=self.falsey(sftpengine),
            cascade_to_nodes=self.falsey(cascade_to_nodes),
        )

    def start(self, *, cascade_to_nodes=True):
        """ Starts the FTP service.

        :param cascade_to_nodes: replay on all nodes (default: True)
        :type cascade_to_nodes: bool
        :returns: generic success message
        :rtype: str
        """
        return self._xmlrpc_query(
            "start", cascade_to_nodes=self.falsey(cascade_to_nodes)
        )

    def start_on_boot(self, *, ftp_startonboot=True, cascade_to_nodes=True):
        """ Set the FTP server start-on-boot status.

        :param ftp_startonboot: whether FTP is automatically started
            on server start up (default: True)
        :type ftp_startonboot: bool
        :param cascade_to_nodes: replay on all nodes (default: True)
        :type cascade_to_nodes: bool
        :returns: generic success message
        :rtype: str
        """
        return self._xmlrpc_query(
            "startOnBoot",
            ftp_startonboot=self.falsey(ftp_startonboot),
            cascade_to_nodes=self.falsey(cascade_to_nodes),
        )

    def start_on_node(self, **kwargs):
        """ Starts the service on a specific node.

        :param node_id: the id of the node to start on
        :type node_id: str
        :returns: generic success message
        :rtype: str
        """
        return self._xmlrpc_query("startOnNode", **kwargs)

    def stop(self, *, cascade_to_nodes=True):
        """ Stops the FTP service.

        :param cascade_to_nodes: replay on all nodes (default: True)
        :type cascade_to_nodes: bool
        :returns: generic success message
        :rtype: str
        """
        return self._xmlrpc_query("stop", cascade_to_nodes=self.falsey(cascade_to_nodes))

    def stop_on_node(self, **kwargs):
        """ Stops the service on a specific node.

        :param node_id: the id of the node to start on
        :type node_id: str
        :returns: generic success message
        :rtype: str
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
        return self._xmlrpc_query("suspend", wd=wd, user=user)

    def unsuspend(self, wd, user):
        """ Unsuspend an FTP account.

        Args:
            wd (str): (required) the working domain being edited
            user (str): (required) username of ftp user

        Returns:
            str: generic success message
        """
        return self._xmlrpc_query("unsuspend", wd=wd, user=user)

