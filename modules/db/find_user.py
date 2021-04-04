import config

def get_user(uname):
    if uname == config.user['uname']:
        return config.user
    else:
        return None


def get_dummy_user():
    return {
        'uname': 'dummy_user',
        'salt': b'\xed\x82\x03\x01\xaaH\xdf\x83!\xc1\xe4\x10L\xc6-5\xb6lS\xf9\xaa\x8f\xa3\x05\xec\xcb[J\x87\xf09\xb1',
        'passwd': 'super-secret'
    }