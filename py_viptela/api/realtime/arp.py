def getInterface(vmanage, deviceId):
    """
    Get ARP interfaces from device (Real Time)
    
    Parameters:
    deviceId	 (string):	Device IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/arp?deviceId={deviceId}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response
