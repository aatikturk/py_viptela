def getConnList(vmanage, deviceId):
    """
    Get transport connection list from device
    
    Parameters:
    deviceId	 (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/transport/connection?deviceId={deviceId}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response
