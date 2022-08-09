def getCloudDiscoveredApps(vmanage):
    """
    Get all cloud discovered applications
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/template/policy/clouddiscoveredapp"
    response = vmanage.apiCall("GET", endpoint)
    return response
