from .controller import Controller

class Cron(Controller):
    def __init__(self, server):
        super().__init__(server)


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
        return self._api_request('add', fields=fields, **attributes)

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
        return self._api_request('edit', fields=fields, **attributes)

    def get_current_system_time(self):
        return self._api_request('getCurrentSystemTime')

    def options(self, **attributes):
        fields = {
            'required': {'user': str},
            'optional': {
                'shell': str,
                'path': list,
                'mailto': str
            }
        }
        return self._api_request('options', fields=fields, **attributes)

    def query_edit(self, **attributes):
        parsed_jobs = []
        fields = {}

    def query_jobs(self, **attributes):
        parsed_jobs = []
        fields = {
            'required': {'user': str},
            'optional': {}
        }
        jobs = self._api_request('queryJobs', fields=fields, **attributes)
        print(jobs)
        for job in jobs:
            parsed_jobs.append(NodeWorxCronJob(job))
        return parsed_jobs

    
class NodeWorxCronJob:
    def __init__(self, info):
       self.user = info.get('user') 
       self.linenum = info.get('linenum')
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