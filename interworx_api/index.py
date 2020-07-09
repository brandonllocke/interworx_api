from .controller import Controller


class Index(Controller):
    def __init__(self, server):
        super().__init__(server)
        self.controller = "/nodeworx/index"

    def get_session(self):
        """ Gets the session id

        :returns: session id
        :rtype: str
        """
        return self._xmlrpc_query('getSession')

    def get_websetup_status(self):
        """ Get web setup status

        :returns: the status and log for web setup
        :rtype: dictionary
        """
        return self._xmlrpc_query('getWebsetupStatus')