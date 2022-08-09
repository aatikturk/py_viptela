def getAllocInfo(vmanage, deviceId):
    """
    Get NetworkHub CPU allocation info from device
    
    Parameters:
    deviceId	 (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/csp/resources/cpu-info/allocation?deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getCPUInfo(vmanage, deviceId):
    """
    Get NetworkHub CPU info from device
    
    Parameters:
    deviceId	 (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/csp/resources/cpu-info/cpus?deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getVNFInfo(vmanage, deviceId):
    """
    Get NetworkHub CPU VNF info from device
    
    Parameters:
    deviceId	 (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/csp/resources/cpu-info/vnfs?deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
