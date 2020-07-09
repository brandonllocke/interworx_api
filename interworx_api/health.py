from .controller import Controller


class Health(Controller):
    def __init__(self, server):
        super().__init__(server)
        self.controller = "/nodeworx/health"

    def edit(self, *, code, repeat_rate="60", run_time="hourly"):
        """ Edit problem settings - action has conditional inputs not documented

        :param code: the error code to edit settings for
        :type code: str
        :param repeat_rate: controls how often notices are sent for the conditions checked [once/0/30/60/1440/10080] (default: 60)
        :type repeat_rate: str
        :param run_time: controls how often the detector is run [fively/fifteenly/hourly/quad_daily/daily/weekly/monthly] (default: hourly)
        :type run_time: str
        :returns: generic success message
        :rtype: str
        """
        return self._xmlrpc_query(
            "edit", code=code, repeat_rate=repeat_rate, run_time=run_time
        )

    def edit_recipients(self, *, code, **kwargs):
        """ Change the recipients of a code

        :param code: the error code to change the recipient for
        :type code: str
        :param email_recipients: the account to send notice to
        :type email_recipients: str/list
        :param banner_recipients: the accounts to display a banner error on
        :type banner_recipients: str/list
        :param email_only: direct email addresses to sent to
        :type email_only: str/list
        :returns: generic success message
        :rtype: str
        """
        return self._xmlrpc_query("editRecipients", code=code, **kwargs)

    def query_code_history(self, *, code):
        """ Get the code history for a specific code

        :param code: the code to get history for
        :type code: str
        :returns: list of dictionaries containing historical data
        :rtype: list
        """
        return self._xmlrpc_query("queryCodeHistory", code=code)

    def query_code_by_email(self, *, email):
        """ List codes the a given email address may recieve

        :param email: the email to scan for
        :type email: str
        :returns: list of dictionaries containing information about codes this email should receive information for
        :rtype: list
        """
        return self._xmlrpc_query("queryCodesByEmail", email=email)

    def query_edit(self):
        """ Displays the information available to the action "edit"

        :returns: dictionary containing information available for edit
        :rtype: dict
        """
        return self._xmlrpc_query("queryEdit")

    def query_edit_recipients(self, *, code):
        """ Displays the information avaliable to the action "edit_recipients"

        :param code: the code to check editable fields for
        :type code: str
        :returns: dictionary of lists for email recipients, banner_recipients, email_only
        :rtype: dict
        """
        return self._xmlrpc_query("queryEditRecipients")

    def query_health_status(self):
        """ Lists real-time status of detectors (actually runs each, be careful about load)

        :returns: list of dictionaries containing information for each detector
        :rtype: list
        """
        return self._xmlrpc_query("queryHealthStatus")

    def remove_target_from_code(self, *, code, target):
        """ Removes a specific target from a code. User query_codes_by_email to see targets

        :param code: the code to remove the target from
        :type code: str
        :param target: the target to remove
        :type target: str
        :returns: generic success message
        :rtype: str
        """
        return self._xmlrpc_query("removeTargetFromCode", code=code, target=target)

