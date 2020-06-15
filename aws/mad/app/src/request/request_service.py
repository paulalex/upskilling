import app.src.request.request_dao as dao

def create_request(email, customer_reference):
    dao.create_request(email, customer_reference)

def get_request_by_id(request_id):
    return dao.get_request_by_id(request_id)

def get_all():
    return dao.get_all()

def update_request(request_id, email, customer_reference):
    return dao.update_request(request_id, email, customer_reference)

def delete_request(request_id):
    return dao.delete_request(request_id)


