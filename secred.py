import os

from modules import menu
from modules import operations
from modules.exit_utils import exit_program

def main():
    menu.display_title("Welcome to SecRed")

    # choise = menu.prompt_menu(render_title=False)
    
    # if choise=='1':
    #     operations.add_record()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit_program()
