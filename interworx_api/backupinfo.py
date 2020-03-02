class BackupInfo:
    def __init__(self, info):
        self.filepath = info.get('filepath')
        self.filename = info.get('filename')
        self.filesize = info.get('filesize')
        self.filesize_bytes = info.get('filesize_bytes')
        self.type = info.get('type')
        self.domain_options = info.get('domain_options')
        self.filedate = info.get('filedate')
        self.complete = info.get('complete')
        self.domain = info.get('domain', '')

    def __str__(self):
        return self.filename

    def __repr__(self):
        return self.filename
