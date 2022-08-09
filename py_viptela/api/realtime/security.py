def getSessionList(vmanage, deviceId):
    """
    Get security information from devices
    
    Parameters:
    deviceId	 (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/security/information?deviceId={deviceId}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response
