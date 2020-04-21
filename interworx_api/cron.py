from .controller import Controller

class Cron(Controller):
    def __init__(self, server):
        super().__init__(server)

    def add(self, fields=None, wd=None, **attributes):
        return self._api_request('add', fields=fields, wd=wd, **attributes)

    def delete(self, fields=None, wd=None, **attributes):
        return self._api_request('delete', fields=fields, wd=wd, **attributes)

    def edit(self, fields=None, wd=None, **attributes):
        return self._api_request('edit', fields=fields, wd=wd, **attributes)
    
    def get_current_system_time(self):
        return self._api_request('getCurrentSystemTime')

    def options(self, fields=None, wd=None, **attributes):
        return self._api_request('options', fields=fields, wd=wd, **attributes)

    def query_edit(self, fields=None, wd=None, **attributes):
        return self._api_request('queryEdit', fields=fields, wd=wd, **attributes)

    def query_jobs(self, fields=None, wd=None, **attributes):
        return self._api_request('queryJobs', fields=fields, wd=wd, **attributes)


class NodeWorxCron(Cron):
    def __init__(self, server):
        super().__init__(server)
        self.controller = '/nodeworx/cron'

    def add(self, **attributes):
        fields = {
            'required': {
                'interface': str,
                'user': str,
                'script': str,
            },
            'optional': {
                'minute': list,
                'hour': list,
                'day': list,
                'month': list,
                'dayofweek': list
            }
        }
        return super().add(fields=fields, **attributes)

    def delete(self, **attributes):
        fields = {
            'required': {
                'user': str,
                'jobs': list
            }
        }
        return super().delete(fields=fields, **attributes)

    def edit(self, **attributes):
        fields = {
            'required': {
                'user': str,
                'job': str,
            },
            'optional': {
                'enabled': int,
                'minute': str,
                'hour': str,
                'day': str,
                'month': str,
                'dayofweek': str,
                'script': str,
            }
        }
        return super().edit(fields=fields, **attributes)

    def options(self, **attributes):
        fields = {
            'required': {
                'user': str,
            },
            'optional': {
                'shell': str,
                'path': list,
                'mailto': str
            }
        }
        return super().options(fields=fields, **attributes)

    def query_edit(self, **attributes):
        parsed_jobs = []
        fields = {
            'required': {
                'user': str,
                'job': int
            }
        }
        return super().query_edit(fields=fields, **attributes)

    def query_jobs(self, **attributes):
        fields = {'required': {'user': str}}
        return super().query_jobs(fields=fields, **attributes)
    
    def query_options(self, **attributes):
        fields = {'required': {'user': str}}
        return self._api_request('queryOptions', fields=fields, **attributes)


class SiteWorxCron(Cron):
    def __init__(self, server):
        super().__init__(server)
        self.controller = '/siteworx/cron'

    def add(self, wd, **attributes):
        fields = {
            'required': {'script': str},
            'optional': {
                'minute': list,
                'hour': list,
                'day': list,
                'month': list,
                'dayofweek': list
            }
        }
        return super().add(fields=fields, wd=wd, **attributes)

    def delete(self, wd, **attributes):
        fields = {
            'required': {'jobs': list}
        }
        return super().delete(fields=fields, wd=wd, **attributes)

    def edit(self, wd, **attributes):
        fields = {
            'required': {'job': int},
            'optional': {
                'enabled': int,
                'minute': str,
                'hour': str,
                'day': str,
                'month': str,
                'dayofweek': str,
                'script': str
            }
        }
        return super().edit(fields=fields, wd=wd, **attributes)

    def options(self, wd, **attributes):
        fields = {
            'required': {'user': str},
            'optional': {
                'shell': str,
                'path': list,
                'mailto': str
            }
        }
        return super().options(fields=fields, wd=wd, **attributes)
    
    def query_edit(self, wd, **attributes):
        parsed_jobs = []
        fields = {
            'required': {
                'job': int
            }
        }
        return super().query_edit(fields=fields, wd=wd, **attributes)

    def query_jobs(self, wd):
        return super().query_jobs(wd=wd)

    def query_options(self, wd):
        return self._api_request('queryOptions', wd=wd)