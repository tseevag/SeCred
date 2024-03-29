import getpass

import config
from data import User
from modules import menu
from modules.auth import signup
from modules.crypto import crypto_hash
from modules.db import find_user

def verify_credential(input_uname, input_passwd):
    """Return:
     if credentials are valid, True
     else False
    """
    user = find_user.get_user(input_uname)

    if(user == None):               #time based attack prevention 
        user = find_user.get_dummy_user()

    salt = bytes.fromhex(user[-2])
    passwd_hash = user[-1]

    _, hashed_input_passwd = crypto_hash.gen_hash(input_passwd, salt)  

    hashed_input_passwd = hashed_input_passwd.hex()

    if(passwd_hash.lower() == hashed_input_passwd.lower()):
        return True

    else:
        return False


def login():
    """
    Return a User obect if login successfull else return 'None'
    """
    menu.display_title("Login")

    remaining_attempts = config.ALLOWED_LOGIN_ATTEMPTS

    while (remaining_attempts > 0):
        uname = input("Username:")
        passwd = getpass.getpass()

        if verify_credential(uname, passwd):
            return User.User(1, uname)

        else:
            print("\nInvalid username or password !")
            remaining_attempts -= 1
            print(str(remaining_attempts) + ' attempts remaing')
        
    else:
        return None