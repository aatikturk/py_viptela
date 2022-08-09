def getHardwareInfo(vmanage, deviceId):
    """
    Get cellular hardware info from device
    
    Parameters:
    deviceId	 (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/cellularEiolte/hardware?deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
