def getPolicedInterface(vmanage, deviceId):
    """
    Get policed interface list from device
    
    Parameters:
    deviceId	 (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/policer?deviceId={deviceId}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response
