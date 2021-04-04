import os
from dotenv import load_dotenv
from mysql.connector import connect, Error

def execute_func(func):
    """
    Argument: function which executes database query
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
            with connection.cursor() as cursor:
                result = func(cursor)
                return result

    except Error:
        print("Unable to connect to database"):

