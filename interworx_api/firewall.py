from .controller import Controller

class Firewall(Controller):
    def __init__(self, server):
        super().__init__(server)
        self.controller = '/nodeworx/firewall'

    def add_port(self, **attributes):
        possible_fields = {
            'required': {
                'port': str,
                'tcp_flow_in': str,
                'tcp_flow_out': str,
                'udp_flow_in': str,
                'udp_flow_out': str
            },
            'optional': {
                'cascade_to_nodes': int
            }
        }
        if self._parse_fields(possible_fields, **attributes):
            return self._xmlrpc_query('addPort', **attributes)

    def allow_deny_ips(self, **attributes):
        possible_fields = {
            'required': {},
            'optional': {
                'trusted_ips': list,
                'blocked_ips': list
            }
        }
        if self._parse_fields(possible_fields, **attributes):
            return self._xmlrpc_query('allowDenyIps', **attributes)

    def delete(self, **attributes):
        possible_fields = {
            'required': {'ports': list},
            'optional': {}
        }
        if self._parse_fields(possible_fields, **attributes):
            return self._xmlrpc_query('delete', **attributes)

    def ipv6_settings(self, **attributes):
        possible_fields = {
            'required': {},
            'optional': {
                'ip6tables_status': str,
                'icmp6_control': str,
                'cascade_to_nodes': int
            }
        }
        if self._parse_fields(possible_fields, **attributes):
            return self._xmlrpc_query('ipv6Settings', **attributes)

    def is_running(self):
        return self._xmlrpc_query('isRunning')
    
    def is_running_on_node(self, **attributes):
        possible_fields = {
            'required': {},
            'optional': {'node_id': str}
        }
        if self._parse_fields(possible_fields, **attributes):
            return self._xmlrpc_query('isRunningOnNode', **attributes)

    def query_allow_deny_ips(self, **attributes):
        trusted_ips = []
        blocked_ips = []
        response = self._xmlrpc_query('queryAllowDenyIps', **attributes)
        for ip in response['trusted_ips']:
            trusted_ips.append(ip)
        for ip in response['blocked_ips']:
            blocked_ips.append(ip)
        return trusted_ips, blocked_ips

    def query_ipv6_settings(self, **attributes):
        return self._xmlrpc_query('queryIpv6Settings', **attributes)

    def restart(self, **attributes):
        possible_fields = {
            'required': {},
            'optional': {'cascade_to_nodes': int}
        }
        if self._parse_fields(possible_fields, **attributes):
            return self._xmlrpc_query('restart', **attributes)

    def restart_on_node(self, **attributes):
        possible_fields = {
            'required': {},
            'optional': {'node_id': str}
        }
        if self._parse_fields(possible_fields, **attributes):
            return self._xmlrpc_query('restartOnNode', **attributes)
    
    def start(self, **attributes):
        possible_fields = {
            'required': {},
            'optional': {'cascade_to_nodes': int}
        }
        if self._parse_fields(possible_fields, **attributes):
            return self._xmlrpc_query('start')

    def start_on_boot(self, **attributes):
        possible_fields = {
            'required': {},
            'optional': {
                'startonboot': int,
                'cascade_to_nodes': int
            }
        }
        if self._parse_fields(possible_fields, **attributes):
            return self._xmlrpc_query('startOnBoot', **attributes)

    def start_on_node(self, **attributes):
        possible_fields = {
            'required': {},
            'optional': {
                'node_id': int
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
                'node_id': int
            }
        }
        if self._parse_fields(possible_fields, **attributes):
            return self._xmlrpc_query('stopOnNode', **attributes)
    
    def update(self, **attributes):
        possible_fields = {
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
        if self._parse_fields(possible_fields, **attributes):
            return self._xmlrpc_query('update', **attributes)
    
    def update_config(self, **attributes):
        possible_fields = {
            'required': {},
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
        if self._parse_fields(possible_fields, **attributes):
            return self._xmlrpc_query('updateConfig', **attributes)