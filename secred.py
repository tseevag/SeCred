import config
from modules import menu
from modules.exit_utils import exit_program


def main():
    current_user = config.CURRENT_USER

    while(current_user == None):
        func = menu.landing_window()
        current_user = func() 

        config.CURRENT_USER = current_user

    else:
        func = menu.prompt_menu()
        func()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit_program()
