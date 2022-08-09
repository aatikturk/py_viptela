def getInterfaceList(vmanage, deviceId):
    """
    Get PPPoE session list from device
    
    Parameters:
    Parameter Description
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/pppoe/session?deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getNeighborList(vmanage, deviceId):
    """
    Get PPPoE statistics from device
    
    Parameters:
    Parameter Description
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/pppoe/statistic?deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
