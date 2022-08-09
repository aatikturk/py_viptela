def getInterface(vmanage, deviceId):
    """
    Get ARP interfaces from device (Real Time)
    
    Parameters:
    deviceId	 (string):	Device IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/arp?deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
