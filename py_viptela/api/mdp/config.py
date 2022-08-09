def getConfig(vmanage, deviceId):
    """
    Retrieve MDP ConfigObject
    
    Parameters:
    Parameter Description
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/mdp/policies/mdpconfig/{deviceId}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response
