def getDetail(vmanage, ifname, deviceId):
    """
    Get SFP detail
    
    Parameters:
    ifname	 (string):	IF Name
	deviceId	 (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/sfp/detail?ifname={ifname}&deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getDiag(vmanage, ifname, deviceId):
    """
    Get SFP diagnostic
    
    Parameters:
    ifname	 (string):	IF Name
	deviceId	 (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/sfp/diagnostic?ifname={ifname}&deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getDiagAlarm(vmanage, ifname, deviceId):
    """
    Get SFP diagnostic measurement alarm
    
    Parameters:
    ifname	 (string):	IF Name
	deviceId	 (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/sfp/diagnosticMeasurementAlarm?ifname={ifname}&deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getDiagValue(vmanage, ifname, deviceId):
    """
    Get SFP diagnostic measurement value
    
    Parameters:
    ifname	 (string):	IF Name
	deviceId	 (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/sfp/diagnosticMeasurementValue?ifname={ifname}&deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
