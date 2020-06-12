import request_service as service

def create():
    pass

def read():
    print("Calling Controller")
    dir(service)
    return service.get_request_by_id(id)

def update():
    pass

def delete():
    pass