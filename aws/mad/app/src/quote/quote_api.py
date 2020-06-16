import app.src.quote.quote_controller as controller
from app.src.api.api import AbstractHandler

class QuoteHandler(AbstractHandler):
    """Handler implementation for the quote item API.
    """
    def create_handler(self, event, context):
        """Lambda handler for creating quote resources. Extracts required properties from the
        event object and hands control to the quote controller.

        Args:
            event: The AWS lambda event object.
            context: The AWS lambda context object.
        """
        request_id = event.get("request_id")
        company_reg_number = event.get("company_reg_number")
        registered_postcode = event.get("registered_postcode")

        controller.create(request_id, company_reg_number, registered_postcode)

    def read_handler(self, event, context):
        """Lambda handler for reading quote resources. Extracts required properties from the
        event object and hands control to the quote controller.

        Args:
            event: The AWS lambda event object.
            context: The AWS lambda context object.

        Returns:
            The quote from the database if it exists.
        """
        quote_id = event.get("quote_id")

        return controller.read(quote_id)

    def read_all_handler(self, event, context):
        """Lambda handler for reading all quote resources. Extracts required properties from the
        event object and hands control to the contract item controller.

        Args:
            event: The AWS lambda event object.
            context: The AWS lambda context object.

        Returns:
            All quotes from the database.
        """
        return controller.read_all()

    def update_handler(self, event, context):
        """Lambda handler for updating quote resources. Extracts required properties from the
        event object and hands control to the contract item controller.

        Args:
            event: The AWS lambda event object.
            context: The AWS lambda context object.
        """
        quote_id = event.get("quote_id")
        company_reg_number = event.get("company_reg_number")
        registered_postcode = event.get("registered_postcode")

        controller.update(quote_id, company_reg_number, registered_postcode)

    def delete_handler(self, event, context):
        """Lambda handler for deleting quote resources. Extracts required properties from the
        event object and hands control to the contract item controller.

        Args:
            event: The AWS lambda event object.
            context: The AWS lambda context object.
        """
        quote_id = event.get("quote_id")

        controller.delete(quote_id)

handler = QuoteHandler()

if __name__ == "__main__":
    handler.create_handler({"request_id": 3, "company_reg_number": "REGTESTX", "registered_postcode": "NEW_POSTCODE"}, {})
    
    print(handler.read_handler({"quote_id": 3}, {}))
    
    handler.update_handler({"quote_id": 1, "company_reg_number": "NEW_REGTESTX", "registered_postcode": "CHANGED"}, {})

    handler.delete_handler({"quote_id": 1}, {})

    print(handler.read_all_handler({}, {}))

