def getDetailById(vmanage, clusterId):
    """
    Provide details of ids of existing clusters
    
    Parameters:
    clusterId	 (string):	Cluster Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/colocation/monitor/cluster?clusterId={clusterId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getConfigById(vmanage, clusterId):
    """
    Provide details of devices of clusters
    
    Parameters:
    clusterId	 (string):	Cluster Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/colocation/monitor/cluster/config?clusterId={clusterId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getPortMappingById(vmanage, clusterId):
    """
    Provide details of port mappings in the cluster
    
    Parameters:
    clusterId	 (string):	Cluster Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/colocation/monitor/cluster/portView?clusterId={clusterId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getDeviceDetailById(vmanage, deviceId):
    """
    List details for Device
    
    Parameters:
    deviceId	 (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/colocation/monitor/device?deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getSystemStatusById(vmanage, deviceId):
    """
    List all connected VNF to a device
    
    Parameters:
    deviceId	 (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/colocation/monitor/device/system?deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getvnfById(vmanage, deviceId):
    """
    List all VNF attached with Device
    
    Parameters:
    deviceId	 (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/colocation/monitor/device/vnf?deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def listNetworkFunctionMap(vmanage):
    """
    Retrieve network function listing
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/colocation/monitor/networkfunction/listmap"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getpnfDetails(vmanage, clusterId):
    """
    List all PNF by cluster Id
    
    Parameters:
    clusterId	 (string):	Cluster Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/colocation/monitor/pnf?clusterId={clusterId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getPNFConfig(vmanage, pnfSerialNumber, clusterId):
    """
    List configuration of PNF
    
    Parameters:
    pnfSerialNumber	 (string):	PNF serial number
	clusterId	 (string):	Cluster Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/colocation/monitor/pnf/configuration?pnfSerialNumber={pnfSerialNumber}&clusterId={clusterId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getServiceChainDetails(vmanage, clusterId, userGroupName):
    """
    List all service chain or service chains by Id
    
    Parameters:
    clusterId	 (string):	Cluster Id
	userGroupName	 (string):	UserGroup Name
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/colocation/monitor/servicechain?clusterId={clusterId}&userGroupName={userGroupName}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getServiceGroupById(vmanage, clusterId):
    """
    List all attached serviceGroups to cluster
    
    Parameters:
    clusterId	 (string):	Cluster Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/colocation/monitor/servicegroup?clusterId={clusterId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getvnfDetails(vmanage, clusterId, userGroupName):
    """
    Provide details of all existing VNF
    
    Parameters:
    clusterId	 (string):	Cluster Id
	userGroupName	 (string):	UserGroup Name
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/colocation/monitor/vnf?clusterId={clusterId}&userGroupName={userGroupName}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def vnfActions(vmanage, vmName, deviceId, action):
    """
    VNF action
    
    Parameters:
    vmName	 (string):	VM Name
	deviceId	 (string):	Device Id
	action	 (string):	Action
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/colocation/monitor/vnf/action?vmName={vmName}&deviceId={deviceId}&action={action}"
    response = vmanage.apiCall("POST", endpoint)
    return response
def getVNFEventsCountDetail(vmanage, user_group):
    """
    Get event detail of VNF
    
    Parameters:
    user_group	 (string):	user group name
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/colocation/monitor/vnf/alarms?user_group={user_group}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getVNFAlarmCount(vmanage, user_group):
    """
    Get event detail of VNF
    
    Parameters:
    user_group	 (string):	user group name
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/colocation/monitor/vnf/alarms/count?user_group={user_group}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getVNFEventsDetail(vmanage, vnfName):
    """
    Get event detail of VNF
    
    Parameters:
    vnfName	 (string):	VNF name
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/colocation/monitor/vnf/events?vnfName={vnfName}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getVNFInterfaceDetail(vmanage, vnfName, deviceIp, deviceClass):
    """
    Get interface detail of VNF
    
    Parameters:
    vnfName	 (string):	VNF name
	deviceIp	 (string):	Device IP
	deviceClass	 (string):	Device class
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/colocation/monitor/vnf/interface?vnfName={vnfName}&deviceIp={deviceIp}&deviceClass={deviceClass}"
    response = vmanage.apiCall("GET", endpoint)
    return response
