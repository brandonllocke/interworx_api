from .controller import Controller


class NodeWorxBackups(Controller):
    def __init__(self, server):
        super().__init__(server)
        self.controller = '/nodeworx/backup'

    def fullbackup(self, *, domains, **kwargs):
        """ Creates a full backup for the specified domains.

        Args:
            domains (str/list): (required) domain to backup
            email (str): where to send notification when backup has
                completed.
        
        Returns:
            str: generic success message
        """
        return self._xmlrpc_query('fullbackup', domains=domains, **kwargs)

    def query_accounts(self, *, reseller):
        """ Query the backups based on the selected reseller.

        Args:
            reseller (str): reseller id (all, 1, 16, etc.)

        Returns:
            list: a list of dictionaries containing information regarding
                backups for accounts under that reseller
        """
        return self._xmlrpc_query('queryAccounts', reseller=reseller)

    def query_backups(self, *, domain):
        """ Get a list of backups given a domain.

        Args:
            domain (str): the domain to query backups for

        Returns:
            list: a list of dictionaries with info about all backups for
                domain
        """
        return self._xmlrpc_query('queryBackups', domain=domain)

    def restore(self, *, domain, file, **kwargs):
        """ Restore a given backup (local).

        Args:
            domain (str): (required) the domain that will be restored
            file (str): (required) the path to the file
            confirm_action (int): (1) confirms the action should occur

        Returns:
            str: generic success message
        """
        return self._xmlrpc_query('restore', domain=domain, file=file, **kwargs)

    def structureonly(self, *, domains, **kwargs):
        """ Creates a structure only backup for the specified domains.

        Args:
            domains (str/list): the domain to make the backup for
            email (str): where to send notification when backup is completed

        Returns:
            str: generic success message
        """
        return self._xmlrpc_query('structureonly', domains=domains, **kwargs)


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