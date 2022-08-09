def getInterfaceList(vmanage, deviceId):
    """
    Get PIM interface list from device
    
    Parameters:
    deviceId	 (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/pim/interface?deviceId={deviceId}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response
def getNeighborList(vmanage, deviceId):
    """
    Get PIM neighbor list from device
    
    Parameters:
    deviceId	 (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/pim/neighbor?deviceId={deviceId}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response
def getRpMappingList(vmanage, deviceId):
    """
    Get PIM Rp-mapping list from device
    
    Parameters:
    deviceId	 (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/pim/rp-mapping?deviceId={deviceId}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response
def getStatsList(vmanage, deviceId):
    """
    Get PIM statistics list from device
    
    Parameters:
    deviceId	 (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/pim/statistics?deviceId={deviceId}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response
def getPPPInterfaceList(vmanage, deviceId):
    """
    Get PPP interface list from device (Real Time)
    
    Parameters:
    deviceId	 (string):	Device IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/ppp/interface?deviceId={deviceId}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response
