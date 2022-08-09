def disconnect(vmanage, nmsId):
    """
    disconnect from mpd controller
    
    Parameters:
    Parameter Description
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/mdp/disconnect/{nmsId}"
    response = vmanage.apiCall("GET", endpoint)
    return response

def offboard(vmanage, nmsId):
    """
    offboard the mdp application
    
    Parameters:
    Parameter Description
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/mdp/onboard/{nmsId}"
    response = vmanage.apiCall("DELETE", endpoint)
    return response
