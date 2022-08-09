def getAllKeys(vmanage):
    """
    Get keys from Umbrella
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/umbrella/getkeys"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getManagementKeys(vmanage):
    """
    Get management keys from Umbrella
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/umbrella/getkeys/management"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getNetworkKeys(vmanage):
    """
    Get network devices keys from Umbrella
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/umbrella/getkeys/networkdevices"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getReportingKeys(vmanage):
    """
    Get reporting keys from Umbrella
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/umbrella/getkeys/reporting"
    response = vmanage.apiCall("GET", endpoint)
    return response
