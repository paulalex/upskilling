import requests
import json
import os
from requests.exceptions import HTTPError

from gas_api_model import Mprn, Supplier
from gas_api_exception import ServerException, MprnNotFoundException

SHIPPER_API = "https://xoserve.apimanagement.hana.ondemand.com:443/v1/Shipper.svc?"
SUPPLIER_API = "https://xoserve.apimanagement.hana.ondemand.com:443/v3/Supplier.svc?"
API_KEY = os.environ["API_KEY"]

def read_mprn(mprn):
    try:        
        mprn_response = requests.get(
            SHIPPER_API,
            params={"mprn": mprn},
            headers={
            "Content-Type": "application/json",
            "APIKey": API_KEY
            }
        )
        
        mprn_response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
        
        raise ServerException("The server was unable to process your request.", [])
    except Exception as err:
        print(f'Other error occurred: {err}')
        
        raise ServerException("The server was unable to process your request.", [])
    else:
        check_for_api_exception_and_raise(mprn_response)

        shipper_response = shipper_response.json().get("mprn")
    
        mprn = Mprn.from_json(json.dumps(shipper_response))

        return mprn

def read_supplier(mprn):
    try:     
        supplier_response = requests.get(
            SUPPLIER_API,
            params={"mprn": mprn},
            headers={
            "Content-Type": "application/json",
            "APIKey": API_KEY
            }
        )       
       
        supplier_response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')

        raise ServerException("The server was unable to process your request.", [])
    except Exception as err:
        print(f'Other error occurred: {err}')

        raise ServerException("The server was unable to process your request.", [])
    else:
        check_for_api_exception_and_raise(supplier_response)

        supplier_response = supplier_response.json().get("supplier")
        
        supplier = Supplier.from_json(json.dumps(supplier_response))

        return supplier

def check_for_api_exception_and_raise(supplier_response):
    fault = supplier_response.json().get("fault")

    if fault:
        fault_string = fault.get("faultstring")

        fault_detail = fault.get("detail").get("errorcode")

        raise MprnNotFoundException(fault_string, [f"Code: {fault_detail}"])



