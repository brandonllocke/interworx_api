from .controller import Controller


class IPv6(Controller):
    def __init__(self, server):
        super().__init__(server)
        self.controller = "/nodeworx/ipv6"
    
    def add_pool(self, *, ipv6_with_cidr, subpool_size, device, gateway,
                 **kwargs):
        return self._xmlrpc_query('addPool', ipv6_with_cidr=ipv6_with_cidr,
                                  subpool_size=subpool_size,
                                  device=device, gateway=gateway, **kwargs)
    
    def add_reservation(self, *, range_start, range_end, **kwargs):
        return self._xmlrpc_query('addReservation', range_start=range_start,
                                  range_end=range_end, **kwargs)

    def delete_pool(self, *, pool):
        return self._xmlrpc_query('deletePool', pool=pool)

    def delete_reservation(self, *, id):
        return self._xmlrpc_query('deleteReservation', id=id)

    def edit_pool(self, *, pool, **kwargs):
        return self._xmlrpc_query('editPool', pool=pool, **kwargs)

    def edit_reservation(self, *, id=id, **kwargs):
        return self._xmlrpc_query('editReservation', id=id, **kwargs)

    def list_pools(self):
        return self._xmlrpc_query('listPools')

    def list_reserved(self):
        return self._xmlrpc_query('listReserved')

    def query_edit_pool(self, *, pool):
        return self._xmlrpc_query('queryEditPool', pool=pool)

    def query_edit_reservation(self):
        return self._xmlrpc_query('queryEditReservation')