class Users():
    def __init__(self, server, ctrl_prefix, ctrl_suffix='/users'):
        self.server = server
        self.url = server.url
        self.key = server.key
        self.ctrl_prefix = ctrl_prefix
        self.ctrl_suffix = ctrl_suffix
        self.ctrlr = ctrl_prefix + ctrl_suffix

    def _modify_key(self, working_domain):
        if self.ctrl_prefix == '/siteworx':
            key = {'apikey': self.key, 'domain': working_domain}
        else:
            key = self.key
        return key

    def activate(self, working_domain='', **attributes):
        key = self._modify_key(working_domain)
        response = self.server.get(key, self.ctrlr, 'activate', attributes)
        print(response['payload'])

    def add(self, working_domain='', **attributes):
        key = self._modify_key(working_domain)
        response = self.server.get(key, self.ctrlr, 'add', attributes)
        print(response['payload'])

    def deactivate(self, working_domain='', **attributes):
        key = self._modify_key(working_domain)
        response = self.server.get(key, self.ctrlr, 'deactivate', attributes)
        print(response['payload'])

    def delete(self, working_domain='', **attributes):
        key = self._modify_key(working_domain)
        response = self.server.get(key, self.ctrlr, 'delete', attributes)
        print(response['payload'])

    def edit(self, working_domain=None, **attributes):
        key = self._modify_key(working_domain)
        response = self.server.get(key, self.ctrlr, 'edit', attributes)
        print(response['payload'])

    def is_reseller(self, working_domain=''):
        if self.ctrl_prefix == '/siteworx':
            print('This method is only for NodeWorx users.')
        else:
            key = self._modify_key(working_domain)
            response = self.server.get(key, self.ctrlr, 'isReseller')
            print(response['payload'])

    def list_deletable(self, working_domain=''):
        key = self._modify_key(working_domain)
        response = self.server.get(key, self.ctrlr, 'listDeletable')
        for user in response['payload']:
            print(user)

    def list_editable(self, working_domain=''):
        key = self._modify_key(working_domain)
        response = self.server.get(key, self.ctrlr, 'listEditable')
        for user in response['payload']:
            print(user)

    def list_master_user(self, working_domain=''):
        if self.ctrl_prefix == '/siteworx':
            print('This method is only for NodeWorx users.')
        else:
            key = self._modify_key(working_domain)
            response = self.server.get(key, self.ctrlr, 'listMasterUser')
            print(response['payload'])

    def list_users(self, working_domain=''):
        key = self._modify_key(working_domain)
        response = self.server.get(key, self.ctrlr, 'listUsers')
        for user in response['payload']:
            print(user)

    def list_working_user(self, working_domain=''):
        key = self._modify_key(working_domain)
        response = self.server.get(key, self.ctrlr, 'listWorkingUser')
        print(response['payload'])
