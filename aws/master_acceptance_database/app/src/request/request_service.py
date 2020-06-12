# import sys
# print(sys.path)
from app.src.utils import postgres_helper

def get_request_by_id(id):
    return "Calling Service"
    # try:
    #     connection = dao.get_connection()
    #     cursor = connection.cursor()
    #     cursor.execute("SELECT version();")
    #     record = cursor.fetchone()

    #     return record
    # except Exception as e:
    #     print(e)
    # finally:
    #     if(connection):
    #         cursor.close()
    #         connection.close()
