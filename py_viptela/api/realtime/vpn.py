def getVPNInstances(vmanage, deviceId):
    """
    Get VPN instance list from device (Real Time)
    
    Parameters:
    deviceId	 (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/vpn?deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
