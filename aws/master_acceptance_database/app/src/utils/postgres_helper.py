from app.lib.psycopg2 import psycopg2

def get_connection():
    connection = psycopg2.connect(user = "mad_user",
                                  password = "mad_password",
                                  host = "127.0.0.1",
                                  port = "5432",
                                  database = "mad_database")

    return connection