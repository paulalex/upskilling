from app.src.helper import postgres_helper as db

def create_request(email, customer_reference):
    db.execute_update("insert into request values(DEFAULT, %s, %s)", (email, customer_reference,))

def get_request_by_id(request_id):
    return db.execute_query("select * from request where request_id = %s", (request_id,))

def get_all():
    return db.execute_query("select * from request", None)

def update_request(request_id, email, customer_reference):
    return db.execute_update("update request set customer_email = %s, customer_reference = %s where request_id = %s", (email, customer_reference, request_id,))

def delete_request(request_id):
    return db.execute_update("delete from request where request_id = %s", (request_id,))