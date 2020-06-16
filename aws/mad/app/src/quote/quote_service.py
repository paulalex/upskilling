import app.src.quote.quote_dao as dao

def create_quote(request_id, company_reg_number, registered_postcode):
    """Creates a quote in the database.

    Args:
        request_id: The id of the request that this quote belongs to.
        company_reg_number: The id of the request that this quote belongs to.
        registered_postcode: The id of the request that this quote belongs to.
    """
    dao.create_quote(request_id, company_reg_number, registered_postcode)

def get_quote_by_id(quote_id):
    """Gets a quote from the database using its ID.

    Args:
        quote_id: The id of the request item.
    
    Returns:
        The quote if it exists.
    """
    return dao.get_quote_by_id(quote_id)

def get_all():
    """Gets all quotes from the database.
    
    Returns:
        All quotes held in the database.
    """
    return dao.get_all()

def update_quote(quote_id, company_reg_number, registered_postcode):
    """Updates a quote in the database using its ID.

    Args:
        quote_id: The id of the quote.
        company_reg_number: The company registration number.
        registered_postcode: The registered postcode of the company.
    """
    dao.update_quote(quote_id, company_reg_number, registered_postcode)

def delete_quote(quote_id):
    """Deletes a quote from the database using its ID.

    Args:
        request_id: The id of the request item.
    """
    dao.delete_quote(quote_id)


