from app.src.helper import postgres_helper as db

def create_quote(request_id, company_reg_number, registered_postcode):
    db.execute_update("insert into quote values(DEFAULT, %s, %s, %s)", (request_id, company_reg_number, registered_postcode,))

def get_quote_by_id(quote_id):
    return db.execute_query("select * from quote where quote_id = %s", (quote_id,))

def get_all():
    return db.execute_query("select * from quote", None)

def update_quote(quote_id, company_reg_number, registered_postcode):
    return db.execute_update("update quote set company_reg_number = %s, registered_postcode = %s \
    where quote_id = %s", (company_reg_number, registered_postcode, quote_id,))

def delete_quote(quote_id):
    return db.execute_update("delete from quote where quote_id = %s", (quote_id,))