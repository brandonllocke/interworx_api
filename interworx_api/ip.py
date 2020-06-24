from .controller import Controller


class IP(Controller):
    def __init__(self, server):
        super().__init__(server)
        self.controller = "/nodeworx/ip"
        self.sites = IPSites(server)

    def activate(self, *, ip):
        return self._xmlrpc_query('activate', ip=ip)

    def add(self, *, ip_start, ip_end, netmask, device, type, reseller, vip):
        return self._xmlrpc_query('add', ip_start=ip_start,
                                  ip_end=ip_end,
                                  netmask=netmask,
                                  device=device,
                                  type=type,
                                  reseller=reseller,
                                  vip=vip)
    
    def delete(self, *, ip, confirm_action):
        return self._xmlrpc_query('delete', ip=ip,
                                  confirm_action=confirm_action)

    def edit(self, *, ip, **kwargs):
        return self._xmlrpc_query('edit', ip=ip, **kwargs)
    
    def force_remove_vip_status(self, *, ip):
        return self._xmlrpc_query('forceRemoveVipStatus', ip=ip)

    def import_ip(self, *, ip):
        return self._xmlrpc_query('import', ip=ip)

    def list_ip_addresses(self):
        return self._xmlrpc_query('listIpAddresses')

    def query_domains(self, *, ip):
        return self._xmlrpc_query('queryDomains', ip=ip)

    def query_edit(self, *, ip):
        return self._xmlrpc_query('queryEdit', ip=ip)

    def query_ipv6_status(self):
        return self._xmlrpc_query('queryIPv6Status')

    def query_resellers(self, *, ip):
        return self._xmlrpc_query('queryResellers', ip=ip)

    def query_siteworx_accounts(self, *, ip):
        return self._xmlrpc_query('querySiteworxAccounts', ip=ip)

    def sync_ip_data(self, *, ip):
        return self._xmlrpc_query('syncIpData', ip=ip)

class IPSites(Controller):
    def __init__(self, server):
        super().__init__(server)
        self.controller = "/nodeworx/ip/sites"
    
    def default_sites_status(self, status=True):
        return self._xmlrpc_query('defaultSitesStatus', status=self.falsey(status))

    def disable_default_sites(self, **kwargs):
        return self._xmlrpc_query('disableDefaultSites', **kwargs)
    
    def enable_default_sites(self, **kwargs):
        return self._xmlrpc_query('enabledDefaultSites', **kwargs)

    def list_ip_default_sites(self):
        return self._xmlrpc_query('listIpDefaultSites')

    def query_default_sites_status(self):
        return self._xmlrpc_query('queryDefaultSitesStatus')

    def update_ip_default_sites(self, *, ip, **kwargs):
        return self._xmlrpc_query('updateIpDefaultSites', ip=ip, **kwargs)