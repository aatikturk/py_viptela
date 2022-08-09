def getDPIDeviceFieldJSON(vmanage, isDeviceDashBoard):
    """
    Get DPI query field from device
    
    Parameters:
    isDeviceDashBoard	 (boolean):	Flag whether is device dashboard request
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/dpi/application/fields?isDeviceDashBoard={isDeviceDashBoard}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def createDPICollectorList(vmanage, vpnId, application, family, deviceId):
    """
    Get DPI applications from device (Real Time)
    
    Parameters:
    vpnId	 (string):	VPN Id
	application	 (string):	Application
	family	 (string):	Family
	deviceId	 (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/dpi/applications?vpn-id={vpnId}&application={application}&family={family}&deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getCommonAppList(vmanage):
    """
    Get DPI common application list from device
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/dpi/common/applications"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getDPIFieldJSON(vmanage):
    """
    Get DPI field from device
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/dpi/device/fields"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getDPIDeviceDetailsFieldJSON(vmanage):
    """
    Get DPI detailed field from device
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/dpi/devicedetails/fields"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getDPIFlowsList(vmanage, vpnId, ip, application, family, deviceId):
    """
    Get DPI flow list from device (Real Time)
    
    Parameters:
    vpnId	            (string):	VPN Id
	ip	                (string):	Source IP
	application	        (string):	Application
	family	            (string):	Family
	deviceId	        (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/dpi/flows?vpn-id={vpnId}&src-ip={ip}&application={application}&family={family}&deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getQosmosAppList(vmanage):
    """
    Get DPI QoSMos application list from device
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/dpi/qosmos/applications"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getDPISummaryRealTime(vmanage, deviceId):
    """
    Get DPI summary from device (Real Time)
    
    Parameters:
    deviceId	 (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/dpi/summary?deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getDPIStatistics(vmanage, application, family, deviceId):
    """
    Get supported applications from device (Real Time)
    
    Parameters:
    application	 (string):	Application
	family	 (string):	Family
	deviceId	 (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/dpi/supported-applications?application={application}&family={family}&deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response