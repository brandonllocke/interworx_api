class AccountBackupInfo:
    def __init__(self, info):
        self.name = info.get('username')
        self.nickname = info.get('nickname')
        self.email = info.get('email')
        self.domain = info.get('domain')
        self.backup_count = info.get('backup_count')
        self.backup_dir_size = info.get('backup_dir_size')
        self.nodeworx_id = info.get('nodeworx_id')

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name
