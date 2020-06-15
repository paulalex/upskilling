import app.src.quote.quote_controller as controller
from app.src.api.api import AbstractHandler

class QuoteHandler(AbstractHandler):
    def create_handler(self, event, context):
        request_id = event.get("request_id")
        company_reg_number = event.get("company_reg_number")
        registered_postcode = event.get("registered_postcode")

        controller.create(request_id, company_reg_number, registered_postcode)

    def read_handler(self, event, context):
        quote_id = event.get("quote_id")

        return controller.read(quote_id)

    def read_all_handler(self, event, context):
        return controller.read_all()

    def update_handler(self, event, context):
        quote_id = event.get("quote_id")
        company_reg_number = event.get("company_reg_number")
        registered_postcode = event.get("registered_postcode")

        return controller.update(quote_id, company_reg_number, registered_postcode)

    def delete_handler(self, event, context):
        quote_id = event.get("quote_id")

        return controller.delete(quote_id)

handler = QuoteHandler()

if __name__ == "__main__":
    handler.create_handler({"request_id": 3, "company_reg_number": "REGTESTX", "registered_postcode": "NEW_POSTCODE"}, {})
    
    print(handler.read_handler({"quote_id": 3}, {}))
    
    handler.update_handler({"quote_id": 1, "company_reg_number": "NEW_REGTESTX", "registered_postcode": "CHANGED"}, {})

    handler.delete_handler({"quote_id": 1}, {})

    print(handler.read_all_handler({}, {}))

