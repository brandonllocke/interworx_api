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
        accounts = []
        for account in self._api_request('listAccounts'):
            accounts.append(SiteWorxAccount(account))
        return accounts

    def list_bandwidth_and_storage_in_mb(self):
        accounts = []
        for account in self._api_request('listBandwidthAndStorageInMB'):
            accounts.append(BandwidthAndStorage(account))
        return accounts

    def list_config(self, **attributes):
        fields = {'required': {'master_domain': str}}
        return self._api_request('listConfig', fields=fields, **attributes)

    def list_current_domain_and_bandwidth_data(self):
        domains = []
        for domain in self._api_request('listCurrentDomainBandwidthData'):
            domains.append(BandwidthByDomain(domain))
        return domains

    def list_dedicated_free_ips(self):
        ips = []
        for ip in self._api_request('listDedicatedFreeIps'):
            if ip[0] != '':
                ips.append(ip[0])
        return ips

    def list_domain_accounts(self):
        accounts = []
        for account in self._api_request('listDomainAccounts'):
            accounts.append(DomainAccounts(account))
        return accounts

    def list_free_ips(self):
        ips = []
        for ip in self._api_request('listFreeIps'):
            if ip[0] != '':
                ips.append(ip[0])
        return ips

    def list_master_domains(self):
        master_domains = []
        for domain in self._api_request('listMasterDomains'):
            master_domains.append(domain)
        return master_domains

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
        accounts = []
        for account in self._api_request('queryEdit'):
            accounts.append(QueryEdit(account))
        return accounts



class SiteWorxAccount:
    def __init__(self, info):
        self.siteworx_id = info.get('siteworx_id')
        self.uniqname = info.get('uniqname')
        self.date_created = info.get('date_created')
        self.status = info.get('status')
        self.nodeworx_id = info.get('nodeworx_id')
        self.package_id = info.get('package_id')
        self.nickname = info.get('nickname')
        self.email = info.get('email')
        self.user_type = info.get('user_type')
        self.domain = info.get('domain')
        self.domain_type = info.get('domain_type')
        self.storage = info.get('storage')
        self.storage_pct = info.get('storage_pct')
        self.bandwidth = info.get('bandwidth')
        self.bandwidth_pct = info.get('bandwidth_pct')
        self.max_bandwidth = info.get('max_bandwidth')
        self.max_storage = info.get('max_storage')
        self.is_favorite = info.get('is_favorite')
        self.php_version = info.get('php_version')
        self.homedir = info.get('homedir')
        self.domainroot = info.get('domainroot')
        self.docroot = info.get('docroot')

    def __str__(self):
        return self.domain
    
    def __repr__(self):
        return self.domain


class BandwidthAndStorage:
    def __init__(self, info):
        self.id = info.get('id')
        self.domain = info.get('domain')
        self.bandwidth_used = info.get('bandwidth_used')
        self.bandwidth = info.get('bandwidth')
        self.storage_used = info.get('storage_used')
        self.storage = info.get('storage')

    def __str__(self):
        return self.domain
    
    def __repr__(self):
        return self.domain


class BandwidthByDomain:
    def __init__(self, info):
        self.reseller_id = info.get('reseller_id')
        self.email = info.get('email')
        self.domain_name = info.get('domain_name')
        self.master_domain = info.get('master_domain')
        self.bw_type = info.get('bw_type')
        self.in_counter = info.get('in_counter')
        self.out_counter = info.get('out_counter')
        self.in_bytes = info.get('in_bytes')
        self.out_bytes = info.get('out_bytes')
    
    def __str__(self):
        return self.domain_name
    
    def __repr__(self):
        return self.domain_name


class DomainAccounts:
    def __init__(self, info):
        self.siteworx_id = info.get('siteworx_id')
        self.uniqname = info.get('uniqname')
        self.date_created = info.get('date_created')
        self.status = info.get('status')
        self.nodeworx_id = info.get('nodeworx_id')
        self.package_id = info.get('package_id')
        self.nickname = info.get('nickname')
        self.email = info.get('email')
        self.user_type = info.get('user_type')
        self.domain = info.get('domain')
        self.domain_type = info.get('domain_type')
        self.storage = info.get('storage')
        self.storage_pct = info.get('storage_pct')
        self.bandwidth = info.get('bandwidth')
        self.bandwidth_pct = info.get('bandwidth_pct')
        self.max_bandwidth = info.get('max_bandwidth')
        self.max_storage = info.get('max_storage')
        self.is_favorite = info.get('is_favorite')
        self.php_version = info.get('php_version')
        self.homedir = info.get('homedir')
        self.domainroot = info.get('domainroot')
        self.docroot = info.get('docroot')

    def __str__(self):
        return self.domain
    
    def __repr__(self):
        return self.domain

class QueryEdit:
    def __init__(self, info):
        self.info = info
        self.master_domain = info.get('master_domain')
        self.master_domain_ipv4 = info.get('master_domain_ipv4')
        self.database_server = info.get('database_server')
        self.reseller = info.get('reseller')
        self.uniqname = info.get('uniqname')
        self.status = info.get('status')
        self.nickname = info.get('nickname')
        self.email = info.get('email')
        self.encrypted = info.get('encrypted')
        self.password = info.get('password')
        self.confirm_password = info.get('confirm_password')
        self.language = info.get('langauge')
        self.theme = info.get('theme')
        self.menu_style = info.get('menu_style')
        self.billing_day = info.get('billing_day')
        self.additional_ipv4 = self.sort_ip_array('additional_ipv4')
        self.ipv6_pool = info.get('ipv6_pool')
        self.additional_ipv6 = self.sort_ip_array('additional_ipv6')
        self.php_version = info.get('php_version')
        self.php_available = info.get('php_available')
        self.packagetemplate = info.get('packagetemplate')
        self.OPT_STORAGE = info.get('OPT_STORAGE')
        self.OPT_BANDWIDTH = info.get('OPT_BANDWIDTH')
        self.OPT_EMAIL_ALIASES = info.get('OPT_EMAIL_ALIASES')
        self.OPT_EMAIL_AUTORESPONDERS = info.get('OPT_EMAIL_AUTORESPONDERS')
        self.OPT_EMAIL_BOXES = info.get('OPT_EMAIL_BOXES')
        self.OPT_EMAIL_GROUPS = info.get('OPT_EMAIL_GROUPS')
        self.OPT_FTP_ACCOUNTS = info.get('OPT_FTP_ACCOUNTS')
        self.OPT_MYSQL_DBS = info.get('OPT_MYSQL_DBS')
        self.OPT_MYSQL_DB_USERS = info.get('OPT_MYSQL_DB_USERS')
        self.OPT_POINTER_DOMAINS = info.get('OPT_POINTER_DOMAINS')
        self.OPT_SLAVE_DOMAINS = info.get('OPT_SLAVE_DOMAINS')
        self.OPT_SUBDOMAINS = info.get('OPT_SUBDOMAINS')
        self.OPT_BACKUP = info.get('OPT_BACKUP')
        self.OPT_CGI_ACCESS = info.get('OPT_CGI_ACCESS')
        self.OPT_CRONTAB = info.get('OPT_CRONTAB')
        self.OPT_DNS_RECORDS = info.get('OPT_DNS_RECORDS')
        self.OPT_SSL = info.get('OPT_SSL')
        self.OPT_BURSTABLE = info.get('OPT_BURSTABLE')
        self.OPT_SAVE_XFER_LOGS = info.get('OPT_SAVE_XFER_LOGS')
        self.fpm_max_children = info.get('fpm_max_children')
        self.fpm_max_requests = info.get('fpm_max_requests')
        self.fpm_process_management = info.get('fpm_process_management')
        self.fpm_start_servers = info.get('fpm_start_servers')
        self.fpm_min_spare_servers = info.get('fpm_min_spare_servers')
        self.fpm_max_spare_servers = info.get('fpm_max_spare_servers')
        self.fpm_process_idle_timeout = info.get('fpm_process_idle_timeout')
        self.simplescripts = info.get('simplescripts')
        self.domain = info.get('domain')
        self.options = Options(info.get('options'))
        self.ipaddr = info.get('ipaddr')
        self.password1 = info.get('password1')
        self.password2 = info.get('password2')
        self.package_name = info.get('package_name')

    def __str__(self):
        return self.master_domain
    
    def __repr__(self):
        return self.master_domain

    def sort_ip_array(self, field):
        ips = []
        for ip in self.info.get(field):
            ips.append(ip)
        return ips

class Options:
    def __init__(self, options):
        self.LG_OPT_STORAGE = options.get('LG_OPT_STORAGE')
        self.LG_OPT_BANDWIDTH = options.get('LG_OPT_BANDWIDTH')
        self.LG_OPT_EMAIL_ALIASES = options.get('LG_OPT_EMAIL_ALIASES')
        self.LG_OPT_EMAIL_AUTORESPONDERS = options.get('LG_OPT_EMAIL_AUTORESPONDERS')
        self.LG_OPT_EMAIL_BOXES = options.get('LG_OPT_EMAIL_BOXES')
        self.LG_OPT_EMAIL_GROUPS = options.get('LG_OPT_EMAIL_GROUPS')
        self.LG_OPT_FTP_ACCOUNTS = options.get('LG_OPT_FTP_ACCOUNTS')
        self.LG_OPT_MYSQL_DBS = options.get('LG_OPT_MYSQL_DBS')
        self.LG_OPT_MYSQL_DB_USERS = options.get('LG_OPT_MYSQL_DB_USERS')
        self.LG_OPT_POINTER_DOMAINS = options.get('LG_OPT_POINTER_DOMAINS')
        self.LG_OPT_SLAVE_DOMAINS = options.get('LG_OPT_SLAVE_DOMAINS')
        self.LG_OPT_SUBDOMAINS = options.get('LG_OPT_SUBDOMAINS')
        self.LG_OPT_BACKUP = options.get('LG_OPT_BACKUP')
        self.LG_OPT_CGI_ACCESS = options.get('LG_OPT_CGI_ACCESS')
        self.LG_OPT_CRONTAB = options.get('LG_OPT_CRONTAB')
        self.LG_OPT_DNS_RECORDS = options.get('LG_OPT_DNS_RECORDS')
        self.LG_OPT_SSL = options.get('LG_OPT_SSL')
        self.LG_OPT_BURSTABLE = options.get('LG_OPT_BURSTABLE')
        self.LG_OPT_SAVE_XFER_LOGS = options.get('LG_OPT_SAVE_XFER_LOGS')