def createServerInfo(vmanage):
    """
    Get Server info
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/server/info"
    response = vmanage.apiCall("GET", endpoint)
    return response
