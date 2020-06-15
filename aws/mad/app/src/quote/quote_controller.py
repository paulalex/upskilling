import app.src.quote.quote_service as service

def create(request_id, company_reg_number, registered_postcode):
    service.create_quote(request_id, company_reg_number, registered_postcode)

def read(quote_id):
    return service.get_quote_by_id(quote_id)

def read_all():
    return service.get_all()

def update(quote_id, company_reg_number, registered_postcode):
    service.update_quote(quote_id, company_reg_number, registered_postcode)

def delete(quote_id):
    service.delete_quote(quote_id)