import app.src.contract_item.contract_item_service as service

def create(quote_id, mpan):
    service.create_contract_item(quote_id, mpan)

def read(contract_item_id):
    return service.get_contract_item_by_id(contract_item_id)

def read_all():
    return service.get_all()

def update(contract_item_id, mpan):
    service.update_contract_item(contract_item_id, mpan)

def delete(contract_item_id):
    service.delete_contract_item(contract_item_id)