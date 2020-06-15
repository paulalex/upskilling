import app.src.contract_item.contract_item_controller as controller
from app.src.api.api import AbstractHandler

class ContractItemHandler(AbstractHandler):
    def create_handler(self, event, context):
        quote_id = event.get("quote_id")
        mpan = event.get("mpan")
        
        controller.create(quote_id, mpan)

    def read_handler(self, event, context):
        contract_item_id = event.get("contract_item_id")

        return controller.read(contract_item_id)

    def read_all_handler(self, event, context):
        return controller.read_all()

    def update_handler(self, event, context):
        contract_item_id = event.get("contract_item_id")
        mpan = event.get("mpan")

        return controller.update(contract_item_id, mpan)

    def delete_handler(self, event, context):
        contract_item_id = event.get("contract_item_id")

        return controller.delete(contract_item_id)

handler = ContractItemHandler()

if __name__ == "__main__":
    handler.create_handler({"quote_id": 4, "mpan": "MPAN1234566"}, {})
    
    print(handler.read_handler({"contract_item_id": 3}, {}))
    
    handler.update_handler({"contract_item_id": 3, "mpan": "MPAN777777"}, {})

    handler.delete_handler({"contract_item_id": 2}, {})

    print(handler.read_all_handler({}, {}))