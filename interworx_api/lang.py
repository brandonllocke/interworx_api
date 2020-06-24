from .controller import Controller


class Lang(Controller):
    def __init__(self, server):
        super().__init__(server)
        self.controller = "/nodeworx/lang"

    def add(self, *, code, lang_file):
        return self._xmlrpc_query('add', code=code, lang_file=lang_file)

    def change_current_user_language(self):
        return self._xmlrpc_query('changeCurrentUserLanguage')
    
    def delete(self, *, code):
        return self._xmlrpc_query('delete', code=code)

    def list_languages(self):
        return self._xmlrpc_query('listLanguages')

    def query_change_current_user_language(self):
        return self._xmlrpc_query('queryChangeCurrentUserLanguage')

    def sync_language(self, *, code):
        return self._xmlrpc_query('syncLanguage', code=code)