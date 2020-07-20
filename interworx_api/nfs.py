from .controller import Controller


class Nfs(Controller):
    def __init__(self, server):
        super().__init__(server)
        self.controller = "/nodeworx/nfs"
        self.export = Export(server)
        self.mount = Mount(server)

    def is_running(self):
        return self._xmlrpc_query('isRunning')

    def is_running_on_node(self, *, node_id='1'):
        return self._xmlrpc_query('isRunningOnNode', node_id=node_id)

    def list_general_name(self):
        return self._xmlrpc_query('listGeneralName')

    def list_port_numbers(self):
        return self._xmlrpc_query('listPortNumbers')

    def list_port_numbers_array(self):
        return self._xmlrpc_query('listPortNumbersArray')

    def list_required_permissions(self):
        return self._xmlrpc_query('listRequiredPermissions')

    def list_service_info(self):
        return self._xmlrpc_query('listServiceInfo')

    def list_service_name(self):
        return self._xmlrpc_query('listServiceName')

    def list_service_page(self):
        return self._xmlrpc_query('listServicePage')

    def restart(self):
        return self._xmlrpc_query('restart')

    def restart_on_node(self, *, node_id='1'):
        return self._xmlrpc_query('restartOnNode', node_id=node_id)

    def start(self):
        return self._xmlrpc_query('start')

    def start_on_boot(self, *, nfs_startonboot=False):
        return self._xmlrpc_query('startOnBoot', nfs_startonboot=self.falsey(nfs_startonboot))

    def start_on_node(self, *, node_id='1'):
        return self._xmlrpc_query('startOnNode', node_id=node_id)

    def stop(self):
        return self._xmlrpc_query('stop')

    def stop_on_node(self, *, node_id='1'):
        return self._xmlrpc_query('stopOnNode', node_id=node_id)

class Export(Controller):
    def __init__(self, server):
        super().__init__(server)
        self.controller = "/nodeworx/nfs/export"

    def add(self, *, directory_to_export, read_write_access, root_user_access, sync_options, **kwargs):
        if read_write_access not in ['ro', 'rw']:
            raise ValueError("ro/rw are the only allowed values for read_write_access")
        if root_user_access not in ['root_squash', 'no_root_squash']:
            raise ValueError("root_squash/no_root_squash are the only allowed values for root_user_access")
        if sync_options not in ['async', 'sync']:
            raise ValueError("async/sync are the only allowed values for sync_options")
        return self._xmlrpc_query('add', directory_to_export=directory_to_export,
                                   read_write_access=read_write_access,
                                   root_user_access=root_user_access,
                                   sync_options=sync_options, **kwargs)

    def list_nfs_exports(self):
        return self._xmlrpc_query('listNfsExports')

class Mount(Controller):
    def __init__(self, server):
        super().__init__(server)
        self.controller = "/nodeworx/nfs/mount"

    def add(self, *, host, remote_directory, mount_point, **kwargs):
        return self._xmlrpc_query('add', host=host, remote_directory=remote_directory,
                                  mount_point=mount_point, **kwargs)

    def list_nfs_mounts(self):
        return self._xmlrpc_query('listNfsMounts')

    