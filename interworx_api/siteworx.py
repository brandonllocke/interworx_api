from .controller import Controller


class SWAccounts(Controller):
    def __init__(self, server):
        super().__init__(server)
        self.controller = "/nodeworx/siteworx"

    def add(
        self,
        *,
        master_domain,
        master_domain_ipv4,
        uniqname,
        email,
        password,
        confirm_password,
        OPT_STORAGE,
        OPT_BANDWIDTH,
        OPT_EMAIL_ALIASES,
        OPT_EMAIL_AUTORESPONDERS,
        OPT_EMAIL_BOXES,
        OPT_EMAIL_GROUPS,
        OPT_FTP_ACCOUNTS,
        OPT_MYSQL_DBS,
        OPT_MYSQL_DB_USERS,
        OPT_POINTER_DOMAINS,
        OPT_SLAVE_DOMAINS,
        OPT_SUBDOMAINS,
        **kwargs
    ):
        """Add a SiteWorx account.

        Args:
            master_domain (str): (required) the domain you want to setup
                (without the www. prefix)
            master_domain_ipv4 (str): (required) the ip address you want the
                account to use
            uniqname (str): (required) a unique unix username for the account
            email (str): (required) email address for the account owner
            password (str): (required) password for the account
            confirm_password (str): (required) password for the account
            OPT_STORAGE (int): (required) storage space allowed in megabytes
            OPT_BANDWIDTH (int): (required) bandwidth allowed in Gigabytes
                per month
            OPT_EMAIL_ALIASES (int): (required) the number of email aliases
                (also known as email forwards) allowed
            OPT_EMAIL_AUTORESPONDERS (int): (required) the number of email
                autoresponders, also called robots, allowed
            OPT_EMAIL_BOXES (int): (required) the number of POP3/IMAP email
                boxes allowed
            OPT_EMAIL_GROUPS (int): (required) number of group email (aliases
                that send to multiple recipients) accounts allowed
            OPT_FTP_ACCOUNTS (int): (required) the number of FTP accounts
                allowed
            OPT_MYSQL_DBS (int): (required) the number of MySQL databases
                allowed
            OPT_MYSQL_DB_USERS (int): (required) the number of MySQL users
                allowed
            OPT_POINTER_DOMAINS (int): (required) the number of domains that
                can be pointed to this domain (sometimes called "parked"
                domains)
            OPT_SLAVE_DOMAINS (int): (required) the number of secondary
                domains allowed. Sometimes called "add-on" domains.
            OPT_SUBDOMAINS (int): (required) the number of subdomains allowed
            ipv6_pool (str): ipv6 pool the account should use
            master_domain_ipv6_from_pool (str): master domain ipv6 pool
            master_domain_ipv6 (str): master domain ipv6 address
            database_server (str): select the database server that the
                account should use
            nickname (str): a 'nickname' can be given to each SiteWorx
                account holder
            encrypted (str): [y/n] whether the password is already encrypted
                or not
            language (str): langauge used for user when logged in (default:
                en-us)
            theme (str): theme used for user (default: calliope)
            menu_style (str): [big/small] the menu style for the user
            billing_day (int): the day for calculating monthly bandwidth
                (default: 0)
            additional_ipv4 (list): additional ip addresses for account
            additional_ipv6 (list): additional ipv6 addresses for account
            php_version (str): the php version used for the master domain
            php_available (list): the php versions available to the account
            packagetemplate (str): package template blueprint for account
            create_package (int): (0/1) whether to create a new package
                 template or not
            new_package_name (str): name for package (if creating one)
            OPT_BACKUP (int): (0/1) allows the account to backup (default: 0)
            OPT_CGI_ACCESS (int): (0/1) whether to grant CGI script access
                (default: 0)
            OPT_CRONTAB (int): (0/1) whether to grant access to crontab
                (default: 0)
            OPT_DNS_RECORDS (int): (0/1) whether to allow access to edit DNS
                records (default:0)
            OPT_SSL (int): (0/1) whether to allow SSL certifications
                (default: 0)
            OPT_BURSTABLE (int): (0/1) allows an account to go over bandwidth
                allotment (default: 0)
            OPT_SAVE_XFER_LOGS (int): (0/1) allows account to write/save
                transfer log (default: 0)
            fpm_max_children (int): simultaneous request limit (default: 4)
            fpm_max_requests (int): number of child processes limit (default:
                8192)
            fpm_process_management (int): [dynamic/static/ondemand] choose
                how the process manager will control the number of child
                processes (default: ondemand)
            fpm_start_servers (int): the number of child processes created on
                startup. Used only when process management is set to dynamic
                (default: 2)
            fpm_min_spare_servers (int): the desired minimum number of idle
                server processes. Used only when pm is set to dynamic
                (default: 1)
            fpm_max_spare_servers (int): the desired maximum number of idle
                server processes. Used only when process management is set
                to dynamic. (default: 4)
            fpm_process_idle_timeout (int): the number of seconds after which
                an idle process will be killed. Used only when process
                management is set to ondemand. available units s(econds),
                m(inutes), h(ours), or d(ays).
            restart_httpd (int): (0/1) whether to restart httpd on account
                creation (default: 1)
            simplescripts (int): (0/1) whether to enable simplescripts
                (default: 1)

        Returns:
            str: generic success message
        """
        return self._xmlrpc_query(
            "add",
            master_domain=master_domain,
            master_domain_ipv4=master_domain_ipv4,
            uniqname=uniqname,
            email=email,
            password=password,
            confirm_password=confirm_password,
            OPT_STORAGE=OPT_STORAGE,
            OPT_BANDWIDTH=OPT_BANDWIDTH,
            OPT_EMAIL_ALIASES=OPT_EMAIL_ALIASES,
            OPT_EMAIL_AUTORESPONDERS=OPT_EMAIL_AUTORESPONDERS,
            OPT_EMAIL_BOXES=OPT_EMAIL_BOXES,
            OPT_EMAIL_GROUPS=OPT_EMAIL_GROUPS,
            OPT_FTP_ACCOUNTS=OPT_FTP_ACCOUNTS,
            OPT_MYSQL_DBS=OPT_MYSQL_DBS,
            OPT_MYSQL_DB_USERS=OPT_MYSQL_DB_USERS,
            OPT_POINTER_DOMAINS=OPT_POINTER_DOMAINS,
            OPT_SLAVE_DOMAINS=OPT_SLAVE_DOMAINS,
            OPT_SUBDOMAINS=OPT_SUBDOMAINS,
            **kwargs
        )

    def add_ip(self, *, domain, **kwargs):
        """Adds an IP to the list of available IPs for a SiteWorx account.

        Args:
            domain (str): the domain to add the ip address for (required)
            ipv4 (list): the ipv4 address(es) to add to the account
            ipv6 (list): the ipv6 address(es) to add to the account

        Returns:
            str: generic success message
        """
        return self._xmlrpc_query("addIp", domain=domain, **kwargs)

    def delete(self, *, domain, **kwargs):
        """Delete a SiteWorx account.

        Args:
            domain (str/list): domain of the account (required)
            purge_pool_ipv6 (int): selecting this will cause any IPv6
                addresses for this SiteWorx account to be deactivated and
                released back to the Pool if not used elsewhere (default: 1)
            confirm_action (int): (default: 1)

        Returns:
            str: generic success message
        """
        return self._xmlrpc_query("delete", domain=domain, **kwargs)

    def delete_config(self, *, master_domain, **kwargs):
        """Delete SiteWorx Level Config Data.

        Args:
            master_domain (str): domain of the account
            config_name (str/list): config name to delete

        Returns:
           str: generic success message
        """
        return self._xmlrpc_query("deleteConfig", master_domain=master_domain, **kwargs)


    def edit(self, *, domain, **kwargs):
        """Edit a SiteWorx account.

        Args:
            domain (str): (required) the domain you want to setup
                (without the www. prefix)
            reseller (int): the id of the reseller editing the account
            status (int): (0/1) the status?
            nickname (str): a 'nickname' can be given to each SiteWorx
                account holder
            email (str): (required) email address for the account owner
            password (str): (required) password for the account
            confirm_password (str): (required) password for the account
            encrypted (str): [y/n] whether the password is already encrypted
                or not
            language (str): langauge used for user when logged in (default:
                en-us)
            theme (str): theme used for user (default: calliope)
            menu_style (str): [big/small] the menu style for the user
            billing_day (int): the day for calculating monthly bandwidth
                (default: 0)
            ipv6_pool (str): ipv6 pool the account should use
            php_version (str): the php version used for the master domain
            php_available (list): the php versions available to the account
            packagetemplate (str): package template blueprint for account
            OPT_STORAGE (int): (required) storage space allowed in megabytes
            OPT_BANDWIDTH (int): (required) bandwidth allowed in Gigabytes
                per month
            OPT_EMAIL_ALIASES (int): (required) the number of email aliases
                (also known as email forwards) allowed
            OPT_EMAIL_AUTORESPONDERS (int): (required) the number of email
                autoresponders, also called robots, allowed
            OPT_EMAIL_BOXES (int): (required) the number of POP3/IMAP email
                boxes allowed
            OPT_EMAIL_GROUPS (int): (required) number of group email (aliases
                that send to multiple recipients) accounts allowed
            OPT_FTP_ACCOUNTS (int): (required) the number of FTP accounts
                allowed
            OPT_MYSQL_DBS (int): (required) the number of MySQL databases
                allowed
            OPT_MYSQL_DB_USERS (int): (required) the number of MySQL users
                allowed
            OPT_POINTER_DOMAINS (int): (required) the number of domains that
                can be pointed to this domain (sometimes called "parked"
                domains)
            OPT_SLAVE_DOMAINS (int): (required) the number of secondary
                domains allowed. Sometimes called "add-on" domains.
            OPT_SUBDOMAINS (int): (required) the number of subdomains allowed
            OPT_BACKUP (int): (0/1) allows the account to backup (default: 0)
            OPT_CGI_ACCESS (int): (0/1) whether to grant CGI script access
                (default: 0)
            OPT_CRONTAB (int): (0/1) whether to grant access to crontab
                (default: 0)
            OPT_DNS_RECORDS (int): (0/1) whether to allow access to edit DNS
                records (default:0)
            OPT_SSL (int): (0/1) whether to allow SSL certifications
                (default: 0)
            OPT_BURSTABLE (int): (0/1) allows an account to go over bandwidth
                allotment (default: 0)
            OPT_SAVE_XFER_LOGS (int): (0/1) allows account to write/save
                transfer log (default: 0)
            fpm_max_children (int): simultaneous request limit (default: 4)
            fpm_max_requests (int): number of child processes limit (default:
                8192)
            fpm_process_management (int): [dynamic/static/ondemand] choose
                how the process manager will control the number of child
                processes (default: ondemand)
            fpm_start_servers (int): the number of child processes created on
                startup. Used only when process management is set to dynamic
                (default: 2)
            fpm_min_spare_servers (int): the desired minimum number of idle
                server processes. Used only when pm is set to dynamic
                (default: 1)
            fpm_max_spare_servers (int): the desired maximum number of idle
                server processes. Used only when process management is set
                to dynamic. (default: 4)
            fpm_process_idle_timeout (int): the number of seconds after which
                an idle process will be killed. Used only when process
                management is set to ondemand. available units s(econds),
                m(inutes), h(ours), or d(ays).
            simplescripts (int): (0/1) whether to enable simplescripts
                (default: 1)

        Returns:
            str: generic success message
        """
        return self._xmlrpc_query("edit", domain=domain, **kwargs)

    def list_accounts(self):
        """List SiteWorx accounts summary.

        Args:
            None

        Returns:
            list: a list containing dictionaries for each account
        """
        return self._xmlrpc_query("listAccounts")

    def list_bandwidth_and_storage_in_mb(self):
        """Lists bandwidth and storage usage for current billing period in
        megabytes.
        
        Args:
            None

        Returns:
            list: a list of dictionaries for each account
        """
        return self._xmlrpc_query("listBandwidthAndStorageInMB")

    def list_config(self, *, master_domain):
        """List all SiteWorx Level Config Data.

        Args:
            master_domain (str): the main domain of the siteworx account
                (required)
        
        Returns:
            dict: a dictionary of config settings
        """
        return self._xmlrpc_query("listConfig", master_domain=master_domain)

    def list_current_domain_and_bandwidth_data(self):
        """List bandwidth data for all master and secondary domains for the
        active billing period.

        Args:
            None

        Returns:
            list: a list of dictionaries for each account
        """
        return self._xmlrpc_query("listCurrentDomainBandwidthData")

    def list_dedicated_free_ips(self):
        """List available dedicated ip addresses.

        Args:
            None

        Returns:
            list: a list of available ip addresses as str
        """
        ips = []
        for ip in self._xmlrpc_query("listDedicatedFreeIps"):
            if ip[0] != "":
                ips.append(ip[0])
        return ips

    def list_domain_accounts(self):
        """List SiteWorx accounts including master and secondary domain
        details.

        Args:
            None

        Returns:
            list: a list containing dictionaries for each domain account
        """
        return self._xmlrpc_query("listDomainAccounts")

    def list_free_ips(self):
        """List available ip addresses.

        Args:
            None

        Returns:
            list: a list of available ip addresses as str
        """
        ips = []
        for ip in self._api_request("listFreeIps"):
            if ip[0] != "":
                ips.append(ip[0])
        return ips

    def list_master_domains(self):
        """List master domains.

        Args:
            None

        Returns:
            list: a list of master domains as str
        """
        return self._xmlrpc_query("listMasterDomains")

    def list_shared_free_ips(self):
        """List available shared ip addresses.

        Args:
            None

        Returns:
            list: a list of available ip addresses as str
        """
        ips = []
        for ip in self._xmlrpc_query("listSharedFreeIps"):
            if ip[0] != "":
                ips.append(ip[0])
        return ips

    def match_packages_with_templates(self):
        """Find existing package template names and match account packages to
        them.

        Args:
            None

        Returns:
            str: generic success message
        """
        return self._xmlrpc_query("matchPackagesWithTemplates")

    def query_account_bandwidth(self, **kwargs):
        """Query SiteWorx Account bandwidth usage data for any billing period.

        Args:
            domains (str/list): domains of accounts to view data for
            timestamp (int): a unix timestamp to identify bulling period
                (default: blank (current time))

        Returns:
            list: a list of dictionaries for each account
        """
        return self._xmlrpc_query("queryAccountBandwidth", **kwargs)

    def query_available_ips(self, *, domain, **kwargs):
        """Displays IPs that are available to a master SiteWorx account.

        Args:
            domain (str): domain of the account to query against

        Returns:
           list: a list of dictionaries for each IP 
        """
        return self._xmlrpc_query("queryAvailableIps", domain=domain, **kwargs)

    def query_config(self, *, master_domain, config_name):
        """Query SiteWorx Level Config Data.

        Args:
            master_domain (str): the domain to query against
            config_name (str): the name of the config

        Returns:
            str: the current setting of the config
        """
        return self._xmlrpc_query(
            "queryConfig", master_domain=master_domain, config_name=config_name
        )

    def query_domain(self, *, domain):
        """Query the system for a domain information. Can be used to see if a
        domain exists.

        Args:
            domain (str): the domain to query against

        Returns:
            dict: a dictionary containing information about the domain
        """
        return self._xmlrpc_query("queryDomain", domain=domain)

    def query_domain_info(self, *, domain):
        """Get info about a domain on the system.

        Args:
            domain (str): the domain to get info about
        
        Returns:
            list: a list with a dictionary for each domain
        """
        return self._xmlrpc_query("queryDomainInfo", domain=domain)

    def query_edit(self, *, domain):
        """Displays the information available to the action "edit".

        Args:
           domain (str): the domain to query edit

        Returns:
           dict: a dictionary with all account information that can be edited
        """
        return self._xmlrpc_query("queryEdit", domain=domain)
