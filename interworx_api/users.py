from .controller import Controller

class Users(Controller):
    def __init__(self, server):
        super().__init__(server)
    
    def add(self, fields=None, wd=None, **attributes):
        return self._api_request('add', fields=fields, wd=wd, **attributes)

    def activate(self, wd=None, **attributes):
        fields = {'required': {'user': list}}
        return self._api_request('activate', fields=fields, wd=wd, **attributes)

    def deactivate(self, wd=None, **attributes):
        fields = {
            'required': {
                'user': list
            },
        }
        return self._api_request('deactivate', fields=fields, wd=wd, **attributes)

    def delete(self, wd=None, **attributes):
        fields = {
            'required': {
                'user': list
            },
        }
        return self._api_request('delete', fields=fields, wd=wd, **attributes)

    def edit(self, fields=None, wd=None, **attributes):
        return self._api_request('edit', fields=fields, wd=wd, **attributes)

    def list_deletable(self, wd=None):
        return self._api_request('listDeletable', wd=wd)

    def list_editable(self, wd=None):
        return self._api_request('listEditable', wd=wd)

    def list_users(self, classname, wd=None):
        return self._api_request('listUsers', wd=wd)

    def list_working_user(self, wd=None):
        return self._api_request('listWorkingUser', wd=wd)

    def query_edit(self, wd=None):
        return self._api_request('queryEdit', wd=wd)


class NodeWorxUsers(Users):
    def __init__(self, server):
        super().__init__(server)
        self.controller = '/nodeworx/users'

    def add(self, **attributes):
        """Adds a NodeWorx User to the server.

        Args:
           nickname (str): the user's nickname
           email (str): the user's email address
           password(str): the user's password
           confirm_password (str): the user's password again
           language (str): the two letter representation for a language (en-us, de, es) (default is en-us)
           theme (str): name of the theme for the user (default is calliope)
           menu_style (str): the menu style for this user (default is big)
           encrypted (str): (y/n) whether the user's password is encrypted or not
           perms (str/list): what permissions a user should have (default is ["LOGIN"])

        Returns:
           str: NodeWorx user successfully added
        """
        fields = {
            'required': {
                'nickname': str, 
                'email': str,
                'password': str,
                'confirm_password': str
            },
            'optional': {
                'language': str,
                'theme': str,
                'menu_style': str,
                'encrypted': str,
                'perms': list
            }}
        return self._api_request('add', fields=fields, **attributes)

    def edit(self, **attributes):
        fields = {
            'required': {
                'user': str
            },
            'optional': {
                'nickname': str, 
                'email': str,
                'language': str,
                'theme': str,
                'menu_style': str,
                'encrypted': str,
                'password': str,
                'confirm_password': str
            }}
        return self._api_request('edit', fields=fields, **attributes)

    def list_deletable(self):
        return super().list_deletable()

    def list_editable(self):
        return super().list_editable()

    def is_reseller(self):
        return self._api_request('isReseller')

    def list_master_user(self):
        return self._api_request('listMasterUser')

    def list_users(self):
        return super().list_users()

    def list_working_user(self):
        return super().list_working_user()

class SiteWorxUsers(Users):
    def __init__(self, server):
        super().__init__(server)
        self.controller = '/siteworx/users'

    def add(self, wd, **attributes):
        fields = {
            'required': {
                'nickname': str, 
                'email': str,
                'password': str,
                'confirm_password': str
            },
            'optional': {
                'language': str,
                'theme': str,
                'menu_style': str,
                'encrypted': str,
                'perms': list,
                'locked_domains': str
            }}
        return super().add(fields=fields, wd=wd, **attributes)
    
    def edit(self, wd, **attributes):
        fields = {
            'required': {
                'user': str, 
            },
            'optional': {
                'language': str,
                'nickname': str, 
                'email': str,
                'password': str,
                'confirm_password': str,
                'theme': str,
                'menu_style': str,
                'encrypted': str,
            }}
        return super().edit(fields=fields, wd=wd, **attributes)

    def list_deletable(self, wd):
        return super().list_deletable(wd=wd)

    def list_editable(self, wd):
        return super().list_editable(wd=wd)

    def list_users(self, wd):
        return super().list_users(wd=wd)

    def list_working_user(self, wd):
        return super().list_working_user(wd=wd)