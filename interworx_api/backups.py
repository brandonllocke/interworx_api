from .controller import Controller

class Backups(Controller):
    def __init__(self, server):
        super().__init__(server)

    def restore(self, fields=None, wd=None, **attributes):
        return self._api_request('restore', fields=fields, wd=wd, **attributes)


class NodeWorxBackups(Backups):
    def __init__(self, server):
        super().__init__(server)
        self.controller = '/nodeworx/backup'

    def fullbackup(self, **attributes):
        fields = {
            'required': {'domains': list},
            'optional': {'email': str}
        }
        return self._api_request('fullbackup', fields=fields, **attributes)

    def query_accounts(self, **attributes):
        accounts = []
        fields = {
            'required': {'reseller': str},
        }
        response =  self._api_request('queryAccounts', fields=fields, **attributes)
        for account in response:
            accounts.append(AccountBackup(account))
        return accounts

    def query_backups(self, **attributes):
        backups = []
        fields = {
            'required': {'domain': str},
        }
        response =  self._api_request('queryBackups', fields=fields, **attributes)
        for backup in response:
            backups.append(Backup(backup))
        return backups

    def restore(self, **attributes):
        fields = {
            'required': {
                'domain': str,
                'file': str
            },
            'optional': {
                'confirm_action': int
            }
        }
        return super().restore(fields=fields, **attributes)

    def structureonly(self, **attributes):
        fields = {
            'required': {'domains': list},
            'optional': {'email': str}
        }
        return self._api_request('structureonly', fields=fields, **attributes)


class SiteWorxBackups(Backups):
    def __init__(self, server):
        super().__init__(server)
        self.controller = '/siteworx/backup'

    def _organize_backups(self, response):
        backups = []
        for backup in response:
            backups.append(Backup(backup))
        return backups

    def create(self, wd, **attributes):
        fields = {
            'required': {
                'type': str,
                'location': str
            },
            'optional': {
                'email_address': str,
                'domain_options': str,
                'exclude_extensions': list,
            }
        }
        if attributes.get('type') == 'partial':
            fields['required']['options'] = str
        return self._api_request('create', fields=fields, wd=wd, **attributes)

    def delete(self, wd, **attributes):
        fields = {
            'required': {'backups': list},
        }
        return self._api_request('delete', fields=fields, wd=wd, **attributes)

    def list_all_backups(self, wd, **attributes):
        response = self._api_request('listAllBackups', wd=wd, **attributes)
        return self._organize_backups(response)

    def list_daily_backups(self, wd, **attributes):
        response = self._api_request('listDailyBackups', wd=wd, **attributes)
        return self._organize_backups(response)

    def list_weekly_backups(self, wd, **attributes):
        response = self._api_request('listWeeklyBackups', wd=wd, **attributes)
        return self._organize_backups(response)

    def list_monthly_backups(self, wd, **attributes):
        response = self._api_request('listMonthlyBackups', wd=wd, **attributes)
        return self._organize_backups(response)

    def restore(self, wd, **attributes):
        fields = {
            'required': {
                'filetype': str,
                'file': str
            },
        }
        return super().restore(fields=fields, wd=wd, **attributes)


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
