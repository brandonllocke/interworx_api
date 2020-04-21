from .controller import Controller

class SWAccounts(Controller):
    def __init__(self, server):
        super().__init__(server)
        self.controller = '/nodeworx/siteworx'

    def add(self, **attributes):
        fields = {
            'required': {
                'master_domain': str,
                'master_domain_ipv4': str,
                'uniqname': str,
                'email': str,
                'password': str,
                'confirm_password': str,
                'OPT_STORAGE': int,
                'OPT_BANDWIDTH': int,
                'OPT_EMAIL_ALIASES': int,
                'OPT_EMAIL_AUTORESPONDERS': int,
                'OPT_EMAIL_BOXES': int,
                'OPT_EMAIL_GROUPS': int,
                'OPT_FTP_ACCOUNTS': int,
                'OPT_MYSQL_DBS': int,
                'OPT_MYSQL_DB_USERS': int,
                'OPT_POINTER_DOMAINS': int,
                'OPT_SLAVE_DOMAINS': int,
                'OPT_SUBDOMAINS': int
            },
            'optional': {
                'ipv6_pool': str,
                'master_domain_ipv6_from_pool': str,
                'master_domain_ipv6': str,
                'database_server': str,
                'nickname': str,
                'encrypted': str,
                'language': str,
                'theme': str,
                'menu_style': str,
                'billing_day': int,
                'additional_ipv4': list,
                'additional_ipv6': list,
                'php_version': str,
                'php_available': list,
                'packagetemplate': str,
                'create_package': int,
                'new_package_name': str,
                'OPT_BACKUP': int,
                'OPT_CGI_ACCESS': int,
                'OPT_CRONTAB': int, 
                'OPT_DNS_RECORDS': int,
                'OPT_SSL': int,
                'OPT_BURSTABLE': int,
                'OPT_SAVE_XFER_LOGS': int,
                'fpm_max_children': int,
                'fpm_max_requests': int,
                'fpm_process_management': int,
                'fpm_start_servers': int,
                'fpm_min_spare_servers': int,
                'fpm_max_spare_servers': int,
                'fpm_process_idle_timeout': int,
                'restart_httpd': int,
                'simplescripts': int
            }
        }
        return self._api_request('add', fields=fields, **attributes)

    def add_ip(self, **attributes):
        fields = {
            'required': {'domain': str},
            'optional': {
                'ipv4': list,
                'ipv6': list
            }
        }
        return self._api_request('addIp', fields=fields, **attributes)

    def delete(self, **attributes):
        fields = {
            'required': {'domain': str},
            'optional': {
                'purge_pool_ipv6': int,
                'confirm_action': list
            }
        }
        return self._api_request('delete', fields=fields, **attributes)
    
    def delete_config(self, **attributes):
        fields = {
            'required': {'master_domain': str},
            'optional': {'config_name': list}
        }
        return self._api_request('deleteConfig', fields=fields, **attributes)

    def edit(self, **attributes):
        fields = {
            'required': {'domain': str},
            'optional': {
                'reseller': int,
                'status': int,
                'ipv6_pool': str,
                'master_domain_ipv6_from_pool': str,
                'master_domain_ipv6': str,
                'database_server': str,
                'nickname': str,
                'encrypted': str,
                'language': str,
                'theme': str,
                'menu_style': str,
                'billing_day': int,
                'php_version': str,
                'php_available': list,
                'packagetemplate': str,
                'OPT_STORAGE': int,
                'OPT_BANDWIDTH': int,
                'OPT_EMAIL_ALIASES': int,
                'OPT_EMAIL_AUTORESPONDERS': int,
                'OPT_EMAIL_BOXES': int,
                'OPT_EMAIL_GROUPS': int,
                'OPT_FTP_ACCOUNTS': int,
                'OPT_MYSQL_DBS': int,
                'OPT_MYSQL_DB_USERS': int,
                'OPT_POINTER_DOMAINS': int,
                'OPT_SLAVE_DOMAINS': int,
                'OPT_SUBDOMAINS': int,
                'OPT_BACKUP': int,
                'OPT_CGI_ACCESS': int,
                'OPT_CRONTAB': int,
                'OPT_DNS_RECORDS': int,
                'OPT_SSL': int,
                'OPT_BURSTABLE': int,
                'OPT_SAVE_XFER_LOGS': int,
                'fpm_max_children': int,
                'fpm_max_requests': int,
                'fpm_process_management': int,
                'fpm_start_servers': int,
                'fpm_min_spare_servers': int,
                'fpm_max_spare_servers': int,
                'fpm_process_idle_timeout': int,
                'simplescripts': int
            }
        }
        return self._api_request('edit', fields=fields, **attributes)

    def list_accounts(self):
        return self._api_request('listAccounts')

    def list_bandwidth_and_storage_in_mb(self):
        return self._api_request('listBandwidthAndStorageInMB')

    def list_config(self, **attributes):
        fields = {'required': {'master_domain': str}}
        return self._api_request('listConfig', fields=fields, **attributes)

    def list_current_domain_and_bandwidth_data(self):
        return self._api_request('listCurrentDomainBandwidthData')

    def list_dedicated_free_ips(self):
        ips = []
        for ip in self._api_request('listDedicatedFreeIps'):
            if ip[0] != '':
                ips.append(ip[0])
        return ips

    def list_domain_accounts(self):
        return self._api_request('listDomainAccounts')

    def list_free_ips(self):
        ips = []
        for ip in self._api_request('listFreeIps'):
            if ip[0] != '':
                ips.append(ip[0])
        return ips

    def list_master_domains(self):
        return self._api_request('listMasterDomains')

    def list_shared_free_ips(self):
        ips = []
        for ip in self._api_request('listSharedFreeIps'):
            if ip[0] != '':
                ips.append(ip[0])
        return ips

    def match_packages_with_templates(self):
        return self._api_request('matchPackagesWithTemplates')

    def query_account_bandwidth(self, **attributes):
        fields = {
            'optional': {
                'domains': list,
                'timestamp': int
            }
        }
        return self._api_request('queryAccountBandwidth', fields=fields, **attributes)

    def query_available_ips(self, **attributes):
        fields = {'required': {'domain': str}}
        return self._api_request('queryAvailableIps', fields=fields, **attributes)

    def query_config(self, **attributes):
        fields = {
            'required': {
                'master_domain': str,
                'config_name': str 
            }
        }
        return self._api_request('queryConfig', fields=fields, **attributes)

    def query_domain(self, **attributes):
        fields = {'required': {'domain': str}}
        return self._api_request('queryDomain', fields=fields, **attributes)

    def query_domain_info(self, **attributes):
        fields = {'required': {'domain': str}}
        return self._api_request('queryDomainInfo', fields=fields, **attributes)

    def query_edit(self, **attributes):
        return self._api_request('queryEdit')