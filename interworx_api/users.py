from .controller import Controller

class Users(Controller):
    def __init__(self, server):
        super().__init__(server)
    
    def _build_user_list(self, response, classname):
        users = []
        for user in response:
            users.append(classname(user))
        return users

    def _build_email_list(self, response):
        users = []
        for user in response:
            users.append(user[0])
        return users

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
        response = self._api_request('listDeletable', wd=wd)
        return self._build_email_list(response)

    def list_editable(self, wd=None):
        response = self._api_request('listEditable', wd=wd)
        return self._build_email_list(response)

    def list_users(self, classname, wd=None):
        response = self._api_request('listUsers', wd=wd)
        return self._build_user_list(response, classname)

    def list_working_user(self, classname, wd=None):
        response = self._api_request('listWorkingUser', wd=wd)
        return classname(response)

    def query_edit(self, wd=None, **attributes):
        return self._api_request('queryEdit', wd=wd, **attributes)


class NodeWorxUsers(Users):
    def __init__(self, server):
        super().__init__(server)
        self.controller = '/nodeworx/users'

    def add(self, **attributes):
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
        return NodeWorxUser(self._api_request('listMasterUser'))

    def list_users(self):
        return super().list_users(NodeWorxUser)

    def list_working_user(self):
        return super().list_working_user(NodeWorxUser)

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
        return super().list_users(SiteWorxUser, wd=wd)

    def list_working_user(self, wd):
        return super().list_working_user(SiteWorxUser, wd=wd)


class User:
    def __init__(self, info):
        self.global_uid = info.get('global_uid', None)
        self.email = info.get('email', None)
        self.nickname = info.get('nickname', None)
        self.language = info.get('language', None)
        self.user_status = info.get('user_status', None)
        self.type = info.get('type', None)

    def __str__(self):
        return self.email

    def __repr__(self):
        return self.email


class NodeWorxUser(User):
    pass


class SiteWorxUser(User):
    def __init__(self, info):
        super().__init__(info)
        self.ssh_enabled = info.get('ssh_enabled', None)
        self.ssh_username = info.get('ssh_username', None)
