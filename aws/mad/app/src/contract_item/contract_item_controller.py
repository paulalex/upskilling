import app.src.contract_item.contract_item_service as service

def create(quote_id, mpan):
    """Controller function for handling the creation of contract item resources.

    Args:
        quote_id: The unique quote ID that this contract item belongs to.
        mpan: The customers unique meter number.
    """
    service.create_contract_item(quote_id, mpan)

def read(contract_item_id):
    """Controller function for handling the reading of contract item resources.

    Args:
        contract_item_id: The id of the contract item.
    
    Returns:
        The contract item from the database if it exists.
    """
    return service.get_contract_item_by_id(contract_item_id)

def read_all():
    """Controller function for handling the reading of all contract item resources.

    Returns:
        All contract items from the database.
    """
    return service.get_all()

def update(contract_item_id, mpan):
    """Controller function for handling the updating of contract item resources.

    Args:
        contract_item_id: The id of the contract item.
        mpan: The customers unique meter number.
    """
    service.update_contract_item(contract_item_id, mpan)

def delete(contract_item_id):
    """Controller function for handling the deletion of contract item resources.

    Args:
        contract_item_id: The id of the contract item to delete.
    """
    service.delete_contract_item(contract_item_id)