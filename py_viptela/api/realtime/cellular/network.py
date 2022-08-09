def getNetworkInfo(vmanage, deviceId):
    """
    Get cellular network  info from device
    
    Parameters:
    deviceId	 (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/cellularEiolte/network?deviceId={deviceId}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response
