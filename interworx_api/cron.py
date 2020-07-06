from .controller import Controller


class NodeWorxCron(Controller):
    def __init__(self, server):
        super().__init__(server)
        self.controller = '/nodeworx/cron'

    def add(self, *, interface='simple', user, script, minute=["*"],
            hour=["*"], day=["*"], month=["*"], dayofweek=["*"]):
        """ Add a job to a user's crontab.

        :param interface: the type of menu to present [simple/advanced]
            (default: 'simple') (required)
        :type interface: str
        :param user: the user's crontab to add to (required)
        :type user: str
        :param script: the script to be run (required)
        :type script: str
        :param minute: cron formatted minute to run on (default: ["*"])
        :type minute: str/list
        :param hour: cron formatted hour to run on (default: ["*"])
        :type hour: str/list
        :param day: cron formatted day to run on (default: ["*"])
        :type day: str/list
        :param month: cron formatted month to run on (default: ["*"])
        :type month: str/list
        :param dayofweek: cron formatted day of the week to run on 
            (default: ["*"])
        :type dayofweek: str/list
        :returns: generic success message
        :rtype: str
        """
        return self._xmlrpc_query('add', interface=interface, user=user, script=script,
                                  minute=minute, hour=hour, day=day, month=month, dayofweek=dayofweek)

    def delete(self, *, user, jobs):
        """ Delete a job(s) from a user's crontab.

        :params user: the user's crontab to delete from (required)
        :type user: str
        :params jobs: the job numbers to delete (required)
        :type jobs: str/list
        :returns: generic success message
        :rtype: str
        """
        return self._xmlrpc_query('delete', user=user, jobs=jobs)

    def edit(self, *, user, job, enabled=True, **kwargs):
        """ Edit a cronjob on a user's crontab.

        :params user: the user's crontab you're editing (required)
        :type user: str
        :params job: the job number of the cronjob you're editing (required)
        :type job: str
        :params enabled: whether to enable the job or not [True/False]
        :type enabled: bool
        :params minute: cron formatted minute to run on
        :type minute: str/list
        :params hour: cron formatted hour to run on
        :type hour: str/list
        :params day: cron formatted day to run on
        :type day: str/list
        :params month: cron formatted month to run on
        :type month: str/list
        :params dayofweek: cron formatted day of the week to run on
        :type dayofweek: str/list
        :params script: the command to run
        :type script: str
        :returns: generic success message
        :rtype: str
        """
        return self._xmlrpc_query('edit', user=user, job=job, enabled=self.falsey(enabled), **kwargs)
    
    def get_current_system_time(self):
        """ Get current system time in RFC822 format.

        :returns: current time in RFC822 format
        :rtype: str
        """
        return self._xmlrpc_query('getCurrentSystemTime')

    def options(self, *, user, **kwargs):
        """ Manage options for cron users.

        :param user: the user to manage options for (required)
        :type user: str
        :param shell: the shell to run the crontab on
        :type shell: str
        :param path: the directories that will be in the search path for cron
        :type path: str/list
        :param mailto: the email address that should receive the output of each cronjob
        :type mailto: str
        :returns: generic success message
        :rtype: str
        """
        return self._xmlrpc_query('options', user=user, **kwargs)

    def query_edit(self, *, user, job):
        """ Displays the information available to the action "edit".

        :param user: the user's crontab you are query-editing (required)
        :type user: str
        :param job: the linenumber of the cronjob you wish to query-edit (required)
        :type job: int
        :returns: a dictionary of editable fields for the cronjob
        :rtype: dict
        """
        return self._xmlrpc_query('queryEdit', user=user, job=job)

    def query_jobs(self, *, user):
        """ List user jobs.

        :param user: the user's crontab you want to list jobs for (required)
        :type user: str
        :returns: a list of dictionaries for each cronjob
        :rtype: list
        """
        return self._xmlrpc_query('queryJobs', user=user)
    
    def query_options(self, *, user):
        """ Displays the information available to the action 'options'.

        :param user: the user's crontab you want to query options for (required)
        :type user: str
        :returns: a dictionary containing editable fields for the crontab options
        :rtype: dict
        """
        return self._xmlrpc_query('queryOptions', user=user)


class SiteWorxCron(Controller):
    def __init__(self, server):
        super().__init__(server)
        self.controller = '/siteworx/cron'

    def add(self, *, wd, script, **kwargs):
        """ Add a new cronjob to the user's crontab.

        Args:
            wd (str): (required) the working directory for the account
            script (str): (required) the script to run
            minute (str/list): cron formatted minute to run on
            hour (str/list): cron formatted hour to run on
            day (str/list): cron formatted day to run on
            month (str/list): cron formatted month to run on
            dayofweek (str/list): cron formatted month to run on
        
        Returns:
            str: generic success message
        """
        return self._xmlrpc_query('add', wd=wd, script=script, **kwargs)

    def delete(self, *, wd, jobs):
        """ Delete cronjob from the SiteWorx user's crontab.

        Args:
            wd (str): (required) the working directory for the account
            jobs (int/list): (required) the linenumber of the cron to delete

        Returns:
            str: generic success message
        """
        return self._xmlrpc_query('delete', wd=wd, jobs=jobs)

    def edit(self, *, wd, job, **kwargs):
        """ Edit a cronjob on a user's crontab.

        Args:
            wd (str): (required) the working directory for the account
            job (str): (required) the job number of the cronjob you're editing
            enabled (int): (0/1) whether to enable the job or not
            minute (str/list): cron formatted minute to run on
            hour (str/list): cron formatted hour to run on
            day (str/list): cron formatted day to run on
            month (str/list): cron formatted month to run on
            dayofweek (str/list): cron formatted month to run on
            script (str): the command to run
        
        Returns: 
            str: generic success message
        """
        return self._xmlrpc_query('edit', wd=wd, job=job, **kwargs)
    
    def get_current_system_time(self, *, wd):
        """ Get current system time in RFC822 format.

        Args:
            wd (str): (required) the working directory for the account

        Returns:
            str: current time in RFC822 format.
        """
        return self._xmlrpc_query('getCurrentSystemTime', wd=wd)

    def options(self, *, wd, user, **kwargs):
        """ Manage options for cron users.

        Args:
            wd (str): (required) the working directory for the account
            user (str): (required) the user to manage options for
            shell (str): the shell to run the crontab on
            path (str/list): the directories that will be in the search path for cron
            mailto (str): the email address that should receive the output of each cronjob
        
        Returns:
            str: generic success message
        """
        return self._xmlrpc_query('options', wd=wd, user=user, **kwargs)
    
    def query_edit(self, *, wd, job):
        """ Displays the information available to the action "edit".

        Args:
            wd (str): (required) the working directory for the account
            job (int): (required) the linenumber/job number of the cronjob to edit

        Returns:
            dict: a dictionary of editable fields for the job
        """
        parsed_jobs = []
        return self._xmlrpc_query('queryEdit', wd=wd, job=job)

    def query_jobs(self, *, wd):
        """ List user jobs.

        Args:
            wd (str): (required) the working directory for the account

        Returns:
            list: a list of dictionaries containing job information
        """
        return self._xmlrpc_query('queryJobs', wd=wd)

    def query_options(self, wd):
        """ Display the information available to the action "options".

        Args:
            wd (str): (required) the working directory for the account

        Returns:
            list: a list of dictionaries containing option information
        """
        return self._xmlrpc_query('queryOptions', wd=wd)