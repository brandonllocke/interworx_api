from .controller import Controller


class NodeWorxBackups(Controller):
    def __init__(self, server):
        super().__init__(server)
        self.controller = '/nodeworx/backup'

    def fullbackup(self, *, domains, email=None):
        """ Creates a full backup for the specified domains.

        :param domains: the domain to backup (required)
        :type domains: str/list
        :param email: where to send notification when backup has completed
        :type email: str
        :returns: generic success message
        :rtype: str
        """
        if email is None:
            return self._xmlrpc_query('fullbackup', domains=domains)
        return self._xmlrpc_query('fullbackup', domains=domains, email=email)

    def query_accounts(self, *, reseller):
        """ Query the backups based on the selected reseller.

        :param reseller: the reseller id as a string
        :type reseller: str
        :returns: a list of dictionaries containing information regarding
            backups for accounts under that reseller
        :rtype: list
        """
        return self._xmlrpc_query('queryAccounts', reseller=reseller)

    def query_backups(self, *, domain):
        """ Get a list of backups given a domain.

        :param domain: the domain to query backups for
        :type domain: str
        :returns: a list of dictionaries with info about all backups for
            domain
        :rtype: list
        """
        return self._xmlrpc_query('queryBackups', domain=domain)

    def restore(self, *, domain, file):
        """ Restore a given backup (local).

        :param domain: the domain that will be restored (required)
        :type domain: str
        :param file: the path to the file (required)
        :type file: str
        :returns: generic success message
        :rtype: str
        """
        return self._xmlrpc_query('restore', domain=domain, file=file, confirm_action=1)

    def structureonly(self, *, domains, email=None):
        """ Creates a structure only backup for the specified domains.

        :param domains: the domain to make the backup for (required)
        :type domains: str/list
        :param email: where to send notification when backup is completed
        :type email: str
        :returns: generic success message
        :rtype: str
        """
        if email is None:
            return self._xmlrpc_query('structureonly', domains=domains)
        return self._xmlrpc_query('structureonly', domains=domains, email=email)


class SiteWorxBackups(Controller):
    def __init__(self, server):
        super().__init__(server)
        self.controller = '/siteworx/backup'

    def create(self, *, wd, type, location, **kwargs):
        """ Create a SiteWorx backup.

        Args:
            wd (str): (required) the domain to create the backup for
            type (str): (required) (full, partial, structure) the type of
                backup to create
            location (str): (required) (siteworx, local, ftp, scp) the final
                location of the backup
            email_address (str): where to send notification when backup is
                complete
            domain_options (str): (single-domain, multi-domain)
            exclude_extensions (str/list): which extensions to ignore when
                building the backup

        Returns:
           str: generic success message
        """
        return self._xmlrpc_query('create', wd=wd, type=type, location=location, **kwargs)

    def delete(self, *, wd, backups):
        """ Delete a siteworx backup.

        Args:
            wd (str): (required) the domain to create the backup for
            backups (str/list): (required) the path to files to delete
        
        Returns:
            str: generic success message
        """
        return self._xmlrpc_query('delete', wd=wd, backups=backups)

    def list_all_backups(self, *, wd):
        """ List all backups created manually.

        Args:
            wd (str): (required) the domain to create the backup for

        Returns:
            list: list of dictionaries containing backup information
        """
        return self._xmlrpc_query('listAllBackups', wd=wd)

    def list_daily_backups(self, *, wd):
        """ List all current daily backups.

        Args:
            wd (str): (required) the domain to create the backup for

        Returns:
            list: list of dictionaries containing backup information
        """
        return self._xmlrpc_query('listDailyBackups', wd=wd)

    def list_weekly_backups(self, *, wd):
        """ List all current weekly backups.

        Args:
            wd (str): (required) the domain to create the backup for

        Returns:
            list: list of dictionaries containing backup information
        """
        return self._xmlrpc_query('listWeeklyBackups', wd=wd)

    def list_monthly_backups(self, *, wd):
        """ List all current monthly backups.

        Args:
            wd (str): (required) the domain to create the backup for

        Returns:
            list: list of dictionaries containing backup information
        """
        return self._xmlrpc_query('listMonthlyBackups', wd=wd)

    def restore(self, *, wd, filetype, file):
        """ Restore a partial siteworx backup.

        Args:
            wd (str): (required) the domain to create the backup for
            filetype (str): (required) (local/remote)
            file (str): the path to the file to restore
        
        Returns:
            str: generic success message
        """
        return self._xmlrpc_query('restore', wd=wd, filetype=filetype, file=file)