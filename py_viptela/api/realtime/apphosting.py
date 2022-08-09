def getAttached(vmanage, deviceId):
    """
    Get App hosting attached device from device
    
    Parameters:
    deviceId	 (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/app-hosting/attached-devices?deviceId={deviceId}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response
def getDetails(vmanage, deviceId):
    """
    Get App hosting details from device
    
    Parameters:
    deviceId	 (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/app-hosting/details?deviceId={deviceId}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response
def getGuestRoutes(vmanage, deviceId):
    """
    Get App hosting guest routes from device
    
    Parameters:
    deviceId	 (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/app-hosting/guest-routes?deviceId={deviceId}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response
def getNetworkDevices(vmanage, deviceId):
    """
    Get App hosting network interface from device
    
    Parameters:
    deviceId	 (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/app-hosting/network-interfaces?deviceId={deviceId}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response
def getNetworkUtils(vmanage, deviceId):
    """
    Get App hosting network utilization from device
    
    Parameters:
    deviceId	 (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/app-hosting/network-utilization?deviceId={deviceId}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response
def getProcesses(vmanage, deviceId):
    """
    Get App hosting processes from device
    
    Parameters:
    deviceId	 (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/app-hosting/processes?deviceId={deviceId}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response
def getStorageUtils(vmanage, deviceId):
    """
    Get App hosting storage utilization from device
    
    Parameters:
    deviceId	 (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/app-hosting/storage-utilization?deviceId={deviceId}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response
def getUtilization(vmanage, deviceId):
    """
    Get App hosting utilization from device
    
    Parameters:
    deviceId	 (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/app-hosting/utilization?deviceId={deviceId}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response
