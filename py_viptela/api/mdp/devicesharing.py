def getAttached(vmanage, nmsId):
    """
    Retrieve MDP attached devices
    
    Parameters:
    Parameter Description
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/mdp/attachDevices/{nmsId}"
    response = vmanage.apiCall("GET", endpoint)
    return response

def editAttached(vmanage, devicelist, nmsId):
    """
    Edit attached devices
    
    Parameters:
    devicelist:	deviceList
	Parameter Description
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/mdp/attachDevices/{nmsId}"
    response = vmanage.apiCall("PUT", endpoint, devicelist)
    return response

def attach(vmanage, devicelist, nmsId):
    """
    Share devices with MDP
    
    Parameters:
    devicelist:	deviceList
	Parameter Description
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/mdp/attachDevices/{nmsId}"
    response = vmanage.apiCall("POST", endpoint, devicelist)
    return response

def detach(vmanage, devicelist, nmsId):
    """
    Disconnect devices from mpd controller
    
    Parameters:
    devicelist:	deviceList
	Parameter Description
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/mdp/detachDevices/{nmsId}"
    response = vmanage.apiCall("POST", endpoint, devicelist)
    return response

def getSupported(vmanage, nmsId):
    """
    Retrieve MDP supported devices
    
    Parameters:
    Parameter Description
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/mdp/devices/{nmsId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
