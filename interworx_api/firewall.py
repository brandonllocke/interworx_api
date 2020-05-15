from .controller import Controller

class Firewall(Controller):
    def __init__(self, server):
        super().__init__(server)
        self.controller = '/nodeworx/firewall'

    def add_port(self, *, port, tcp_flow_in, tcp_flow_out, udp_flow_in,
                 upd_flow_out, **kwargs):
        """ Add a port to the firewall configuration.

        Args:
            port (str): (required) the port or ports you with to add to the
                firewall. You can enter port ranges as well.
            tcp_flow_in (str): (required) (open/closed)
            tcp_flow_out (str): (required) (open/closed)
            udp_flow_in (str): (required) (open/closed)
            udp_flow_out (str): (required) (open/closed)
            cascade_to_nodes (int): (0/1) replay on nodes?
        
        Returns:
            str: generic success message
        """
        return self._xmlrpc_query('addPort', port=port, 
                                  tcp_flow_in=tcp_flow_in, 
                                  tcp_flow_out=tcp_flow_out,
                                  udp_flow_in=udp_flow_in,
                                  udp_flow_out=udp_flow_out,
                                  **kwargs)

    def allow_deny_ips(self, **kwargs):
        """ Set firewall ip address allow and deny lists.

        Args:
            trusted_ips (str/list): the ip address for license.interworx.info
                (207.32.181.150) must be present for proper function of the
                InterWorx license authentication system.
            blocked_ips (str/list): list of ips to block
        
        Returns:
            str: generic success message
        """
        return self._xmlrpc_query('allowDenyIps', **kwargs)

    def delete(self, *, ports):
        """ Delete firewall port configuration.

        Args:
            ports (str/list): (required) port numbers to delete configuration
                for
        
        Returns:
            str: generic success message
        """
        return self._xmlrpc_query('delete', ports=ports)

    def ipv6_settings(self, **kwargs):
        """ Controls how IPv6 Settings are handled when restarting the
        firewall.

        Args:
            ip6tables_status (str): (off/manual/managed)
            icmp6_control (str): (default/managed)
            cascade_to_nodes (int): (1) replay on nodes?
        
        Returns:
            str: generic success message
        """
        return self._xmlrpc_query('ipv6Settings', **kwargs)

    def is_running(self):
        """ Checks if the service is running or not.

        Args:
            None

        Returns:
            bool: whether the service is running or not
        """
        return self._xmlrpc_query('isRunning')
    
    def is_running_on_node(self, **kwargs):
        """ Checks if the service is running on a sepcific node (clustering
        only).

        Args:
            node_id (str): the node id

        Returns:
            str: generic success message
        """
        return self._xmlrpc_query('isRunningOnNode', **kwargs)

    def list_general_name(self):
        """ Lists the "normal" name - ie "web server" instead of httpd.

        Args:
            None
        
        Returns:
            str: the general name
        """
        return self._xmlrpc_query('listGeneralName')
    
    def list_port_numbers(self):
        """ Lists a string of the port numbers that this services uses,
        comma-separated.

        Args:
            None
        
        Returns:
            str: the comma-separated list of ports used by the service
        """
        return self._xmlrpc_query('listPortNumbers')
    
    def list_port_numbers_array(self):
        """ Lists an array of the port numbers that this services uses,
        comma-separated.

        Args:
            None
        
        Returns:
            list: a list of port numbers and arrays as strings
        """
        return self._xmlrpc_query('listPortNumbersArray')

    def list_required_permissions(self):
        """ List permissions required to control the service.

        Args:
            None

        Returns:
            list: list of required permissions as strings
        """
        return self._xmlrpc_query('listRequiredPermissions')

    def list_service_info(self):
        """ Lists the service name, ports, page, and status.

        Args:
            None
        
        Returns:
            dict: information about the service
        """
        return self._xmlrpc_query('listServiceInfo')
    
    def list_service_name(self):
        """ Lists the service name - ie "httpd" instead of "web server'.

        Args:
            None
        
        Returns:
            str: the service name
        """
        return self._xmlrpc_query('listServiceName')

    def list_service_page(self):
        """ List the page that controls the service.

        Args:
            None
        
        Returns:
            str: the service page
        """
        return self._xmlrpc_query('listServicePage')

    def query_allow_deny_ips(self):
        """ Displays the information available to the action "allowDenyIps".

        Args:
            None
        
        Returns:
            tuple: two lists (trusted_ips and blocked_ips)
        """
        trusted_ips = []
        blocked_ips = []
        response = self._xmlrpc_query('queryAllowDenyIps')
        for ip in response['trusted_ips']:
            trusted_ips.append(ip)
        for ip in response['blocked_ips']:
            blocked_ips.append(ip)
        return trusted_ips, blocked_ips

    def query_ipv6_settings(self):
        """ Display the information available to the action "ipv6Settings".

        Args:
            None
        
        Returns:
            dict: information available to action ipv6settings
        """
        return self._xmlrpc_query('queryIpv6Settings')

    def restart(self, **kwargs):
        fields = {
            'optional': {'cascade_to_nodes': int}
        }
        return self._api_request('restart', fields=fields, **kwargs)

    def restart_on_node(self, **kwargs):
        fields = {
            'optional': {'node_id': str}
        }
        return self._api_request('restartOnNode', fields=fields, **kwargs)
    
    def start(self, **kwargs):
        fields = {
            'optional': {'cascade_to_nodes': int}
        }
        return self._api_request('start', fields=fields, **kwargs)

    def start_on_boot(self, **kwargs):
        fields = {
            'optional': {
                'startonboot': int,
                'cascade_to_nodes': int
            }
        }
        return self._api_request('startOnBoot', fields=fields, **kwargs)

    def start_on_node(self, **kwargs):
        fields = {
            'optional': {
                'node_id': int
            }
        }
        return self._api_request('startOnNode', fields=fields, **kwargs)

    def stop(self, **kwargs):
        fields = {
            'optional': {
                'cascade_to_nodes': int
            }
        }
        return self._api_request('stop', fields=fields, **kwargs)

    def stop_on_node(self, **kwargs):
        fields = {
            'optional': {
                'node_id': int
            }
        }
        return self._api_request('stopOnNode', fields=fields, **kwargs)
    
    def update(self, **kwargs):
        fields = {
            'required': {
                'ports': list
            },
            'optional': {
                'tcp_flow_in': str,
                'tcp_flow_out': str,
                'udp_flow_in': str,
                'udp_flow_out': str
            }
        }
        return self._api_request('update', fields=fields, **kwargs)
    
    def update_config(self, **kwargs):
        fields = {
            'optional': {
                'debug_mode': int,
                'defult_tos': int,
                'tcp_drop_policy': str,
                'udp_drop_policy': str,
                'block_multicast': int,
                'block_private_network': int,
                'set_egress_filter': int,
                'max_sessions': int,
                'sysctl_tcp': int,
                'if': str,
                'tifs': str,
                'cascade_to_nodes': int
            }
        }
        return self._api_request('updateConfig', fields=fields, **kwargs)