from .controller import Controller


class Help(Controller):
    def __init__(self, server):
        super().__init__(server)
        self.controller = "/nodeworx/help"

    def query_ssh(self):
        """ Displays the information available to the action "ssh"

        :returns: a dictionary of information available to action "ssh"
        :rtype: dict
        """
        return self._xmlrpc_query("querySsh")

    def ssh(self, *, mode=False, duration="72 hours"):
        """ Enabled or disable InterWorx Support SSH user

        :param mode: whether the ssh account is enabled (True) or disabled (False) (default: True)
        :type mode: bool
        :param duration: defines how long Remote assistance will be enabled before automatically disabling (default: 72 hours)
        :type duration: str
        :returns: generic success message
        :rtype: str
        """
        return self._xmlrpc_query("ssh", mode=self.falsey(mode), duration=duration)

