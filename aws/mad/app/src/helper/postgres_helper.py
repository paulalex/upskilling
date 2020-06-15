import psycopg2

def execute_update(statement, params):
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
    return psycopg2.connect(user = "mad_user",
                            password = "mad_password",
                            host = "127.0.0.1",
                            port = "5432",
                            database = "mad_database")

# Make this a decorator
def log(statement):
    print(f"[INFO] Running Query: {statement}")