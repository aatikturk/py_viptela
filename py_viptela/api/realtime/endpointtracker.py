def getInfo(vmanage, deviceId):
    """
    Get endpoint tracker info from device
    
    Parameters:
    deviceId	 (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/endpointTracker?deviceId={deviceId}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response
