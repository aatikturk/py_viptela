def getPnicStats(vmanage, deviceId):
    """
    Get pnic interfaces from device
    
    Parameters:
    deviceId	 (string):	Device IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/csp/pnic?deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getPNICStatsFromDevice(vmanage, deviceId):
    """
    Get pnic stats from device
    
    Parameters:
    deviceId	 (string):	Device IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/csp/pnic/synced?deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getRBACInterface(vmanage, deviceId):
    """
    Get RBAC interfaces from device
    
    Parameters:
    deviceId	 (string):	Device IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/csp/rbac?deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
