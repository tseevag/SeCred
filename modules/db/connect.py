import os
from dotenv import load_dotenv
from mysql.connector import connect, Error
from modules.exit_utils import exit_program

def exec_func(func):
    """
    Argument: function which takes connection object as argument and executes database query\n
    Return: result of query
    """
    load_dotenv('.env')

    host = os.getenv('DB_HOST')
    db = os.getenv('DB_NAME')
    user = os.getenv('DB_USER')
    password = os.getenv('DB_PASSWORD')

    try:
        with connect(
            host = host,
            user = user,
            password = password,
            database = db

        ) as connection:
            result = func(connection)
            return(result)

    except Error:
        print("Unable to connect to database !")
        print("Please check your connection to database or contact dabase administrator.")
    
        exit_program()

