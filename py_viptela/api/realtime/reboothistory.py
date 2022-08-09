def getList(vmanage, deviceId):
    """
    Get device reboot history
    
    Parameters:
    deviceId	 (string):	Device IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/reboothistory?deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getDetails(vmanage):
    """
    Get detailed reboot history list
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/reboothistory/details"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getSyncedList(vmanage, deviceId):
    """
    Get device reboot history synchronously
    
    Parameters:
    deviceId	 (string):	Device IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/reboothistory/synced?deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
