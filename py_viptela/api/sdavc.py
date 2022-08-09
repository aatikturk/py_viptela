def getCloudConnector(vmanage):
    """
    Get SD_AVC Cloud Connector Config
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/sdavc/cloudconnector"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response
def disableCloudConnector(vmanage, payload):
    """
    Disable SD_AVC Cloud Connector
    
    Parameters:
    payload:	Request Payload
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/sdavc/cloudconnector"
    response = vmanage.client.apiCall(vmanage.PUT, endpoint, payload)
    return response
def enableCloudConnector(vmanage, payload):
    """
    Enable SD_AVC Cloud Connector
    
    Parameters:
    payload:	Request Payload
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/sdavc/cloudconnector"
    response = vmanage.client.apiCall(vmanage.POST, endpoint, payload)
    return response
def getCloudConnectorStatus(vmanage):
    """
    Get SD_AVC Cloud Connector Status
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/sdavc/cloudconnector/status"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response
