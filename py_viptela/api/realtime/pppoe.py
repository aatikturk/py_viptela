def getInterfaceList(vmanage, deviceId):
    """
    Get PPPoE session list from device
    
    Parameters:
    Parameter Description
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/pppoe/session?deviceId={deviceId}"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response
def getNeighborList(vmanage, deviceId):
    """
    Get PPPoE statistics from device
    
    Parameters:
    Parameter Description
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/pppoe/statistic?deviceId={deviceId}"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response
