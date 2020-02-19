class NodeWorxUser:
    def __init__(self, info):
        self.global_uid = info.get('global_uid')
        self.email = info.get('email')
        self.nickname = info.get('nickname')
        self.language = info.get('language')
        self.user_status = info.get('user_status')
        self.type = info.get('type')

    def __str__(self):
        return self.email

    def __repr__(self):
        return self.email


class SiteWorxUser:
    def __init__(self, info):
        self.global_uid = info.get('global_uid')
        self.email = info.get('email')
        self.nickname = info.get('nickname')
        self.language = info.get('language')
        self.user_status = info.get('user_status')
        self.type = info.get('type')
        self.ssh_enabled = info.get('ssh_enabled')
        self.ssh_username = info.get('ssh_username')

    def __str__(self):
        return self.email

    def __repr__(self):
        return self.email
