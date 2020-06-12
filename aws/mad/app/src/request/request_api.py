import request_controller as controller


def create_handler(event, context):
    customer_email = event.get("customer_email")
    customer_reference = event.get("customer_reference")

    controller.create(customer_email, customer_reference)

def read_handler(event, context):
    request_id = event.get("request_id")

    return controller.read(request_id)

def read_all_handler(event, context):
    return controller.read_all()

def update_handler(event, context):
    request_id = event.get("request_id")
    customer_email = event.get("customer_email")
    customer_reference = event.get("customer_reference")

    return controller.update(request_id, customer_email, customer_reference)

def delete_handler(event, context):
    request_id = event.get("request_id")

    return controller.delete(request_id)

if __name__ == "__main__":
    create_handler({"customer_email": "paul.ockleford@edfenergy.com", "customer_reference": "REF1234"}, {})
    
    print(read_handler({"request_id": 1}, {}))
    
    update_handler({"request_id": 1, "customer_email": "new@edfenergy.com", "customer_reference": "REF5678"}, {})

    delete_handler({"request_id": 1}, {})

    print(read_all_handler({}, {}))

    create_handler({"customer_email": "customer5@email.com", "customer_reference": "REF1234"}, {})

