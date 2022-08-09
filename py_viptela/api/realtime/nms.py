def getRunning(vmanage, deviceId):
    """
    Get nms running state from device
    
    Parameters:
    deviceId	 (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/nms/running?deviceId={deviceId}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response
