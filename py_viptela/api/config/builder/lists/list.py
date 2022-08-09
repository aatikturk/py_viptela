def getAll(vmanage):
    """
    Get all policy lists
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/template/policy/list"
    response = vmanage.apiCall("GET", endpoint)
    return response
