def getConnList(vmanage, deviceId):
    """
    Get transport connection list from device
    
    Parameters:
    deviceId	 (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/transport/connection?deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
