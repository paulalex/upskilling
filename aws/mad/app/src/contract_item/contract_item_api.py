import app.src.contract_item.contract_item_controller as controller

def create_handler(event, context):
    quote_id = event.get("quote_id")
    mpan = event.get("mpan")
    
    controller.create(quote_id, mpan)

def read_handler(event, context):
    contract_item_id = event.get("contract_item_id")

    return controller.read(contract_item_id)

def read_all_handler(event, context):
    return controller.read_all()

def update_handler(event, context):
    contract_item_id = event.get("contract_item_id")
    mpan = event.get("mpan")

    return controller.update(contract_item_id, mpan)

def delete_handler(event, context):
    contract_item_id = event.get("contract_item_id")

    return controller.delete(contract_item_id)

if __name__ == "__main__":
    create_handler({"quote_id": 4, "mpan": "MPAN1234566"}, {})
    
    print(read_handler({"contract_item_id": 3}, {}))
    
    update_handler({"contract_item_id": 3, "mpan": "MPAN777777"}, {})

    delete_handler({"contract_item_id": 2}, {})

    print(read_all_handler({}, {}))