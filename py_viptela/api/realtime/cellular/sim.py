def getSimInfo(vmanage, deviceId):
    """
    Get cellular sim info from device
    
    Parameters:
    deviceId	 (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/cellularEiolte/sim?deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
