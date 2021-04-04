import os

import secred
import config
from modules import menu


def add_record():
    menu.display_title("add record")

    pass

def update_record():
    menu.display_title("Update record")

    pass

def delete_record():
    menu.display_title("delete record")

    pass

def delete_account():
    menu.display_title("delete Account")

    pass

def logout():
    config.CURRENT_USER = None
    secred.main()