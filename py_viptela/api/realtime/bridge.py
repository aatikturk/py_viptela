def getInterfaces(vmanage, deviceId):
    """
    Get device bridge interface list (Real Time)
    
    Parameters:
    deviceId	 (string):	Device IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/bridge/interface?deviceId={deviceId}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response
def getInterfaceMac(vmanage, bridgeId, ifName, macAddr, deviceId):
    """
    Get device bridge interface MAC (Real Time)
    
    Parameters:
    bridgeId	 (string):	Bridge ID
	ifName	 (string):	Interface name
	macAddr	 (string):	MAC address
	deviceId	 (string):	Device IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/bridge/mac?bridgeId={bridgeId}&ifName={ifName}&macAddr={macAddr}&deviceId={deviceId}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response
def getBridgeInterfaceTable(vmanage, deviceId):
    """
    Get device bridge interface table (Real Time)
    
    Parameters:
    deviceId	 (string):	Device IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/bridge/table?deviceId={deviceId}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response
