def getConnections(vmanage, deviceId):
    """
    Get cellular connection list from device
    
    Parameters:
    deviceId	 (string):	Device IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/cellular/connection?deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getHardwareList(vmanage, deviceId):
    """
    Get cellular hardware list from device
    
    Parameters:
    deviceId	 (string):	Device IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/cellular/hardware?deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getModemList(vmanage, policyId):
    """
    Get cellular modem list from device
    
    Parameters:
    policyId	 (string):	Policy IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/cellular/modem?policyId={policyId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getNetworkList(vmanage, deviceId):
    """
    Get cellular network list from device
    
    Parameters:
    deviceId	 (string):	Device IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/cellular/network?deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getProfileList(vmanage, deviceId):
    """
    Get cellular profile list from device
    
    Parameters:
    deviceId	 (string):	Device IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/cellular/profiles?deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getRadioList(vmanage, deviceId):
    """
    Get cellular radio list from device
    
    Parameters:
    deviceId	 (string):	Device IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/cellular/radio?deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getSessionsList(vmanage, ifName, priDns, deviceId):
    """
    Get cellular session list from device
    
    Parameters:
    ifName	 (string):	Interface name
	priDns	 (string):	DNS primary IP
	deviceId	 (string):	Device IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/cellular/sessions?ifName={ifName}&priDns={priDns}&deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getCellularStatusList(vmanage, deviceId):
    """
    Get cellular status list from device
    
    Parameters:
    deviceId	 (string):	Device IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/cellular/status?deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
