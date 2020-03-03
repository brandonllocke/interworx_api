class Firewall:
    def __init__(self, server):
        self.server = server
        self.key = server.key
        self.controller = '/nodeworx/firewall'

    def _xmlrpc_query(self, action, **attributes):
        return self.server.get(self.key, self.controller, action, attributes)

    def add_port(self, **attributes):
        return self._xmlrpc_query('addPort', **attributes)

    def allow_deny_ips(self, **attributes):
        return self._xmlrpc_query('allowDenyIps', **attributes)

    def delete(self, **attributes):
        return self._xmlrpc_query('delete', **attributes)

    def ipv6_settings(self, **attributes):
        return self._xmlrpc_query('ipv6Settings', **attributes)

    def is_running(self):
        return self._xmlrpc_query('isRunning')

    def is_running_on_node(self, **attributes):
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
