def getStats(vmanage, deviceId):
    """
    Get tcp proxy statistics from device
    
    Parameters:
    deviceId	 (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/tcpproxy/statistics?deviceId={deviceId}"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response
def getStatus(vmanage, deviceId):
    """
    Get tcp proxy status from device
    
    Parameters:
    deviceId	 (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/tcpproxy/status?deviceId={deviceId}"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response
