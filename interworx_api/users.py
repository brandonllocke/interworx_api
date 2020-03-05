from .fields import Fields

class Users:
    def __init__(self, server):
        self.server = server
        self.key = server.key

    def _modify_key(self, working_domain=None):
        if working_domain is not None:
            key = {'apikey': self.key, 'domain': working_domain}
            return key
        return self.key

    def _xmlrpc_query(self, action, working_domain=None, **attributes):
        key = self._modify_key(working_domain)
        return self.server.get(key, self.controller, action, attributes)
    
    def _parse_fields(self, possible_fields, **attributes):
        fields = Fields(possible_fields, **attributes)
        reqs_met = fields.check_required_fields()
        validated = fields.validate_fields()
        if reqs_met and validated:
            return True
        return False

    def activate(self, working_domain=None, **attributes):
        possible_fields = {'required': {'user': list}}
        if self._parse_fields(possible_fields, **attributes):
            print(self._xmlrpc_query('activate', working_domain, **attributes))

    def add(self, working_domain=None, **attributes):
        return self._xmlrpc_query('add', working_domain, **attributes)

    def deactivate(self, working_domain=None, **attributes):
        return self._xmlrpc_query('deactivate', working_domain, **attributes)

    def delete(self, working_domain=None, **attributes):
        return self._xmlrpc_query('delete', working_domain, **attributes)

    def edit(self, working_domain=None, **attributes):
        return self._xmlrpc_query('edit', working_domain, **attributes)

    def list_deletable(self, working_domain=None):
        return self._xmlrpc_query('listDeletable', working_domain)

    def list_editable(self, working_domain=None):
        return self._xmlrpc_query('listEditable', working_domain)

    def list_users(self, classname, working_domain=None):
        users = []
        response = self._xmlrpc_query('listUsers', working_domain)
        for user in response:
            users.append(classname(user))
        return users

    def list_working_user(self, classname, working_domain=None):
        response = self._xmlrpc_query('listWorkingUser', working_domain)
        return classname(response)

    def query_edit(self, working_domain=None, **attributes):
        return self._xmlrpc_query('queryEdit', working_domain, **attributes)


class NodeWorxUsers(Users):
    def __init__(self, server):
        super().__init__(server)
        self.controller = '/nodeworx/users'

    def _build_user_list(self, response):
        users = []
        for user in response:
            users.append(NodeWorxUser({'email': user[0]}))
        return users

    def list_deletable(self):
        response = super().list_deletable()
        return self._build_user_list(response)

    def list_editable(self):
        response = super().list_editable()
        return self._build_user_list(response)

    def is_reseller(self):
        return self._xmlrpc_query('isReseller')

    def list_master_user(self):
        response = self._xmlrpc_query('listMasterUser')
        return NodeWorxUser(response)

    def list_users(self):
        return super().list_users(NodeWorxUser)

    def list_working_user(self):
        return super().list_working_user(NodeWorxUser)

class SiteWorxUsers(Users):
    def __init__(self, server):
        super().__init__(server)
        self.controller = '/siteworx/users'

    def _build_user_list(self, response):
        users = []
        for user in response:
            users.append(SiteWorxUser({'email': user}))
        return users

    def list_deletable(self, working_domain):
        response = super().list_deletable(working_domain)
        return self._build_user_list(response)

    def list_editable(self, working_domain):
        response = super().list_editable(working_domain)
        return self._build_user_list(response)

    def list_users(self, working_domain):
        return super().list_users(SiteWorxUser, working_domain)

    def list_working_user(self, working_domain):
        return super().list_working_user(SiteWorxUser, working_domain)


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
