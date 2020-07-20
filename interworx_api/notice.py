from .controller import Controller


class Notice(Controller):
    def __init__(self, server):
        super().__init__(server)
        self.controller = "/nodeworx/notice"

    def dismiss_banner(self, *, delivery_id=None):
        if delivery_id is None:
            return self._xmlrpc_query('dismissBanner')
        return self._xmlrpc_query('dismissBanner', delivery_id=delivery_id)

    def ignore_until(self, *, delivery_id, ignore_until):
        return self._xmlrpc_query('ignoreUntil', delivery_id=delivery_id, ignore_until=ignore_until)

    def list_banner_notices(self):
        return self._xmlrpc_query('listBannerNotices')

    def remove_unsubscription(self, *, code):
        return self._xmlrpc_query('removeUnsubscription', code=code)

    def unsubscribe(self, *, code):
        return self._xmlrpc_query('unsubscribe', code=code)

    def unsubscribe_all(self):
        return self._xmlrpc_query('unsubscribeAll')