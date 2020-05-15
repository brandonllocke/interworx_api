from .controller import Controller


class NodeWorxCron(Controller):
    def __init__(self, server):
        super().__init__(server)
        self.controller = '/nodeworx/cron'

    def add(self, *, interface, user, script, **kwargs):
        """ Add a job to a user's crontab.

        Args:
            interface (str): (simple/advanced) (required) the type of menu to
                present (useless in cli)
            user (str): (required) the user's crontab to add to
            script (str): (required) the script to be run
            minute (str/list): cron formatted minute to run on
            hour (str/list): cron formatted hour to run on
            day (str/list): cron formatted day to run on
            month (str/list): cron formatted month to run on
            dayofweek (str/list): cron formatted month to run on

        Returns:
            str: generic success message
        """
        return self._xmlrpc_query('add', interface=interface, user=user, script=script,  **kwargs)

    def delete(self, *, user, jobs):
        """ Delete a job(s) from a user's crontab.

        Args:
            user (str): (required) the user's crontab to delete from
            jobs (str/list): (required) the job numbers to delete
        
        Returns:
            str: generic success message
        """
        return self._xmlrpc_query('delete', user=user, jobs=jobs)

    def edit(self, *, user, job, **kwargs):
        """ Edit a cronjob on a user's crontab.

        Args:
            user (str): (required) the user's crontab you're editing
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
        return self._xmlrpc_query('edit', user=user, job=job, **kwargs)
    
    def get_current_system_time(self):
        """ Get current system time in RFC822 format.

        Args:
            None

        Returns:
            str: current time in RFC822 format.
        """
        return self._xmlrpc_query('getCurrentSystemTime')

    def options(self, *, user, **kwargs):
        """ Manage options for cron users.

        Args:
            user (str): (required) the user to manage options for
            shell (str): the shell to run the crontab on
            path (str/list): the directories that will be in the search path for cron
            mailto (str): the email address that should receive the output of each cronjob
        
        Returns:
            str: generic success message
        """
        return self._xmlrpc_query('options', user=user, **kwargs)

    def query_edit(self, *, user, job):
        """ Displays the information available to the action "edit".

        Args:
            user (str): (required) the user's crontab you are query editing
            job (int): (required) the linenumber of the cronjob you wish to query edit
        
        Returns:
            dict: a dictionary of editable fields for the cronjob
        """
        return self._xmlrpc_query('queryEdit', user=user, job=job)

    def query_jobs(self, *, user):
        """ List user jobs.

        Args:
            user (str): (required) the user's crontab you want to list jobs for
        
        Returns:
            list: a list of dictionaries for each cronjob
        """
        return self._xmlrpc_query('queryJobs', user=user)
    
    def query_options(self, *, user):
        """ Displays the information available to the action 'options'.

        Args:
            user (str): (required) the user's crontab you want to query options for
        
        Returns:
            dict: a dictionary containing editable fields for the crontab options
        """
        return self._xmlrpc_query('queryOptions', user=user)


class SiteWorxCron(Cron):
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