def getList(vmanage, deviceId):
    """
    Get feature lists from device (Real Time)
    
    Parameters:
    deviceId	 (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/featurelist?deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getSyncedList(vmanage, deviceId):
    """
    Get feature lists synchronously from device
    
    Parameters:
    deviceId	 (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/featurelist/synced?deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
