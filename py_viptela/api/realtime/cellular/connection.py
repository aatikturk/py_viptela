def getConnInfo(vmanage, deviceId):
    """
    Get cellular connection info from device
    
    Parameters:
    deviceId	 (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/cellularEiolte/connections?deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getRadioInfo(vmanage, deviceId):
    """
    Get cellular radio info from device
    
    Parameters:
    deviceId	 (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/cellularEiolte/radio?deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
