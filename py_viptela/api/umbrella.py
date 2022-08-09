def getAllKeys(vmanage):
    """
    Get keys from Umbrella
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/umbrella/getkeys"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response
def getManagementKeys(vmanage):
    """
    Get management keys from Umbrella
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/umbrella/getkeys/management"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response
def getNetworkKeys(vmanage):
    """
    Get network devices keys from Umbrella
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/umbrella/getkeys/networkdevices"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response
def getReportingKeys(vmanage):
    """
    Get reporting keys from Umbrella
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/umbrella/getkeys/reporting"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response
