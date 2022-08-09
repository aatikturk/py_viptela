def getGlobalDropStats(vmanage, deviceId):
    """
    Get SD-WAN global drop statistics detail from device (Real Time)
    
    Parameters:
    deviceId	 (string):	Device IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/sdwan-global-drop-statistics?deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getStats(vmanage, deviceId):
    """
    Get SD-WAN statistics detail from device (Real Time)
    
    Parameters:
    deviceId	 (string):	Device IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/sdwan-stats?deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
