def getRunning(vmanage, deviceId):
    """
    Get nms running state from device
    
    Parameters:
    deviceId	 (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/nms/running?deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
