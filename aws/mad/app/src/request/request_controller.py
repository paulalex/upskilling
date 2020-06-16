import app.src.request.request_service as service

def create(email, customer_reference):
    """Controller function for handling the creation of request resources.

    Args:
        email: The customers email address.
        customer_reference: The customers unique reference number.
    """
    service.create_request(email, customer_reference)

def read(request_id):
    """Controller function for handling the reading of request resources.

    Args:
        request_id: The id of the request.
        context: The AWS lambda context object.

    Returns:
        The contract item from the database if it exists.
    """
    return service.get_request_by_id(request_id)

def read_all():
    """Controller function for handling the reading of all request resources.

    Returns:
        All requests from the database.
    """
    return service.get_all()

def update(request_id, email, customer_reference):
    """Controller function for handling the updating of request resources.

    Args:
        request_id: The id of the request.
        email: The customers email address.
        customer_reference: The customers unique reference number.
    """
    service.update_request(request_id, email, customer_reference)

def delete(request_id):
    """Controller function for handling the deletion of request resources.

    Args:
        request_id: The ID of the request to delete.
    """
    service.delete_request(request_id)