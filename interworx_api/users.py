from .user import NodeWorxUser
from .user import SiteWorxUser

class Users:
    def __init__(self, server):
        self.server = server
        self.key = server.key

    def _modify_key(self, working_domain=None):
        if working_domain is not None:
            key = {'apikey': self.key, 'domain': working_domain}
            return key
        return self.key

    def _query_xmlrpc(

    def activate(self, working_domain=None, **attributes):
        key = self._modify_key(working_domain)
        response = self.server.get(key, self.controller, 'activate', attributes)
        print(response['payload'])

    def add(self, working_domain=None, **attributes):
        key = self._modify_key(working_domain)
        response = self.server.get(key, self.controller, 'add', attributes)
        print(response['payload'])

    def deactivate(self, working_domain=None, **attributes):
        key = self._modify_key(working_domain)
        response = self.server.get(key, self.controller, 'deactivate', attributes)
        print(response['payload'])

    def delete(self, working_domain=None, **attributes):
        key = self._modify_key(working_domain)
        response = self.server.get(key, self.controller, 'delete', attributes)
        print(response['payload'])

    def edit(self, working_domain=None, **attributes):
        key = self._modify_key(working_domain)
        response = self.server.get(key, self.controller, 'edit', attributes)
        print(response['payload'])

    def list_deletable(self, working_domain=None):
        key = self._modify_key(working_domain)
        response = self.server.get(key, self.controller, 'listDeletable')
        for user in response['payload']:
            print(user)

    def list_editable(self, working_domain=None):
        key = self._modify_key(working_domain)
        response = self.server.get(key, self.controller, 'listEditable')
        for user in response['payload']:
            print(user)

    def list_users(self, classname, working_domain=None):
        users = []
        key = self._modify_key(working_domain)
        response = self.server.get(key, self.controller, 'listUsers')
        for user in response:
            users.append(classname(user))
        return users

    def list_working_user(self, classname, working_domain=None):
        key = self._modify_key(working_domain)
        response = self.server.get(key, self.controller, 'listWorkingUser')
        return classname(response)

class NodeWorxUsers(Users):
    def __init__(self, server):
        super().__init__(server)
        self.controller = '/nodeworx/users'

    def is_reseller(self):
        response = self.server.get(self.key, self.controller, 'isReseller')
        return response

    def list_users(self):
        response = super().list_users(NodeWorxUser)
        return response

    def list_working_user(self):
        response = super().list_working_user(NodeWorxUser)
        return response

class SiteWorxUsers(Users):
    def __init__(self, server):
        super().__init__(server)
        self.controller = '/siteworx/users'

    def list_users(self, working_domain):
        response = super().list_users(SiteWorxUser, working_domain)
        return response

    def list_working_user(self, working_domain):
        response = super().list_working_user(SiteWorxUser, working_domain)
        return response
