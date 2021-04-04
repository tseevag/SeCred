class User:
    """Logged in user"""
    def __init__(self, uid, uname):
        self._uid = uid
        self._uname = uname
    
    def get_uid():
        return self._uid

    def get_uname():
        return self._uname

    def update_uname(uname):
        self._uname = uname