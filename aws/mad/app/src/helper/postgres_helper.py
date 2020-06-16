import os
import functools

import psycopg2

def execute_update(statement, params):
    """Execute a database update using the supplied prepared statement and tuple of parameters, this returns
    no values from the database.

        Args:
            statement: Prepared statement that should be executed.
            params: A tuple of parameters that map to the bind variables in the statement.
    """
    log(statement)
    connection = None
    cursor = None
    
    try:
        connection = get_connection()

        cursor = connection.cursor()

        cursor.execute(statement, params)

        cursor.close()

        connection.commit()

        connection.close()
    except Exception as e:
        print(e)

        if(connection):
            cursor.close()
            connection.close()

        raise e

def execute_query(statement, params):
    """Execute a database query using the supplied prepared statement and tuple of parameters and return
    the output cursor.

        Args:
            statement: Prepared statement that should be executed.
            params: A tuple of parameters that map to the bind variables in the statement.

        Returns:
            The output cursor as a map which represents the data items returned when executing the supplied query and bind variables.
    """
    log(statement)
    connection = None

    try:
        connection = get_connection()
        cursor = connection.cursor()

        if params:
            cursor.execute(statement, params)
        else:
            print(f"Executing {statement}")
            cursor.execute(statement)
        
        result = cursor.fetchall()

        cursor.close()

        connection.close()

        return result
    except Exception as e:
        print(e)

        if(connection):
            cursor.close()
            connection.close()

        raise e

def get_connection():
    db_user = os.environ['POSTGRES_USER']
    db_pwd = os.environ['POSTGRES_PASSWORD']
    db_database = os.environ['POSTGRES_DB']
    db_host = os.environ['POSTGRES_HOST']
    db_port = os.environ['POSTGRES_PORT']
    
    return psycopg2.connect(user = db_user,
                            password = db_pwd,
                            database = db_database,
                            host = db_host,
                            port = db_port)

# Make this a decorator
def log(statement):
    print(f"[INFO] Running Query: {statement}")