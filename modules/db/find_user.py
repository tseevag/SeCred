import config
from modules.db import connect

def get_user(uname):
    """Argument: uname\n
    Return: (uid, uname, 0xsalt, 0xpasswd)
    """
    query = f"""
    SELECT uid, uname, HEX(salt), HEX(passwd) FROM users WHERE uname='{uname}'
    """
    def query_func(conn):
        cursor = conn.cursor()
        cursor.execute(query)
        result = cursor.fetchone()
        return result


    user = connect.exec_func(query_func)

    if(user != None):
        return user  
    else:
        return None


def get_dummy_user():
    user = (0, 'user',\
        '583e549c996c95371993a4e29ea222d47ecdb96bd38c69cb4eb8d2d4fb4353b0',\
        'c753199d53073bc2277cf8c9459cdcc56ac50f9d3e86c2ec48de079c37ca18221d742e61ab4941db4a1851430f9305500bba5607ef5e787df4f0b5b8aa46ca01'\
        )

    return user