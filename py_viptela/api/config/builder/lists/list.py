def getAll(vmanage):
    """
    Get all policy lists
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/policy/list"
    response = vmanage.client.apiCall("GET", endpoint)
    return response
