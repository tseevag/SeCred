import getpass
from getch import getch

import config
from data import User
from modules import menu
from modules.error import *
from modules.db import find_user
from modules.crypto import crypto_hash

def signup():
    """Returns:
     currently if sign up successfull
     else None
     """
    menu.display_title("sign up")

    try:
        first_name = input("First Name: ").split()[0]
        last_name = input("Last Name: ").split()[0]
        
        
        while True:
            uname = input("User Name: ")

            if find_user.get_user(uname):
                print("Username already taken ! Please choose another.")
                continue
            else:
                break

        
        while True:
            passwd = getpass.getpass()
            confirm_passwd = getpass.getpass(prompt="Confirm Password: ")

            if(passwd == confirm_passwd):
                salt, hashed_passwd = crypto_hash.gen_hash(passwd)
                #update database
                config.user['uname'] = uname
                config.user['salt'] = salt
                config.user['passwd'] = hashed_passwd

                return User.User(2, uname)

            else:
                print("Sorry, passwords do not match!")
                continue
        else:
            raise SignupFailedError

    except SignupFailedError:
        print("Sorry, we are unable to sign you up")
        print("Press any key to return")
        getch()
        return None