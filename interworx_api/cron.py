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
            },
            'optional': {}
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
            },
            'optional': {}
        }
        job = super().query_edit(fields=fields, **attributes)
        return NodeWorxCronQueryEdit(job)

    def query_jobs(self, **attributes):
        parsed_jobs = []
        fields = {
            'required': {'user': str},
            'optional': {}
        }
        jobs = super().query_jobs(fields=fields, **attributes)
        print(jobs)
        for job in jobs:
            parsed_jobs.append(NodeWorxCronJob(job))
        return parsed_jobs
    
    def query_options(self, **attributes):
        fields = {
            'required': {'user': str},
            'optional': {}
        }
        options = self._api_request('queryOptions', fields=fields, **attributes)
        return CronOptions(options)


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
            'required': {'jobs': list},
            'optional': {}
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
            },
            'optional': {}
        }
        job = self._api_request('queryEdit', fields=fields, **attributes)
        return NodeWorxCronQueryEdit(job)

    def query_jobs(self, wd, **attributes):
        parsed_jobs = []
        jobs = super().query_jobs(wd=wd, **attributes)
        for job in jobs:
            parsed_jobs.append(SiteWorxCronJob(job))
        return parsed_jobs

    def query_options(self, wd):
        options = self._api_request('queryOptions', wd=wd)
        return CronOptions(options[0])

    
class NodeWorxCronJob:
    def __init__(self, info):
       self.user = info.get('user') 
       self.number = info.get('linenum')
       self.status = info.get('status')
       self.minute = info.get('minute')
       self.hour = info.get('hour')
       self.day = info.get('day')
       self.month = info.get('month')
       self.dayofweek = info.get('dayofweek')
       self.script = info.get('script')

    def __str__(self):
        return self.script

    def __repr__(self):
        return self.script

    def print_like_crontab(self):
        crontab = [self.minute, self.hour, self.day,
                   self.month, self.dayofweek, self.script]
        return ' '.join(crontab)

class CronOptions:
    def __init__(self, info):
        self.shell = info.get('shell')
        self.path = info.get('path')
        self.mailto = info.get('mailto')


class NodeWorxCronQueryEdit:
    def __init__(self, info):
        self.systemtime = info.get('systemtime')
        self.enabled = info.get('enabled')
        self.minute = info.get('minute')
        self.hour = info.get('minute')
        self.day = info.get('day')
        self.month = info.get('month')
        self.dayofweek = info.get('dayofweek')
        self.script = info.get('script')
        self.user = info.get('user')
        self.job = info.get('job')

    def __str__(self):
        return self.script
    
    def __repr__(self):
        return self.script


class SiteWorxCronJob:
    def __init__(self, info):
        self.number = info.get('linenum')
        self.type = info.get('type')
        self.enabled = info.get('enabled')
        self.minute = info.get('minute')
        self.hour = info.get('hour')
        self.day = info.get('day')
        self.month = info.get('month')
        self.dayofweek = info.get('dayofweek')
        self.script = info.get('script')

    def __str__(self):
        return self.script

    def __repr__(self):
        return self.script