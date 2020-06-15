from app.src.helper import postgres_helper as db

def create_contract_item(quote_id, mpan):
    db.execute_update("insert into contract_item values(DEFAULT, %s, %s)", (quote_id, mpan,))

def get_contract_item_by_id(contract_item_id):
    return db.execute_query("select * from contract_item where c_id = %s", (contract_item_id,))

def get_all():
    return db.execute_query("select * from contract_item", None)

def update_contract_item(contract_item_id, mpan):
    return db.execute_update("update contract_item set mpan = %s where c_id = %s", (mpan, contract_item_id,))

def delete_contract_item(contract_item_id):
    return db.execute_update("delete from contract_item where c_id = %s", (contract_item_id,))