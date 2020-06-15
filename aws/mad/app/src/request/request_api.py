import app.src.request.request_controller as controller
from app.src.api.api import AbstractHandler

class RequestHandler(AbstractHandler):
    def create_handler(self, event, context):
        customer_email = event.get("customer_email")
        customer_reference = event.get("customer_reference")

        controller.create(customer_email, customer_reference)

    def read_handler(self, event, context):
        request_id = event.get("request_id")

        return controller.read(request_id)

    def read_all_handler(self, event, context):
        return controller.read_all()

    def update_handler(self, event, context):
        request_id = event.get("request_id")
        customer_email = event.get("customer_email")
        customer_reference = event.get("customer_reference")

        return controller.update(request_id, customer_email, customer_reference)

    def delete_handler(self, event, context):
        request_id = event.get("request_id")

        return controller.delete(request_id)

handler = RequestHandler()

if __name__ == "__main__":
    handler.create_handler({"customer_email": "paul.ockleford@edfenergy.com", "customer_reference": "REF1234"}, {})
    
    print(handler.read_handler({"request_id": 1}, {}))
    
    handler.update_handler({"request_id": 1, "customer_email": "new@edfenergy.com", "customer_reference": "REF5678"}, {})

    handler.delete_handler({"request_id": 1}, {})

    print(handler.read_all_handler({}, {}))


