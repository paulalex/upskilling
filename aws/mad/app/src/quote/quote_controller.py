import app.src.quote.quote_service as service

def create(request_id, company_reg_number, registered_postcode):
    """Controller function for handling the creation of quote resources.

    Args:
        request_id: The ID of the request that this quote belongs to.
        company_reg_number: The company registration number.
        registered_postcode: The customers registered postcode.
    """
    service.create_quote(request_id, company_reg_number, registered_postcode)

def read(quote_id):
    """Controller function for handling the reading of quote resources.

    Args:
        quote_id: The id of the quote.
    
    Returns:
        All quotes from the database.
    """
    return service.get_quote_by_id(quote_id)

def read_all():
    """Controller function for handling the reading of all quote resources.

    Returns:
        The quote from the database if it exists.
    """
    return service.get_all()

def update(quote_id, company_reg_number, registered_postcode):
    """Controller function for handling the updating of request resources.

    Args:
        quote_id: The id of the request.
        company_reg_number: The company registration number.
        registered_postcode: The customers registered postcode.
    """
    service.update_quote(quote_id, company_reg_number, registered_postcode)

def delete(quote_id):
    """Controller function for handling the deletion of quote resources.

    Args:
        quote_id: The unique quote ID to delete.
    """
    service.delete_quote(quote_id)