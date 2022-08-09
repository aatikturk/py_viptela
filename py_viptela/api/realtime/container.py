def getDeviceInfo(vmanage, deviceId):
    """
    Get device container from device (Real Time)
    
    Parameters:
    deviceId	 (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/csp/containers/container?deviceId={deviceId}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response
