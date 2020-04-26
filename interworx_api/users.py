from .controller import Controller


class NodeWorxUsers(Controller):
    def __init__(self, server):
        super().__init__(server)
        self.controller = "/nodeworx/users"

    def activate(self, *, user):
        """Activates a NodeWorx user.

        Args:
            user (str/list): username of the user to activate (required)

        Returns:
            str: NodeWorx User activated
        """
        return self._xmlrpc_query("activate", user=user)

    def add(self, *, nickname, email, password, confirm_password, **kwargs):
        """Adds a NodeWorx user.

        Args:
           nickname (str): the user's nickname (required)
           email (str): the user's email address (required)
           password(str): the user's password (required)
           confirm_password (str): the user's password again (required)
           language (str): the representation for a language (en-us, de, es)
               (default is en-us)
           theme (str): name of the theme for the user (default is calliope)
           menu_style (str): the menu style for this user (default is big)
           encrypted (str): (y/n) whether the user's password is encrypted or
               not (default: 'n')
           perms (str/list): what permissions a user should have (default is
               ["LOGIN"])

        Returns:
           str: NodeWorx user successfully added
        """

        return self._xmlrpc_query(
            "add",
            nickname=nickname,
            email=email,
            password=password,
            confirm_password=confirm_password,
            **kwargs
        )

    def deactivate(self, *, user):
        """Deactivates (but does not delete) a NodeWorx user.

        Args:
            user (str/list): username of the account to deactivate (required)

        Returns:
            str: NodeWorx user deactivated
        """
        return self._xmlrpc_query("deactivate", user=user)

    def delete(self, *, user):
        """Delete a NodeWorx user.

        Args:
            user (str/list): username of the account to delete
        
        Returns:
            str: NodeWorx user deleted
        """
        return self._xmlrpc_query("delete", user=user)

    def edit(self, *, user, **kwargs):
        """ Edit a NodeWorx user.

        Args:
            user (str):  the user's username (required)
            nickname (str): the user's nickname
            email (str): the user's email address
            language (str): language code (default: en-us)
            theme (str): the theme for the user
            menu_style (str): the menu style for the user
            encrypted (str): [y/n] whether the password is already encrypted
                (default: n)
            password (str): new password for the user
            confirm_password (str): new password for the user

        Returns:
            str: NodeWorx user successfully edited 
        """
        return self._xmlrpc_query("edit", user=user, **kwargs)

    def is_reseller(self):
        """Check if the current user is a reseller or not.

        Args:
            None

        Returns:
            bool: True for yes, False for no.
        """
        return self._xmlrpc_query("isReseller")

    def list_deletable(self):
        """List deleteable NodeWorx users.

        Args:
            None

        Returns:
            list: A list containing a dictionary for each deleteable users.
        """
        return self._xmlrpc_query("listDeletable")

    def list_editable(self):
        """List editable NodeWorx users.

        Args:
            None

        Returns:
            list: A list containing a dictionary for each editable users.
        """
        return self._xmlrpc_query("listEditable")

    def list_master_user(self):
        """Get details of the master user.

        Args:
            None

        Returns:
            dict: a dictionary containing information about master user.
        """
        return self._xmlrpc_query("listMasterUser")

    def list_users(self):
        """List NodeWorx users.

        Args:
            None

        Returns:
            list: A list containing a dictionary for each users.
        """
        return self._xmlrpc_query("listUsers")

    def list_working_user(self):
        """List NodeWorx working user.

        Args:
            None

        Returns:
            dict: a dictionary containing information about the working user.
        """
        return self._xmlrpc_query("listWorkingUser")

    def query_edit(self, *, user):
        """Displays the information available to the action "edit".

        Args:
            user (str): the username of the user

        Returns:
            dict: a dictionary of editable fields for the user
        """
        return self._xmlrpc_query("queryEdit", user=user)


class SiteWorxUsers(Controller):
    def __init__(self, server):
        super().__init__(server)
        self.controller = "/siteworx/users"

    def activate(self, *, wd=None, user):
        """Activates a SiteWorx user.

        Args:
            user (str/list): username of the user to activate (required)
            wd (str): working domain the user is part of (required)

        Returns:
            str: SiteWorx User activated
        """
        return self._xmlrpc_query("activate", wd=wd, user=user)

    def add(self, *, wd, nickname, email, password, confirm_password, **kwargs):
        """Adds a SiteWorx user.

        Args:
            wd (str): the working domain the user should be added to
                (required)
            nickname (str): the user's nickname (required)
            email (str): the user's email address (required)
            password(str): the user's password (required)
            confirm_password (str): the user's password again (required)
            language (str): the representation for a language (en-us, de, es)
                (default is en-us)
            menu_style (str): the menu style for this user (default is big)
            encrypted (str): (y/n) whether the user's password is encrypted
                or not (default 'n')
            perms (str/list): what permissions a user should have (default is
                ["LOGIN"])
            locked_domains (str): a comma separated list of domains a user
                should be able to manage (may additionally use the negation
                operator (!) and the wildcard (*).


        Returns:
           str: SiteWorx user successfully added
        """
        return self._xmlrpc_query(
            "add",
            wd=wd,
            nickname=nickname,
            email=email,
            password=password,
            confirm_password=confirm_password,
            **kwargs
        )

    def deactivate(self, *, wd=None, user):
        """Deactivates (but does not delete) a SiteWorx user.

        Args:
            user (str/list): username of the account to deactivate (required)
            wd (str): working domain the user is part of

        Returns:
            str: SiteWorx user deactivated
        """
        return self._xmlrpc_query("deactivate", wd=wd, user=user)

    def delete(self, *, wd=None, user):
        """Delete a SiteWorx user.

        Args:
            user (str/list): username of the account to delete
            wd (str): working domain the user is part of
        
        Returns:
            str: SiteWorx user deleted
        """
        return self._xmlrpc_query("delete", wd=wd, user=user)

    def edit(self, *, wd, user, **kwargs):
        """ Edits user in SiteWorx account.

        Args:
            wd (str): working domain for the siteworx account (required)
            user (str): username of the desired user (required)
            language (str): language code for setting user's interface
                language (default: en-us)
            nickname (str): the nickname of the user
            email (str): the email of the user
            password (str): the password of the user
            confirm_password (str): the password of the user again
            theme (str): the theme for the user's interface
            menu_style (str): the menu style for the user's interface
            encrypted (str): [y,n] whether the password is already encrypted
                or not

        Returns:
            str: SiteWorx user successfully edited
        """
        return self._xmlrpc_query("edit", wd=wd, **kwargs)

    def list_deletable(self, *, wd):
        """List deletable SiteWorx users.

        Args:
            wd (str): working domain for the siteworx account

        Returns:
            list: list of SiteWorx users that can be deleted
        """
        return self._xmlrpc_query("listDeletable", wd=wd)

    def list_editable(self, *, wd):
        """List editable SiteWorx users.

        Args:
            wd (str): working domain for the siteworx account (required)

        Returns:
            list: A list containing a dictionary for each editable user.
        """
        return self._xmlrpc_query("listEditable", wd=wd)

    def list_users(self, *, wd):
        """List SiteWorx users.

        Args:
            wd (str): working domain for the siteworx account (required)

        Returns:
            list: A list containing a dictionary for each users.
        """
        return self._xmlrpc_query("listUsers", wd=wd)

    def list_working_user(self, *, wd):
        """List SiteWorx working user.

        Args:
            wd (str): working domain for the siteworx account (required)

        Returns:
            dict: a dictionary containing information about the working user.
        """
        return self._xmlrpc_query("listWorkingUser", wd=wd)

    def query_edit(self, wd=None):
        """Displays the information available to the action "edit".

        Args:
            user (str): the username of the user
            wd (str): working domain for the siteworx account (required)

        Returns:
            dict: a dictionary of editable fields for the user
        """
        return self._xmlrpc_query("queryEdit", wd=wd)
