from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

def getCloudConnector(vmanage):
    """
    Get SD_AVC Cloud Connector Config
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/sdavc/cloudconnector"
    response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
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
    response = vmanage.client.apiCall(HttpMethods.PUT, endpoint, payload)
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
    response = vmanage.client.apiCall(HttpMethods.POST, endpoint, payload)
    return response
def getCloudConnectorStatus(vmanage):
    """
    Get SD_AVC Cloud Connector Status
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/sdavc/cloudconnector/status"
    response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
    return response
