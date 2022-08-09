def getEvalInfo(vmanage, deviceId):
    """
    Get license evaluation info from device
    
    Parameters:
    deviceId	 (string):	Device IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/license/evaluation?deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getPAKInfo(vmanage, deviceId):
    """
    Get license pak info from device
    
    Parameters:
    deviceId	 (string):	Device IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/license/pak?deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getPrivacyInfo(vmanage, deviceId):
    """
    Get license privacy info from device
    
    Parameters:
    deviceId	 (string):	Device IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/license/privacy?deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getRegInfo(vmanage, deviceId):
    """
    Get license registration info from device
    
    Parameters:
    deviceId	 (string):	Device IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/license/registration?deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getUDIInfo(vmanage, deviceId):
    """
    Get license UDI info from device
    
    Parameters:
    deviceId	 (string):	Device IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/license/udi?deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getUsageInfo(vmanage, deviceId):
    """
    Get license usage info from device
    
    Parameters:
    deviceId	 (string):	Device IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/license/usage?deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
