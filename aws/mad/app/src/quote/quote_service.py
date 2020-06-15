import app.src.quote.quote_dao as dao

def create_quote(request_id, company_reg_number, registered_postcode):
    dao.create_quote(request_id, company_reg_number, registered_postcode)

def get_quote_by_id(quote_id):
    return dao.get_quote_by_id(quote_id)

def get_all():
    return dao.get_all()

def update_quote(quote_id, company_reg_number, registered_postcode):
    return dao.update_quote(quote_id, company_reg_number, registered_postcode)

def delete_quote(quote_id):
    return dao.delete_quote(quote_id)


