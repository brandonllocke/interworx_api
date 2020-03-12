from .controller import Controller

class Firewall(Controller):
    def __init__(self, server):
        super().__init__(server)
        self.controller = '/nodeworx/firewall'

    def add_port(self, **attributes):
        fields = {
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
        return self._api_request('addPort', fields=fields, **attributes)

    def allow_deny_ips(self, **attributes):
        fields = {
            'required': {},
            'optional': {
                'trusted_ips': list,
                'blocked_ips': list
            }
        }
        return self._api_request('allowDenyIps', fields=fields, **attributes)

    def delete(self, **attributes):
        fields = {
            'required': {'ports': list},
            'optional': {}
        }
        return self._api_request('delete', fields=fields, **attributes)

    def ipv6_settings(self, **attributes):
        fields = {
            'required': {},
            'optional': {
                'ip6tables_status': str,
                'icmp6_control': str,
                'cascade_to_nodes': int
            }
        }
        return self._api_request('ipv6Settings', fields=fields, **attributes)

    def is_running(self):
        return self._api_request('isRunning')
    
    def is_running_on_node(self, **attributes):
        fields = {
            'required': {},
            'optional': {'node_id': str}
        }
        return self._api_request('isRunningOnNode', fields=fields, **attributes)

    def query_allow_deny_ips(self, **attributes):
        trusted_ips = []
        blocked_ips = []
        response = self._api_request('queryAllowDenyIps', **attributes)
        for ip in response['trusted_ips']:
            trusted_ips.append(ip)
        for ip in response['blocked_ips']:
            blocked_ips.append(ip)
        return trusted_ips, blocked_ips

    def query_ipv6_settings(self, **attributes):
        return self._api_request('queryIpv6Settings', **attributes)

    def restart(self, **attributes):
        fields = {
            'required': {},
            'optional': {'cascade_to_nodes': int}
        }
        return self._api_request('restart', fields=fields, **attributes)

    def restart_on_node(self, **attributes):
        fields = {
            'required': {},
            'optional': {'node_id': str}
        }
        return self._api_request('restartOnNode', fields=fields, **attributes)
    
    def start(self, **attributes):
        fields = {
            'required': {},
            'optional': {'cascade_to_nodes': int}
        }
        return self._api_request('start', fields=fields, **attributes)

    def start_on_boot(self, **attributes):
        fields = {
            'required': {},
            'optional': {
                'startonboot': int,
                'cascade_to_nodes': int
            }
        }
        return self._api_request('startOnBoot', fields=fields, **attributes)

    def start_on_node(self, **attributes):
        fields = {
            'required': {},
            'optional': {
                'node_id': int
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
                'node_id': int
            }
        }
        return self._api_request('stopOnNode', fields=fields, **attributes)
    
    def update(self, **attributes):
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
        return self._api_request('update', fields=fields, **attributes)
    
    def update_config(self, **attributes):
        fields = {
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
        return self._api_request('updateConfig', fields=fields, **attributes)