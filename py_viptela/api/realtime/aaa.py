    
def getServers(vmanage, deviceId):
    """
    Get AAA servers from device (Real Time)
    
    Parameters:
    deviceId	 (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/aaa/servers?deviceId={deviceId}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response
def getUsers(vmanage, deviceId):
    """
    Get AAA users from device (Real Time)
    
    Parameters:
    deviceId	 (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/aaa/users?deviceId={deviceId}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response
def getACLMatchCounterUsers(vmanage, deviceId):
    """
    Get ACL match counters from device (Real Time)
    
    Parameters:
    deviceId	 (string):	Device IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/acl/matchcounter?deviceId={deviceId}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response
def getLoggingFromDevice(vmanage, deviceId):
    """
    Get logging from device (Real Time)
    
    Parameters:
    deviceId	 (string):	Device IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/logging?deviceId={deviceId}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response
def getUnclaimedVedges(vmanage, deviceId):
    """
    Get unclaimed vEdges from vbond
    
    Parameters:
    deviceId	 (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/unclaimed/vedges?deviceId={deviceId}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response
def getUsersFromDevice(vmanage, deviceId):
    """
    Get users from device (Real Time)
    
    Parameters:
    deviceId	 (string):	Device IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/users?deviceId={deviceId}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response
def getAllDeviceUsers(vmanage, deviceId):
    """
    Get all users from device
    
    Parameters:
    deviceId	 (string):	Device IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/users/list?deviceId={deviceId}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response
