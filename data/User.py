class User:
    """Logged in user"""
    def __init__(self, uid, uname):
        self._uid = uid
        self._uname = uname
    
    def get_uid(self):
        return self._uid

    def get_uname(self):
        return self._uname

    def update_uname(self, uname):
        self._uname = uname