def getCloudConnector(vmanage):
    """
    Get SD_AVC Cloud Connector Config
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/sdavc/cloudconnector"
    response = vmanage.apiCall("GET", endpoint)
    return response
def disableCloudConnector(vmanage, payload):
    """
    Disable SD_AVC Cloud Connector
    
    Parameters:
    payload:	Request Payload
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/sdavc/cloudconnector"
    response = vmanage.apiCall("PUT", endpoint, payload)
    return response
def enableCloudConnector(vmanage, payload):
    """
    Enable SD_AVC Cloud Connector
    
    Parameters:
    payload:	Request Payload
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/sdavc/cloudconnector"
    response = vmanage.apiCall("POST", endpoint, payload)
    return response
def getCloudConnectorStatus(vmanage):
    """
    Get SD_AVC Cloud Connector Status
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/sdavc/cloudconnector/status"
    response = vmanage.apiCall("GET", endpoint)
    return response
