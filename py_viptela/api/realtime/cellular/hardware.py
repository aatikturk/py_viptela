def getHardwareInfo(vmanage, deviceId):
    """
    Get cellular hardware info from device
    
    Parameters:
    deviceId	 (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/cellularEiolte/hardware?deviceId={deviceId}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response
