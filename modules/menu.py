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
        '1': operations.view_record,
        '2': operations.view_all_records,
        '3': operations.add_record,
        '4': operations.update_record,
        '5': operations.delete_record,
        '6': operations.delete_account,
        '7': operations.logout,
        'exit': exit_program
    }
    
    display_title("menu")

    while True:
        print("Choose an option (enter 'exit' to exit SeCred)")
        print("[1] View site record")
        print("[2] View all records")
        print("[3] Add new record")
        print("[4] Update existing record")
        print("[5] Delete existing record")
        print("[6] Delete account and all related information")
        print("[7] Logout")
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
            '1': login.login,
            '2': signup.signup,
            'exit': exit_program
        }

    display_title("Welcome to SecRed")

    print("Choose a option (press 'exit' to exit SeCred)")
    
    while True:
        print("[1] Login")
        print("[2] Sign Up")

        choise = input("> ").lower()

        if( choise in switcher.keys()):
            return switcher.get(choise)
        else:
            print("Please make a valid choise!")
            continue
