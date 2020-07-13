from gas_api_exception import RequestValidationException

def validate_mprn_request(mprn):    
    errors = []
    if not len(mprn) >= 8:
        errors.append("Field request.mprn should be greater than or equal to 8 digits.")
    if not mprn.isnumeric():
        errors.append("Field request.mprn should be numeric.")

    if errors:
        raise RequestValidationException(
            "Request parameters were passed incorrectly. \
                Please see errors field for specific detail.",
            errors,
        )