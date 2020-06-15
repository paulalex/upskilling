import app.src.contract_item.contract_item_dao as dao

def create_contract_item(quote_id, mpan):
    dao.create_contract_item(quote_id, mpan)

def get_contract_item_by_id(contract_item_id):
    return dao.get_contract_item_by_id(contract_item_id)

def get_all():
    return dao.get_all()

def update_contract_item(contract_item_id, mpan):
    return dao.update_contract_item(contract_item_id, mpan)

def delete_contract_item(contract_item_id):
    return dao.delete_contract_item(contract_item_id)