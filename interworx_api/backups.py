class Backups:
    def __init__(self, server):
        self.server = server
        self.key = server.key

    def _modify_key(self, working_domain=None):
        if working_domain is not None:
            key = {'apikey': self.key, 'domain': working_domain}
            return key
        return self.key

    def _xmlrpc_query(self, action, working_domain=None, **attributes):
        key = self._modify_key(working_domain)
        return self.server.get(key, self.controller, action, attributes)

    def restore(self, working_domain=None, **attributes):
        return self._xmlrpc_query('restore', **attributes)


class NodeWorxBackups(Backups):
    def __init__(self, server):
        super().__init__(server)
        self.controller = '/nodeworx/backup'

    def fullbackup(self, **attributes):
        return self._xmlrpc_query('fullbackup', **attributes)

    def query_accounts(self, **attributes):
        accounts = []
        response = self._xmlrpc_query('queryAccounts', **attributes)
        for account in response:
            accounts.append(AccountBackup(account))
        return accounts

    def query_backups(self, **attributes):
        backups = []
        response = self._xmlrpc_query('queryBackups', **attributes)
        for backup in response:
            backups.append(Backup(backup))
        return backups

    def structureonly(self, **attributes):
        return self._xmlrpc_query('structureonly', **attributes)

class SiteWorxBackups(Backups):
    def __init__(self, server):
        super().__init__(server)
        self.controller = '/siteworx/backup'

    def _organize_backups(self, response):
        backups = []
        for backup in response:
            backups.append(Backup(backup))
        return backups

    def create(self, working_domain, **attributes):
        return self._xmlrpc_query('create', working_domain, **attributes)

    def delete(self, working_domain, **attributes):
        return self._xmlrpc_query('delete', working_domain, **attributes)

    def list_all_backups(self, working_domain, **attributes):
        response = self._xmlrpc_query('listAllBackups', working_domain, **attributes)
        return self._organize_backups(response)

    def list_daily_backups(self, working_domain, **attributes):
        response = self._xmlrpc_query('listDailyBackups', working_domain, **attributes)
        return self._organize_backups(response)

    def list_weekly_backups(self, working_domain, **attributes):
        response = self._xmlrpc_query('listWeeklyBackups', working_domain, **attributes)
        return self._organize_backups(response)

    def list_monthly_backups(self, working_domain, **attributes):
        response = self._xmlrpc_query('listMonthlyBackups', working_domain, **attributes)
        return self._organize_backups(response)

class Backup:
    def __init__(self, info):
        self.filepath = info.get('filepath')
        self.filename = info.get('filename')
        self.filesize = info.get('filesize')
        self.filesize_bytes = info.get('filesize_bytes')
        self.type = info.get('type')
        self.domain_options = info.get('domain_options')
        self.filedate = info.get('filedate')
        self.complete = info.get('complete')
        self.domain = info.get('domain', '')

    def __str__(self):
        return self.filename

    def __repr__(self):
        return self.filename

class AccountBackup:
    def __init__(self, info):
        self.name = info.get('username')
        self.nickname = info.get('nickname')
        self.email = info.get('email')
        self.domain = info.get('domain')
        self.backup_count = info.get('backup_count')
        self.backup_dir_size = info.get('backup_dir_size')
        self.nodeworx_id = info.get('nodeworx_id')

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name
