import getpass
from getch import getch

from data import User
from modules import menu
from modules.error import *


def signup():
    """Returns:
     currently if sign up successfull
     else None
     """
    menu.display_title("sign up")
    unmatch_count = 0

    try:
        first_name = input("First Name: ").split()[0]
        last_name = input("Last Name: ").split()[0]
        uname = input("User Name: ")

        # if uname_exits:
        
        while (unmatch_count < 3):
            passwd = getpass.getpass()
            confirm_passwd = getpass.getpass(prompt="Confirm Password: ")

            if(passwd == confirm_passwd):
                #generate password hash
                #update database
                return User.User(2, uname)

            else:
                print("Sorry, passwords do not match!")
                unmatch_count += 1

        else:
            raise SignupFailedError

    except SignupFailedError:
        print("Sorry, we are unable to sign you up")
        print("Press any key to return")
        getch()
        return None