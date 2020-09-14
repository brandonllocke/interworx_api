import ssl
import sys
import xmlrpc.client

class Iworx():
    def __init__(self, server_url, key):
        self.url = server_url
        self.key = key
        context = ssl.SSLContext()
        self.server = xmlrpc.client.ServerProxy(f'https://{self.url}:2443/xmlrpc', context=context)

    def _xmlrpc_request(self, key, path, cmd, params=None):
        params = params or {}
        response = self.server.iworx.route(
            key, path, cmd, params)
        try:
            if response['status'] == 0:
                return response['payload']
            else:
                raise ValidationError(response['status'], response['payload'])
        except ValidationError as e:
            sys.exit(e)

    def _modify_key(self, siteworx_domain=None):
        if siteworx_domain is not None:
            return {"apikey": self.key, "domain": siteworx_domain}
        return self.key

    def request(self, controller, action, siteworx_domain=None, **kwargs):
        key = self._modify_key(siteworx_domain)
        return self._xmlrpc_request(key, controller, action, kwargs)


class ValidationError(Exception):
    def __init__(self, status, payload):
        super().__init__(payload)
        self.status = status
        self.payload = payload

    def __str__(self):
        return f'''Server responded with an exit code of: {self.status}.
The server's response was: {self.payload}.'''            