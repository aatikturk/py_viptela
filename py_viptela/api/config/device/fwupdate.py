def get(vmanage):
    """
    Get list of firmware images in the repository
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/action/firmware"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response

def process(vmanage):
    """
    Upload firmware image package
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/action/firmware"
    response = vmanage.client.apiCall(vmanage.POST, endpoint)
    return response

def activate(vmanage, fwInfo):
    """
    Activate firmware on device
    
    Parameters:
    fwInfo:    Firmware Info
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/action/firmware/activate"
    response = vmanage.client.apiCall(vmanage.POST, endpoint, fwInfo)
    return response

def getDevicesFWUpgrade(vmanage):
    """
    Get list of devices that support firmware upgrade
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/action/firmware/devices"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response

def install(vmanage, fwInfo):
    """
    Install firmware on device
    
    Parameters:
    fwInfo:    Firmware Info
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/action/firmware/install"
    response = vmanage.client.apiCall(vmanage.POST, endpoint, fwInfo)
    return response

def remove(vmanage, fwInfo):
    """
    Remove firmware on device
    
    Parameters:
    fwInfo:    Firmware Info
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/action/firmware/remove"
    response = vmanage.client.apiCall(vmanage.POST, endpoint, fwInfo)
    return response

def getDetails(vmanage, versionId):
    """
    Get firmware image details for a given version
    
    Parameters:
    versionId	 (string):	Firmware image version
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/action/firmware/{versionId}"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response

def delete(vmanage, versionId):
    """
    Delete firmware image package
    
    Parameters:
    versionId	 (string):	Firmware image version
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/action/firmware/{versionId}"
    response = vmanage.client.apiCall(vmanage.DELETE, endpoint)
    return response
