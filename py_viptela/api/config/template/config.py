def uploadConfig(vmanage, templateconfig, deviceId):
    """
    Upload device config
    
    Parameters:
    templateconfig:	Template config
	deviceId	 (string):	Device Model ID
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/template/config/attach/{deviceId}"
    response = vmanage.apiCall("PUT", endpoint, templateconfig)
    return response

def getAttached(vmanage, deviceId, type):
    """
    Get local template attached config for given device
    
    Parameters:
    deviceId	 (string):	Device Model ID
	type	 (string):	Config type
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/template/config/attached/{deviceId}?type={type}"
    response = vmanage.apiCall("GET", endpoint)
    return response

def getCLIModeDevices(vmanage, type):
    """
    Generates a JSON object that contains a list of valid devices in CLI mode
    
    Parameters:
    type	 (string):	Device type
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/template/config/device/mode/cli?type={type}"
    response = vmanage.apiCall("GET", endpoint)
    return response

def updateToCLI(vmanage, devicelist):
    """
    Given a JSON list of devices not managed by any third member partners, push to devices from a CLI template
    
    Parameters:
    devicelist:	Device list
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/template/config/device/mode/cli"
    response = vmanage.apiCall("POST", endpoint, devicelist)
    return response

def getvManageModeDevices(vmanage, type):
    """
    Get list of devices that are allowable for vmanage modes
    
    Parameters:
    type	 (string):	Device type
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/template/config/device/mode/vmanage?type={type}"
    response = vmanage.apiCall("GET", endpoint)
    return response

def getDeviceDiff(vmanage, deviceId):
    """
    Generates a JSON object that contains the diff for a given device
    
    Parameters:
    deviceId	 (string):	Device Model ID
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/template/config/diff/{deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response

def getCompatibleDevices(vmanage, oldDeviceId):
    """
    Get compatible devices of model, chassis number, certificate serial number with the old device
    
    Parameters:
    oldDeviceId	 (string):	Device Model ID
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/template/config/rmalist/{oldDeviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response

def rmaUpdate(vmanage, templateconfig):
    """
    Update new device
    
    Parameters:
    templateconfig:	Template config
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/template/config/rmaupdate"
    response = vmanage.apiCall("PUT", endpoint, templateconfig)
    return response

def getRunningConfig(vmanage, deviceId):
    """
    Get device running config
    
    Parameters:
    deviceId	 (string):	Device Model ID
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/template/config/running/{deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response

def getVpnForDevice(vmanage, deviceId):
    """
    Get list of configured VPN (excluding reserved VPN) for a device
    
    Parameters:
    deviceId	 (string):	Device Model ID
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/template/config/vpn/{deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
