import app.src.contract_item.contract_item_dao as dao

def create_contract_item(quote_id, mpan):
    """Create a contract item in the data store.

    Args:
        quote_id: The id of the quote that the contract item belongs to.
        mpan: The id of the request item.
    """
    dao.create_contract_item(quote_id, mpan)

def get_contract_item_by_id(contract_item_id):
    """Gets a contract item from the database using its ID.

    Args:
        contract_item_id: The id of the request item.
    
    Returns:
        The contract item if it exists.
    """
    return dao.get_contract_item_by_id(contract_item_id)

def get_all():
    """Get all contract items from the database..
    
    Returns:
        All contract items.
    """
    return dao.get_all()

def update_contract_item(contract_item_id, mpan):
    """Gets a contract item from the database using its ID.

    Args:
        contract_item_id: The id of the contract item.
    
    Returns:
        The contract item if it exists.
    """
    dao.update_contract_item(contract_item_id, mpan)

def delete_contract_item(contract_item_id):
    """Gets a request from the database using its ID.

    Args:
        request_id: The id of the request item.
    
    Returns:
        The request item if it exists.
    """
    dao.delete_contract_item(contract_item_id)