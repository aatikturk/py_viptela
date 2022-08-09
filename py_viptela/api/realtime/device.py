def getV6Data(vmanage, deviceId):
    """
    Get ipv6 data from device
    
    Parameters:
    Parameter Description
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/ipv6/nd6?deviceId={deviceId}"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response
