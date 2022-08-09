def getUmbrella(vmanage, deviceId):
    """
    Get SIG Umbrella tunnels from device
    
    Parameters:
    deviceId	 (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/sig/umbrella/tunnels?deviceId={deviceId}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response
def getZscaler(vmanage, deviceId):
    """
    Get SIG Zscaler tunnels from device
    
    Parameters:
    deviceId	 (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/sig/zscaler/tunnels?deviceId={deviceId}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response
