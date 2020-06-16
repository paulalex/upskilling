from app.src.helper import postgres_helper as db

def create_quote(request_id, company_reg_number, registered_postcode):
    """Creates a quote in the the database.

    Args:
        request_id: The id of the request this quote belongs to.
        company_reg_number: The companies registration number.
        registered_postcode: The conpanies postcode.
    """
    db.execute_update("insert into quote values(DEFAULT, %s, %s, %s)", (request_id, company_reg_number, registered_postcode,))

def get_quote_by_id(quote_id):
    """Gets a quote from the database using its ID.

    Args:
        quote_id: The id of the quote item.
    
    Returns:
        The quote if it exists.
    """
    return db.execute_query("select * from quote where quote_id = %s", (quote_id,))

def get_all():
    """Gets all quotes from the database.

    Returns:
        All quotess from the database.
    """
    return db.execute_query("select * from quote", None)

def update_quote(quote_id, company_reg_number, registered_postcode):
    """Updates a quote.

    Args:
        quote_id: The id of the quote.
        company_reg_number: The company registration number.
        registered_postcode: The registered postcode.
    """
    db.execute_update("update quote set company_reg_number = %s, registered_postcode = %s \
    where quote_id = %s", (company_reg_number, registered_postcode, quote_id,))

def delete_quote(quote_id):
    """Deletes a quote from the database.

    Args:
        quote_id: The id of the quote.
    """
    db.execute_update("delete from quote where quote_id = %s", (quote_id,))