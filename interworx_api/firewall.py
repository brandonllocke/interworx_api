from .controller import Controller


class Firewall(Controller):
    def __init__(self, server):
        super().__init__(server)
        self.controller = "/nodeworx/firewall"

    def _check_open_closed(self, options):
        return all(option in ["open", "closed"] for option in options)

    def _ensure_licensing_ip_allowed(self, **kwargs):
        trusted_ips = kwargs.get("trusted_ips")
        if trusted_ips and (type(trusted_ips) == str):
            kwargs["trusted_ips"] = [trusted_ips, "207.32.181.150"]
        if trusted_ips and (type(trusted_ips) == list):
            kwargs["trusted_ips"].append("207.32.181.150")
        return kwargs

    def add_port(
        self,
        *,
        port,
        tcp_flow_in,
        tcp_flow_out,
        udp_flow_in,
        udp_flow_out,
        cascade_to_nodes=True
    ):
        """ Add a port to the firewall configuration.

        :param port: the port or ports you wish to add to the firewall. You
            can enter port ranges, as well (required)
        :type port: str
        :param tcp_flow_in: [open/closed] (required)
        :type tcp_flow_in: str
        :param tcp_flow_out: [open/closed] (required)
        :type tcp_flow_out: str
        :param udp_flow_in: [open/closed] (required)
        :type udp_flow_in: str
        :param udp_flow_out: [open/closed] (required)
        :type udp_flow_out: str
        :param cascade_to_nodes: replay command on all nodes
        :type cascade_to_nodes: bool
        :returns: generic success message
        :rtype: str
        """
        if not self._check_open_closed(
            [tcp_flow_in, tcp_flow_out, udp_flow_in, udp_flow_out]
        ):
            raise ValueError("open/closed are the only allowed values")
        return self._xmlrpc_query(
            "addPort",
            port=port,
            tcp_flow_in=tcp_flow_in,
            tcp_flow_out=tcp_flow_out,
            udp_flow_in=udp_flow_in,
            udp_flow_out=udp_flow_out,
            cascade_to_nodes=cascade_to_nodes,
        )

    def allow_deny_ips(self, **kwargs):
        """ Set firewall ip address allow and deny lists.

        :param trusted_ips: a trusted IP string/list
        :type trusted_ips: str/list
        :param blocked_ips: a blocked IP string/list
        :type blocked_ips: str/list
        :returns: generic success message
        :rtype: str
        """
        kwargs = self._ensure_licensing_ip_allowed(**kwargs)
        return self._xmlrpc_query("allowDenyIps", **kwargs)

    def delete(self, *, ports):
        """ Delete firewall port configuration.

        :param ports: port numbers to delete configuration for (required)
        :type ports: str/list
        :returns: generic success message
        :rtype: str
        """
        return self._xmlrpc_query("delete", ports=ports)

    def ipv6_settings(
        self, ip6tables_status="manual", icmp6_control="managed", cascade_to_nodes=True
    ):
        """ Controls how IPv6 Settings are handled when restarting the
        firewall.

        :param ip6tables_status: [off/manual/managed] (default: manual) 
        :type ip6tables_status: str
        :param icmp6_control: [default/managed] (default: managed)
        :type icmp6_control: str
        :param cascade_to_nodes: replay command on nodes (default: True)
        :type cascade_to_nodes: bool
        :returns: generic success message
        :rtype: str
        """
        if ip6tables_status not in ["off", "manual", "managed"]:
            raise ValueError("ip6tables_status must be off/manual/managed")
        if icmp6_control not in ["default", "managed"]:
            raise ValueError("icmp6_control must be default/managed")
        return self._xmlrpc_query(
            "ipv6Settings",
            ip6tables_status=ip6tables_status,
            icmp6_control=icmp6_control,
            cascade_to_nodes=self.falsey(cascade_to_nodes),
        )

    def is_running(self):
        """ Checks if the service is running or not.

        :returns: whether the service is running or not
        :rtype: bool
        """
        return self._xmlrpc_query("isRunning")

    def is_running_on_node(self, **kwargs):
        """ Checks if the service is running on a specific node (clustering
        only).

        :param node_id: the node id as a string
        :type node_id: str
        :returns: generic success message
        :rtype: str
        """
        return self._xmlrpc_query("isRunningOnNode", **kwargs)

    def list_general_name(self):
        """ Lists the "normal" name - ie "web server" instead of httpd.

        :returns: the general name
        :rtype: str
        """
        return self._xmlrpc_query("listGeneralName")

    def list_port_numbers(self):
        """ Lists a string of the port numbers that this services uses,
        comma-separated.

        :returns: the comma-separated list of ports used by the service
        :rtype: str
        """
        return self._xmlrpc_query("listPortNumbers")

    def list_port_numbers_array(self):
        """ Lists an array of the port numbers that this services uses,
        comma-separated.

        :returns: a list of port numbers and arrays as strings
        :rtype: list
        """
        return self._xmlrpc_query("listPortNumbersArray")

    def list_required_permissions(self):
        """ List permissions required to control the service.

        :returns: list of required permissions as strings
        :rtype: list
        """
        return self._xmlrpc_query("listRequiredPermissions")

    def list_service_info(self):
        """ Lists the service name, ports, page, and status.

        :returns: information about the service
        :rtype: dict
        """
        return self._xmlrpc_query("listServiceInfo")

    def list_service_name(self):
        """ Lists the service name - ie "httpd" instead of "web server'.

        :returns: the service name
        :rtype: str
        """
        return self._xmlrpc_query("listServiceName")

    def list_service_page(self):
        """ List the page that controls the service.

        :returns: the service page
        :rtype: str
        """
        return self._xmlrpc_query("listServicePage")

    def query_allow_deny_ips(self):
        """ Displays the information available to the action "allowDenyIps".

        :returns: two lists (trusted_ips and blocked_ips)
        :rtype: tuple
        """
        trusted_ips = []
        blocked_ips = []
        response = self._xmlrpc_query("queryAllowDenyIps")
        for ip in response["trusted_ips"]:
            trusted_ips.append(ip)
        for ip in response["blocked_ips"]:
            blocked_ips.append(ip)
        return trusted_ips, blocked_ips

    def query_ipv6_settings(self):
        """ Display the information available to the action "ipv6Settings".

        :returns: information available to action ipv6settings
        :rtype: dict
        """
        return self._xmlrpc_query("queryIpv6Settings")

    def restart(self, *, cascade_to_nodes=True):
        """ Restart the firewall service.

        :param cascade_to_nodes: replay on nodes (default: True)
        :type cascade_to_nodes: bool
        :returns: generic success message
        :rtype: str
        """
        return self._xmlrpc_query(
            "restart", cascade_to_nodes=self.falsey(cascade_to_nodes)
        )

    def restart_on_node(self, **kwargs):
        """ Restarts the service on a specific node (Clustering only)

        :param node_id: the node id
        :type: node_id: str
        :returns: generic success message
        :rtype: str
        """
        return self._xmlrpc_query("restartOnNode", **kwargs)

    def start(self, *, cascade_to_nodes=True):
        """ Starts the service

        :param cascade_to_nodes: replay on nodes (default: True)
        :type cascade_to_nodes: bool
        :returns: generic success message
        :rtype: str
        """
        return self._xmlrpc_query(
            "start", cascade_to_nodes=self.falsey(cascade_to_nodes)
        )

    def start_on_boot(self, *, startonboot=True, cascade_to_nodes=True):
        """ Set the firewall start-on-boot status

        :param startonboot: Whether to start on boot (default: True)
        :type startonboot: bool
        :param cascade_to_nodes: replay on nodes (default: True)
        :type cascade_to_nodes: bool
        :returns: generic success message
        :rtype: str
        """
        return self._xmlrpc_query(
            "startOnBoot",
            startonboot=self.falsey(startonboot),
            cascade_to_nodes=self.falsey(cascade_to_nodes),
        )

    def start_on_node(self, **kwargs):
        """ Starts the service on a specific node (Clustering only)

        :param node_id: the node id
        :type: node_id: str
        :returns: generic success message
        :rtype: str
        """
        return self._xmlrpc_query("startOnNode", **kwargs)

    def stop(self, **kwargs):
        """ Stops the service

        :param cascade_to_nodes: replay on nodes (default: True)
        :type cascade_to_nodes: bool
        :returns: generic success message
        :rtype: str
        """
        return self._xmlrpc_query("stop", **kwargs)

    def stop_on_node(self, **kwargs):
        """ Stops the service on a specific node (Clustering only)

        :param node_id: the node id
        :type: node_id: str
        :returns: generic success message
        :rtype: str
        """
        return self._xmlrpc_query("stopOnNode", **kwargs)

    def update(self, *, ports, **kwargs):
        """ Update a port in the firewall configuration

        :param ports: which port to update
        :type ports: str
        :param tcp_flow_in: [none/open/closed]
        :type tcp_flow_in: str
        :param tcp_flow_out: [none/open/closed]
        :type tcp_flow_out: str
        :param udp_flow_in: [none/open/closed]
        :type udp_flow_in: str
        :param udp_flow_out: [none/open/closed]
        :type udp_flow_out: str
        :returns: generic success message
        :rtype: str
        """
        return self._xmlrpc_query("update", ports=ports, **kwargs)

    def update_config(
        self,
        *,
        debug_mode=False,
        default_tos=4,
        tcp_drop_policy="DROP",
        udp_drop_policy="DROP",
        block_multicast=False,
        block_private_network=False,
        set_egress_filter=False,
        max_sessions=34576,
        sysctl_tcp=True,
        interface="eth0",
        cascade_to_nodes=True,
        **kwargs
    ):
        """ Update basic firewall configuration

        :param debug_mode: when enabled, firewall rules are flushed every 5
            minutes to prevent being locked out (default: False)
        :type debug_mode: bool
        :param default_tos: defines the default type of service (default: 4)
        :type default_tos: int
        :param tcp_drop_policy: [RESET/DROP/REJECT] defines how tcp packets are filtered. (default: DROP)
        :type tcp_drop_policy: str
        :param udp_drop_policy: [RESET/DROP/REJECT] defines how udp packets are filtered. (default: DROP)
        :type udp_drop_policy: str
        :param block_multicast: defines if firewall should block multicast traffic (default: False)
        :type block_multicast: bool
        :param block_private_network: defines if firewall should block all private ipv4 addresses (default: False)
        :type block_private_network: bool
        :param set_egress_filter: outbound egress filtering provides full outbound packet filtering (default: False)
        :type set_egress_filter: bool
        :param max_sessions: defines max connection tracking entries to can be handled simultaneously (default: 34576)
        :type max_sessions: int
        :param sysctl_tcp: enabled or disables sysctl hook changes to harden the kernel from certain network-based attacks. (default: True)
        :type sysctl_tcp: bool
        :param interface: all traffic on defined interface will be subject to all firewall rules (default: eth0)
        :type interface: str
        :param tifs: all traffic on defined interface(s) will bypass all firewall rules
        :type tifs: str/list
        :param cascade_to_nodes: replay on nodes
        :type cascade_to_nodes: bool
        :returns: generic success message
        :rtype: str
        """
        return self._xmlrpc_query(
            "updateConfig",
            debug_mode=self.falsey(debug_mode),
            default_tos=default_tos,
            tcp_drop_policy=tcp_drop_policy,
            udp_drop_policy=udp_drop_policy,
            block_multicast=self.falsey(block_multicast),
            block_private_network=self.falsey(block_private_network),
            set_egress_filter=self.falsey(set_egress_filter),
            max_sessions=max_sessions,
            sysctl_tcp=self.falsey(sysctl_tcp),
            interface=interface,
            cascade_to_nodes=self.falsey(cascade_to_nodes),
            **kwargs
        )

