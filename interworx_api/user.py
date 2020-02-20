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
