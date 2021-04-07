import os
import math

import config
from modules import operations
from modules.auth import login
from modules.auth import signup
from modules.exit_utils import exit_program

clear = lambda: os.system("clear")

def display_title(title_string):
    # clear()
    window_width = config.WINDOW_WIDTH
    space_count = math.floor( (window_width/2) - (len(title_string)/2) ) 

    print('=' * window_width)
    print(' ' * space_count + title_string.title())
    print('='* window_width)


def prompt_menu():
    """
    Prompts options for differents operations

    return value: choise of operation
    """
    if(config.CURRENT_USER == None):
        return

    switcher = {
        '1': operations.add_record,
        '2': operations.update_record,
        '3': operations.delete_record,
        '4': operations.delete_account,
        '5': operations.logout,
        'exit': exit_program
    }
    
    display_title("menu")

    while True:
        print("Choose an option (enter 'exit' to exit SeCred)")
        print("[1] Add new record")
        print("[2] Update existing record")
        print("[3] Delete existing record")
        print("[4] Delete account and all related information")
        print("[5] Logout")
        print()
        print("Enter your choise")

        choise = input("> ").lower()

        if(choise in switcher.keys()):
            return switcher.get(choise)

        else:
            print("Please enter a valid choise.")
            prompt_menu()

def landing_window():
    """Prompts option for Sign up and login
    Return: choise"""
    
    switcher = {
            '1': signup.signup,
            '2': login.login,
            'exit': exit_program
        }

    display_title("Welcome to SecRed")

    print("Choose a option (press 'exit' to exit SeCred)")
    
    while True:
        print("[1] Sign Up")
        print("[2] Login")

        choise = input("> ").lower()

        if( choise in switcher.keys()):
            return switcher.get(choise)
        else:
            print("Please make a valid choise!")
            continue
