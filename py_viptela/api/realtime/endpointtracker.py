def getInfo(vmanage, deviceId):
    """
    Get endpoint tracker info from device
    
    Parameters:
    deviceId	 (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/endpointTracker?deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
