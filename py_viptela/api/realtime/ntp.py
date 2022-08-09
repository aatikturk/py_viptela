def getAssocs(vmanage, deviceId):
    """
    Get NTP peer associations list from device (Real Time)
    
    Parameters:
    deviceId	 (string):	Device IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/ntp/associations?deviceId={deviceId}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response
def getPeers(vmanage, deviceId):
    """
    Get NTP peer list from device (Real Time)
    
    Parameters:
    deviceId	 (string):	Device IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/ntp/peer?deviceId={deviceId}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response
def getStatus(vmanage, deviceId):
    """
    Get NTP status list from device (Real Time)
    
    Parameters:
    deviceId	 (string):	Device IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/ntp/status?deviceId={deviceId}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response
def getTeList(vmanage, deviceId):
    """
    Get ThousandEyes app list from device
    
    Parameters:
    deviceId	 (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/virtualApplication/te?deviceId={deviceId}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response
def getUtdList(vmanage, deviceId):
    """
    Get Utd apps list from device
    
    Parameters:
    deviceId	 (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/virtualApplication/utd?deviceId={deviceId}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response
def getWaasList(vmanage, deviceId):
    """
    Get Waas apps list from device
    
    Parameters:
    deviceId	 (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/virtualApplication/waas?deviceId={deviceId}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response
