import app.src.request.request_dao as dao

def create_request(email, customer_reference):
    """Creates a request in the database.

    Args:
        email: The customers email.
        customer_reference: The customers unique reference number.
    """
    dao.create_request(email, customer_reference)

def get_request_by_id(request_id):
    """Gets a request from the database using its ID.

    Args:
        request_id: The id of the request item.
    
    Returns:
        The request if it exists.
    """
    return dao.get_request_by_id(request_id)

def get_all():
    """Gets all requests from the database using its ID.

    Args:
        request_id: The id of the request item.
    
    Returns:
        All requests in the database.
    """
    return dao.get_all()

def update_request(request_id, email, customer_reference):
    """Updates a request int the database using its ID.

    Args:
        request_id: The id of the request item.
    """
    return dao.update_request(request_id, email, customer_reference)

def delete_request(request_id):
    """Deletes a request from the database using its ID.

    Args:
        request_id: The id of the request item.
    """
    return dao.delete_request(request_id)


