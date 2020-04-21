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
        fields = {
            'required': {'reseller': str},
        }
        return self._api_request('queryAccounts', fields=fields, **attributes)

    def query_backups(self, **attributes):
        fields = {
            'required': {'domain': str},
        }
        return self._api_request('queryBackups', fields=fields, **attributes)

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
        return self._api_request('listAllBackups', wd=wd, **attributes)

    def list_daily_backups(self, wd, **attributes):
        return self._api_request('listDailyBackups', wd=wd, **attributes)

    def list_weekly_backups(self, wd, **attributes):
        return self._api_request('listWeeklyBackups', wd=wd, **attributes)

    def list_monthly_backups(self, wd, **attributes):
        return self._api_request('listMonthlyBackups', wd=wd, **attributes)

    def restore(self, wd, **attributes):
        fields = {
            'required': {
                'filetype': str,
                'file': str
            },
        }
        return super().restore(fields=fields, wd=wd, **attributes)
