import app.src.request.request_service as service

def create(email, customer_reference):
    service.create_request(email, customer_reference)

def read(request_id):
    return service.get_request_by_id(request_id)

def read_all():
    return service.get_all()

def update(request_id, email, customer_reference):
    service.update_request(request_id, email, customer_reference)

def delete(request_id):
    service.delete_request(request_id)