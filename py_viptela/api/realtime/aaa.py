    
def getServers(vmanage, deviceId):
    """
    Get AAA servers from device (Real Time)
    
    Parameters:
    deviceId	 (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/aaa/servers?deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getUsers(vmanage, deviceId):
    """
    Get AAA users from device (Real Time)
    
    Parameters:
    deviceId	 (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/aaa/users?deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getACLMatchCounterUsers(vmanage, deviceId):
    """
    Get ACL match counters from device (Real Time)
    
    Parameters:
    deviceId	 (string):	Device IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/acl/matchcounter?deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getLoggingFromDevice(vmanage, deviceId):
    """
    Get logging from device (Real Time)
    
    Parameters:
    deviceId	 (string):	Device IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/logging?deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getUnclaimedVedges(vmanage, deviceId):
    """
    Get unclaimed vEdges from vbond
    
    Parameters:
    deviceId	 (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/unclaimed/vedges?deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getUsersFromDevice(vmanage, deviceId):
    """
    Get users from device (Real Time)
    
    Parameters:
    deviceId	 (string):	Device IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/users?deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getAllDeviceUsers(vmanage, deviceId):
    """
    Get all users from device
    
    Parameters:
    deviceId	 (string):	Device IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/users/list?deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
