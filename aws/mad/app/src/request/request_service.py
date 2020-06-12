from app.src.utils import postgres_helper as dao

def create_request(email, customer_reference):
    dao.execute_update("insert into request values(DEFAULT, %s, %s)", (email, customer_reference,))

def get_request_by_id(request_id):
    return dao.execute_query("select * from request where request_id = %s", (request_id,))

def get_all():
    return dao.execute_query("select * from request", None)

def update_request(request_id, email, customer_reference):
    return dao.execute_update("update request set customer_email = %s, customer_reference = %s where request_id = %s", (email, customer_reference, request_id,))

def delete_request(request_id):
    return dao.execute_update("delete from request where request_id = %s", (request_id,))


