def getConfig(vmanage, deviceId):
    """
    Retrieve MDP ConfigObject
    
    Parameters:
    Parameter Description
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/mdp/policies/mdpconfig/{deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
