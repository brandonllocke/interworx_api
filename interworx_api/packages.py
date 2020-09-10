from .controller import Controller

class Packages(Controller):
    def __init__(self, server):
        super().__init__(server)
        self.controller = "/nodeworx/packages"

   def add(self, *, 
           package_name, 
           is_default=False,
           OPT_STORAGE,
           OPT_BANDWIDTH,
           OPT_EMAIL_ALIASES,
           OPT_EMAIL_AUTORESPONDERS,
           OPT_EMAIL_GROUPS,
           OPT_FTP_ACCOUNTS,
           OPT_MYSQL_DBS,
           OPT_MYSQL_DB_USERS,
           OPT_POINTER_DOMAINS,
           OPT_SLAVE_DOMAINS,
           OPT_SUBDOMAINS,
           OPT_BACKUP,
           OPT_CGI_ACCESS,
           OPT_CRONTAB,
           OPT_DNS_RECORDS,
           OPT_SSL,
           OPT_BURSTABLE,
           OPT_SAVE_XFER_LOGS,
           fpm_max_children=4,
           fpm_max_requests=8192,
           fpm_process_management="ondemand",
           **kwargs):
        return self._xmlrpc_query(
            "add",
            package_name=package_name, 
            OPT_STORAGE=OPT_STORAGE,
            OPT_BANDWIDTH=OPT_BANDWIDTH,
            OPT_EMAIL_ALIASES=OPT_EMAIL_ALIASES,
            OPT_EMAIL_AUTORESPONDERS=OPT_EMAIL_AUTORESPONDERS,
            OPT_EMAIL_GROUPS=OPT_EMAIL_GROUPS,
            OPT_FTP_ACCOUNTS=OPT_FTP_ACCOUNTS,
            OPT_MYSQL_DBS=OPT_MYSQL_DBS,
            OPT_MYSQL_DB_USERS=OPT_MYSQL_DB_USERS,
            OPT_POINTER_DOMAINS=OPT_POINTER_DOMAINS,
            OPT_SLAVE_DOMAINS=OPT_SLAVE_DOMAINS,
            OPT_SUBDOMAINS=OPT_SUBDOMAINS,
            OPT_BACKUP=OPT_BACKUP,
            OPT_CGI_ACCESS=OPT_CGI_ACCESS,
            OPT_CRONTAB=OPT_CRONTAB,
            OPT_DNS_RECORDS=OPT_DNS_RECORDS,
            OPT_SSL=OPT_SSL,
            OPT_BURSTABLE=OPT_BURSTABLE,
            OPT_SAVE_XFER_LOGS=OPT_SAVE_XFER_LOGS,
            **kwargs
        ) 

def backup(self, *, id):
    return self._xmlrpc_query("backup", id=id)

def delete(self, *, id):
    return self._xmlrpc_query("delete", id=id)

def edit(self, *, id, **kwargs):
    return self._xmlrpc_query("edit", id=id, **kwargs)

def import_package(self, *, package_file, **kwargs):
    return self._xmlrpc_query("import", package_file=package_file, **kwargs)

def list_details(self):
    return self._xmlrpc_query("listDetails")

def list_packages(self):
    return self._xmlrpc_query("listPackages")