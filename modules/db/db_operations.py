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
        with conn.cursor() as cursor:
            cursor.execute(query)
            conn.commit()
        
            uid = cursor.lastrowid
        return uid

    return connect.exec_func(query_func)

def get_file(uid):
    """Argument: uid\n
    Return: (enc_key, content) if file exist else None
    """

    query = f"""
    SELECT enc_key, content FROM files WHERE uid={uid}
    """

    def query_func(conn):
        with conn.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchone()
        return result

    result = connect.exec_func(query_func)

    return result if result else (None, None)

def create_file_record(uid):
    query = f"""
    INSERT INTO files (uid, content) VALUES (
        {uid},
        '[]'
    )
    """

    def query_func(conn):
        with conn.cursor() as cursor:
            cursor.execute(query)
        conn.commit()
        return

    connect.exec_func(query_func)
    


def update_file(uid, content):
    """Updates the content column of files table"""

    query = f"""
    UPDATE files SET content='{content}' WHERE uid={uid}
    """

    def query_func(conn):
        with conn.cursor() as cursor:
            cursor.execute(query)
        conn.commit()
        return

    connect.exec_func(query_func)
    return



def delete_account(uid):
    query1 = f"""
    DELETE FROM files WHERE uid={uid}
    """
    query2 = f"""
    DELETE FROM users WHERE uid={uid}
    """

    def query_func(conn):
        with conn.cursor() as cursor:
            cursor.execute(query1)
            cursor.execute(query2)
        conn.commit()
        return

    connect.exec_func(query_func)
    return