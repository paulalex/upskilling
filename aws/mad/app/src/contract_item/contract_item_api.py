import app.src.contract_item.contract_item_controller as controller
from app.src.api.api import AbstractHandler

class ContractItemHandler(AbstractHandler):
    """Handler implementation for the contract item API.
    """
    def create_handler(self, event, context):
        """Lambda handler for creating contract item resources. Extracts required properties from the
        event object and hands control to the contract item controller.

        Args:
            event: The AWS lambda event object.
            context: The AWS lambda context object.
        """
        quote_id = event.get("quote_id")
        mpan = event.get("mpan")
        
        controller.create(quote_id, mpan)

    def read_handler(self, event, context):
        """Lambda handler for reading contract item resources. Extracts required properties from the
        event object and hands control to the contract item controller.

        Args:
            event: The AWS lambda event object.
            context: The AWS lambda context object.

        Returns:
            The contract item from the database if it exists.
        """
        contract_item_id = event.get("contract_item_id")

        return controller.read(contract_item_id)

    def read_all_handler(self, event, context):
        """Lambda handler for reading all contract item resources. Extracts required properties from the
        event object and hands control to the contract item controller.

        Args:
            event: The AWS lambda event object.
            context: The AWS lambda context object.

        Returns:
            All contract items in the database. 
        """
        return controller.read_all()

    def update_handler(self, event, context):
        """Lambda handler for updating contract item resources. Extracts required properties from the
        event object and hands control to the contract item controller.

        Args:
            event: The AWS lambda event object.
            context: The AWS lambda context object.            
        """
        contract_item_id = event.get("contract_item_id")
        mpan = event.get("mpan")

        controller.update(contract_item_id, mpan)

    def delete_handler(self, event, context):
        """Lambda handler for deleting contract item resources. Extracts required properties from the
        event object and hands control to the contract item controller.

        Args:
            event: The AWS lambda event object.
            context: The AWS lambda context object.
        """
        contract_item_id = event.get("contract_item_id")

        controller.delete(contract_item_id)

handler = ContractItemHandler()

if __name__ == "__main__":
    handler.create_handler({"quote_id": 4, "mpan": "MPAN1234566"}, {})
    
    print(handler.read_handler({"contract_item_id": 3}, {}))
    
    handler.update_handler({"contract_item_id": 3, "mpan": "MPAN777777"}, {})

    handler.delete_handler({"contract_item_id": 2}, {})

    print(handler.read_all_handler({}, {}))