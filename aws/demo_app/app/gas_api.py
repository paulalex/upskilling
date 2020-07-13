# 8910387400
# 9108299602
# 9108300908
# 9309082102
# 15799600
# 6686900
import gas_api_controller as controller

def read_mprn(event, context):
    mprn = event.get("mprn")

    return controller.read_mprn(mprn)

def read_supplier(event, context):
    mprn = event.get("mprn")
    
    return controller.read_supplier(mprn)



