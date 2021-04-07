from modules.db import connect

import getch

def add_user(first_name, last_name,uname, salt, passwd):
    """Add user to database\n
    Argument: first_name, last_name, uname, salt, passwd\n
    Return: uid of inserted user
    """
    query = f"""
        INSERT INTO users (firstName, lastName, uname, salt, passwd) VALUES (
            '{first_name}',
            '{last_name}',
            '{uname}',
            UNHEX('{salt.hex()}'),
            UNHEX('{passwd.hex()}')
        )
    """

    def query_func(conn):
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        
        uid = cursor.lastrowid
        return uid

    return connect.exec_func(query_func)