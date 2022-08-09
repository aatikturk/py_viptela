from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

def invalidateDevice(vmanage, devInfo):
    """
    invalidate the device
    
    Parameters:
    devInfo:	vEdge device info
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/certificate/device/invalidate"
    response = vmanage.client.apiCall(HttpMethods.POST, endpoint, devInfo)
    return response
def stageDevice(vmanage, devInfo):
    """
    Stop data traffic to device
    
    Parameters:
    devInfo:	vEdge device info
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/certificate/device/stage"
    response = vmanage.client.apiCall(HttpMethods.POST, endpoint, devInfo)
    return response
def createAdminTech(vmanage, request):
    """
    Generate admin tech logs
    
    Parameters:
    request:	Admin tech generation request
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/tools/admintech"
    response = vmanage.client.apiCall(HttpMethods.POST, endpoint, request)
    return response
def copyAdminTechOnDevice(vmanage, request):
    """
    copy admin tech logs
    
    Parameters:
    request:	Admin tech copy request
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/tools/admintech/copy"
    response = vmanage.client.apiCall(HttpMethods.POST, endpoint, request)
    return response
def deleteAdminTechOnDevice(vmanage, request):
    """
    delete admin tech logs
    
    Parameters:
    request:	Admin tech copy request
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/tools/admintech/delete"
    response = vmanage.client.apiCall(HttpMethods.DELETE, endpoint, request)
    return response
def downloadAdminTechFile(vmanage, filename):
    """
    Download admin tech logs
    
    Parameters:
    filename	 (string):	Admin tech file
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/tools/admintech/download/{filename}"
    response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
    return response
def deleteAdminTechFile(vmanage, requestID):
    """
    Delete admin tech logs
    
    Parameters:
    requestID	 (string):	Request Id of admin tech generation request
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/tools/admintech/{requestID}"
    response = vmanage.client.apiCall(HttpMethods.DELETE, endpoint)
    return response
def listAdminTechsOnDevice(vmanage, request):
    """
    List admin tech logs
    
    Parameters:
    request:	Admin tech listing request
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/tools/admintechlist"
    response = vmanage.client.apiCall(HttpMethods.POST, endpoint, request)
    return response
def listAdminTechs(vmanage):
    """
    Get device admin-tech information
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/tools/admintechs"
    response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
    return response
def getInProgressCount(vmanage):
    """
    Get device admin-tech InProgressCount
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/tools/admintechs/inprogress"
    response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
    return response
def factoryReset(vmanage, payload):
    """
    Device factory reset
    
    Parameters:
    payload:	Device factory reset
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/tools/factoryreset"
    response = vmanage.client.apiCall(HttpMethods.POST, endpoint, payload)
    return response
def npingDevice(vmanage, npingparameter, deviceIP):
    """
    NPing device
    
    Parameters:
    npingparameter:	NPing parameter
	deviceIP	 (string):	Device IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/tools/nping/{deviceIP}"
    response = vmanage.client.apiCall(HttpMethods.POST, endpoint, npingparameter)
    return response
def pingDevice(vmanage, pingparameter, deviceIP):
    """
    Ping device
    
    Parameters:
    pingparameter:	Ping parameter
	deviceIP	 (string):	Device IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/tools/ping/{deviceIP}"
    response = vmanage.client.apiCall(HttpMethods.POST, endpoint, pingparameter)
    return response
def processPortHopColor(vmanage, deviceporthopcolor, deviceIP):
    """
    Request port hop color
    
    Parameters:
    deviceporthopcolor:	Device port hop color
	deviceIP	 (string):	Device IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/tools/porthopcolor/{deviceIP}"
    response = vmanage.client.apiCall(HttpMethods.POST, endpoint, deviceporthopcolor)
    return response
def processInterfaceReset(vmanage, deviceinterface, deviceIP):
    """
    Reset device interface
    
    Parameters:
    deviceinterface:	Device interface
	deviceIP	 (string):	Device IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/tools/reset/interface/{deviceIP}"
    response = vmanage.client.apiCall(HttpMethods.POST, endpoint, deviceinterface)
    return response
def processResetUser(vmanage, deviceuserreset, deviceIP):
    """
    Request reset user
    
    Parameters:
    deviceuserreset:	Device user reset
	deviceIP	 (string):	Device IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/tools/resetuser/{deviceIP}"
    response = vmanage.client.apiCall(HttpMethods.POST, endpoint, deviceuserreset)
    return response
def servicePath(vmanage, servicepathparameter, deviceIP):
    """
    Service path
    
    Parameters:
    servicepathparameter:	Service path parameter
	deviceIP	 (string):	Device IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/tools/servicepath/{deviceIP}"
    response = vmanage.client.apiCall(HttpMethods.POST, endpoint, servicepathparameter)
    return response
def tracerouteDevice(vmanage, tracerouteparameter, deviceIP):
    """
    Traceroute
    
    Parameters:
    tracerouteparameter:	Traceroute parameter
	deviceIP	 (string):	Device IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/tools/traceroute/{deviceIP}"
    response = vmanage.client.apiCall(HttpMethods.POST, endpoint, tracerouteparameter)
    return response
def tunnelPath(vmanage, tunnelpathparameter, deviceIP):
    """
    TunnelPath
    
    Parameters:
    tunnelpathparameter:	TunnelPath parameter
	deviceIP	 (string):	Device IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/tools/tunnelpath/{deviceIP}"
    response = vmanage.client.apiCall(HttpMethods.POST, endpoint, tunnelpathparameter)
    return response
def getControlConnections(vmanage, uuid):
    """
    Troubleshoot control connections
    
    Parameters:
    uuid	 (string):	Device uuid
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/troubleshooting/control/{uuid}"
    response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
    return response
def getDeviceConfiguration(vmanage, uuid):
    """
    Debug device bring up
    
    Parameters:
    uuid	 (string):	Device uuid
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/troubleshooting/devicebringup?uuid={uuid}"
    response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
    return response
