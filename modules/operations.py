import os

import config
from modules import menu
from .db import db_operations

from .file import File


def add_record():
    menu.display_title("add record")

    current_user = config.CURRENT_USER

    site = input('Name of Site:')
    uname = input('Username:')
    passwd = input('Password:')

    enc_key, content = db_operations.get_file(current_user.get_uid())

    if(content == None):
        content = b'[]'
    
    #decrypt content

    f = File(enc_key, content)

    content = f.add_record(site, uname, passwd)

    db_operations.update_file(current_user.get_uid(), content)



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
    return