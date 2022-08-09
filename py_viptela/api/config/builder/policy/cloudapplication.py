def getCloudDiscoveredApps(vmanage):
    """
    Get all cloud discovered applications
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/policy/clouddiscoveredapp"
    response = vmanage.client.apiCall("GET", endpoint)
    return response
