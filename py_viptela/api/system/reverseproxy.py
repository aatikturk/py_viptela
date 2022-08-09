def get(vmanage, uuid):
    """
    Get reverse proxy IP/Port mappings for controller
    
    Parameters:
    uuid	 (string):	Device uuid
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/system/reverseproxy/{uuid}"
    response = vmanage.apiCall("GET", endpoint)
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
    
    endpoint = f"dataservice/system/reverseproxy/{uuid}"
    response = vmanage.apiCall("POST", endpoint, mapping)
    return response
