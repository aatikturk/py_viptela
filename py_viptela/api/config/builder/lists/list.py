from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

def getAll(vmanage):
    """
    Get all policy lists
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/policy/list"
    response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
    return response
