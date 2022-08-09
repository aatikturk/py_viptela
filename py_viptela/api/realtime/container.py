def getDeviceInfo(vmanage, deviceId):
    """
    Get device container from device (Real Time)
    
    Parameters:
    deviceId	 (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/csp/containers/container?deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
