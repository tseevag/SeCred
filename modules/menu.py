import sys
import math

from modules.exit_utils import exit_program

def display_title(title_string):
    space_count = math.floor(25 - len(title_string)/2) 

    print('='*50)
    print(' ' * space_count + title_string.title())
    print('='*50)


def prompt_menu(render_title = True):
    """
    Prompts options for differents operations

    return value: choise of operation
    """
    valid_choises = {'1', '2', '3', '4', '5', 'exit'}

    if render_title:
        display_title("menu")

    print("Enter 'exit' to exit")
    print("[1] Add new record")
    print("[2] Update existing record")
    print("[3] Delete existing record")
    print("[4] Delete account and all related information")
    print("[5] Logout")
    print()
    print("Enter your choise")

    choise = input("> ").lower()

    if(choise == 'exit'):
        exit_program()

    elif(choise not in valid_choises):
        print("Please enter a valid choise.")
        prompt_menu()

    else:
        return choise

def landing_window():
    pass
