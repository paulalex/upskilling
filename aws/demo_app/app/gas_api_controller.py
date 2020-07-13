import functools
import jsons

import gas_api_service as service
from gas_api_exception import ApiBaseException, ServerException
from gas_api_validator import validate_mprn_request

@functools.lru_cache(maxsize=128)
def read_mprn(mprn):
    try:
        validate_mprn_request(mprn)

        result = service.read_mprn(mprn)

        response = jsons.dump(result.to_dict())
    except ApiBaseException as base_exception:
        raise base_exception
    except Exception as exception:
        print(exception)

        raise ServerException("The server was unable to process your request.", [])

    return response

@functools.lru_cache(maxsize=128)
def read_supplier(mprn):
    try:
        validate_mprn_request(mprn)
        
        result = service.read_supplier(mprn)

        response = jsons.dump(result.to_dict())
    except ApiBaseException as base_exception:
        raise base_exception
    except Exception as exception:
        print(exception)

        raise ServerException("The server was unable to process your request.", [])

    return response



