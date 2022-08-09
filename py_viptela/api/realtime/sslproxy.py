def getStats(vmanage, deviceId):
    """
    Get ssl proxy statistics from device
    
    Parameters:
    deviceId	 (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/sslproxy/statistics?deviceId={deviceId}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response
def getStatus(vmanage, deviceId):
    """
    Get ssl proxy status from device
    
    Parameters:
    deviceId	 (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/sslproxy/status?deviceId={deviceId}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response
