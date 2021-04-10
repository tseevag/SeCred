import getch

import config
from modules import menu
from .db import db_operations

from .file import File

def ip_site_name():
    while True:
        site = input("Name of site: ")

        if(site):
            return site
        else:
            print("Name of site not specified !\n")
            continue
    

def view_record():
    menu.display_title('view record')

    current_user = config.CURRENT_USER
    
    site = ip_site_name()

    enc_key, content = db_operations.get_file(current_user.get_uid())

    f = File(enc_key, content)

    record = f.get_site_record(site)

    if(record):
        print(f"Record for {site}:")
        print(f"Username: {record['uname']}")
        print(f"Password: {record['passwd']}")

        print("\nEnter any key to return")
        getch.getch()
    else:
        print("Record not available for specified site!")
        print("Press any key to return.")
        getch.getch()


def view_all_records():
    menu.display_title('view all records')

    current_user = config.CURRENT_USER

    enc_key, content = db_operations.get_file(current_user.get_uid())

    f = File(enc_key, content)

    records = f.content_to_list()    

    for record in records:
        print('Site: ', record['site'])
        print('User Name: ', record['uname'])
        print('Password: ', record['passwd'])
        print()

    print("Press any key to return")
    getch.getch()
    return


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

    current_user = config.CURRENT_USER

    site = ip_site_name()

    enc_key, content = db_operations.get_file(current_user.get_uid())

    f = File(enc_key, content)
    
    uname = input("New user name: ")
    passwd = input("New password: ")

    f.delete_record(site)

    content = f.add_record(site, uname, passwd)

    db_operations.update_file(current_user.get_uid(), content)

    



def delete_record():
    menu.display_title("delete record")

    current_user = config.CURRENT_USER

    site = ip_site_name()

    enc_key, content = db_operations.get_file(current_user.get_uid())

    f = File(enc_key, content)

    try:
        content = f.delete_record(site)
        db_operations.update_file(current_user.get_uid(), content)
    except ValueError:
        print("Record doesn't exist!")
        print("Press any key to return")
        getch.getch()




def delete_account():

    current_user = config.CURRENT_USER

    db_operations.delete_account(current_user.get_uid())

    logout()

    return
    

def logout():
    config.CURRENT_USER = None
    return