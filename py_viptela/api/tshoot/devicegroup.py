def listDeviceGroupList(vmanage):
    """
    Retrieve device group list
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/group"
    response = vmanage.apiCall("GET", endpoint)
    return response
def listDeviceGroups(vmanage):
    """
    Retrieve device groups
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/group/device"
    response = vmanage.apiCall("GET", endpoint)
    return response
def listGroupDevices(vmanage, groupId, ssh, vpnId):
    """
    Retrieve devices in group
    
    Parameters:
    groupId	 (string):	Group Id
	ssh	 (boolean):	SSH
	vpnId	 (array):	VPN Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/group/devices?groupId={groupId}&ssh={ssh}&vpnId={vpnId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def listGroupDevicesForMap(vmanage, groupId, vpnId):
    """
    Retrieve group devices for map
    
    Parameters:
    groupId	 (string):	Group Id
	vpnId	 (array):	VPN Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/group/map/devices?groupId={groupId}&vpnId={vpnId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def listGroupLinksForMap(vmanage, groupId):
    """
    Retrieve devices in group for map
    
    Parameters:
    groupId	 (string):	Group Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/group/map/devices/links?groupId={groupId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
