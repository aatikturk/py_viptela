def getSessionList(vmanage, deviceId):
    """
    Get security information from devices
    
    Parameters:
    deviceId	 (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/security/information?deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
