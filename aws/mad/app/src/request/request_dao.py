from app.src.helper import postgres_helper as db

def create_request(email, customer_reference):
    """Creates a request in the the database.

    Args:
        email: The email of the requesting company.
        customer_reference: The customer reference number.
    """
    db.execute_update("insert into request values(DEFAULT, %s, %s)", (email, customer_reference,))

def get_request_by_id(request_id):
    """Gets a request from the database using its ID.

    Args:
        request_id: The id of the request item.
    
    Returns:
        The request if it exists.
    """
    return db.execute_query("select * from request where request_id = %s", (request_id,))

def get_all():
    """Gets all requests from the database.

    Returns:
        All requests from the database.
    """
    return db.execute_query("select * from request", None)

def update_request(request_id, email, customer_reference):
    """Updates a request.

    Args:
        request_id: The id of the request.
        mpan: The meter identifier.
    """
    db.execute_update("update request set customer_email = %s, customer_reference = %s where request_id = %s", (email, customer_reference, request_id,))

def delete_request(request_id):
    """Deletes a request from the database.

    Args:
        request_id: The id of the request.
    """
    db.execute_update("delete from request where request_id = %s", (request_id,))