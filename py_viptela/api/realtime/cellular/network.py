def getNetworkInfo(vmanage, deviceId):
    """
    Get cellular network  info from device
    
    Parameters:
    deviceId	 (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/cellularEiolte/network?deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
