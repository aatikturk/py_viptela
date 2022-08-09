def getMpDatabase(vmanage, deviceId):
    """
    Get mp database from device
    
    Parameters:
    deviceId	 (string):	Device IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/cfm/mp/database?deviceId={deviceId}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response
def getMpLocalMep(vmanage, domain, service, mepId, deviceId):
    """
    Get mp local mep from device
    
    Parameters:
    domain	 (string):	Domain Name
	service	 (string):	Service Name
	mepId	 (number):	MEP ID
	deviceId	 (string):	Device IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/cfm/mp/local/mep?domain={domain}&service={service}&mepId={mepId}&deviceId={deviceId}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response
def getMpLocalMip(vmanage, level, port, svcInst, deviceId):
    """
    Get mp local mip from device
    
    Parameters:
    level	 (number):	Level
	port	 (string):	Port
	svcInst	 (number):	Service Instance
	deviceId	 (string):	Device IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/cfm/mp/local/mip?level={level}&port={port}&svcInst={svcInst}&deviceId={deviceId}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response
def getMpRemoteMep(vmanage, domain, service, locMepId, remMepId, deviceId):
    """
    Get mp remote mep from device
    
    Parameters:
    domain	 (string):	Domain Name
	service	 (string):	Service Name
	locMepId	 (number):	Local MEP ID
	remMepId	 (number):	Remote MEP ID
	deviceId	 (string):	Device IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/cfm/mp/remotemep?domain={domain}&service={service}&locMepId={locMepId}&remMepId={remMepId}&deviceId={deviceId}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response
