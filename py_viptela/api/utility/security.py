from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

def checkGivenIpList(vmanage, devicedetail):
    """
    Block IP based on list
    
    Parameters:
    devicedetail:	Device detail
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/software/compliance/ip/origin/check"
    response = vmanage.client.apiCall(HttpMethods.POST, endpoint, devicedetail)
    return response
