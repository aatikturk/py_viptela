from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

def get(vmanage, uuid):
    """
    Get reverse proxy IP/Port mappings for controller
    
    Parameters:
    uuid	 (string):	Device uuid
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/system/reverseproxy/{uuid}"
    response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
    return response
def create(vmanage, mapping, uuid):
    """
    Create reverse proxy IP/Port mappings for controller
    
    Parameters:
    mapping:	Device reverse proxy mappings
	uuid	 (string):	Device uuid
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/system/reverseproxy/{uuid}"
    response = vmanage.client.apiCall(HttpMethods.POST, endpoint, mapping)
    return response
