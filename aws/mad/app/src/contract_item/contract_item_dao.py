from app.src.helper import postgres_helper as db

def create_contract_item(quote_id, mpan):
    """Creates a contract item in the the database.

    Args:
        quote_id: The id of the quote.
        mpan: The meter identifier.
    
    Returns:
        All quotes from the database.
    """
    db.execute_update("insert into contract_item values(DEFAULT, %s, %s)", (quote_id, mpan,))

def get_contract_item_by_id(contract_item_id):
    """Gets a contract item from the database using its ID.

    Args:
        contract_item_id: The id of the contract item.
    
    Returns:
        The contract item if it exists.
    """
    return db.execute_query("select * from contract_item where c_id = %s", (contract_item_id,))

def get_all():
    """Gets all contract items from the database.

    Returns:
        All contract items from the database.
    """
    return db.execute_query("select * from contract_item", None)

def update_contract_item(contract_item_id, mpan):
    """Updates a contract item.

    Args:
        contract_item_id: The id of the contract item.
        mpan: The meter identifier.
    """
    db.execute_update("update contract_item set mpan = %s where c_id = %s", (mpan, contract_item_id,))

def delete_contract_item(contract_item_id):
    """Deletes a contract item from the database.

    Args:
        contract_item_id: The id of the contract item.
    """
    db.execute_update("delete from contract_item where c_id = %s", (contract_item_id,))