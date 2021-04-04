import getpass

import config
from data.User import User
from modules import menu
from modules.auth import signup

def verify_credential(uname_input, passwd_input):
    uname = config.user_name
    passwd = config.password

    #database implementation is remaining
    if (uname == uname_input) and (passwd == passwd_input):
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

        is_cred_valid = verify_credential(uname, passwd)

        if is_cred_valid:
            return User(1, uname)

        else:
            print("\nInvalid username or password !")
            remaining_attempts -= 1
            print(str(remaining_attempts) + ' attempts remaing')
        
    else:
        return None