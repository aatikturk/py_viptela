def generateChangePartitionInfo(vmanage, deviceId):
    """
    Get change partition information
    
    Parameters:
    deviceId	 (array):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/action/changepartition?deviceId={deviceId}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def processChangePartition(vmanage, payload):
    """
    Process change partition operation
    
    Parameters:
    payload:	Device change partition request payload
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/action/changepartition"
    response = vmanage.client.apiCall("POST", endpoint, payload)
    return response

def generateDeactivateInfo(vmanage, deviceId):
    """
    Get deactivate partition information
    
    Parameters:
    deviceId	 (array):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/action/deactivate?deviceId={deviceId}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def processDeactivateSmu(vmanage, request):
    """
    Process deactivate operation for smu image
    
    Parameters:
    request:	Device smu image deactivate request
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/action/deactivate"
    response = vmanage.client.apiCall("POST", endpoint, request)
    return response

def processDefaultPartition(vmanage, request):
    """
    Process marking default partition operation
    
    Parameters:
    request:	Marking default partition request
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/action/defaultpartition"
    response = vmanage.client.apiCall("POST", endpoint, request)
    return response

def createFilterVPNList(vmanage):
    """
    Get filter VPN list
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/action/filter/vpn"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def generateInstallInfo(vmanage, deviceId):
    """
    Generate install info
    
    Parameters:
    deviceId	 (array):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/action/install?deviceId={deviceId}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def processInstall(vmanage, payload):
    """
    Process an installation operation
    
    Parameters:
    payload:	Installation payload
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/action/install"
    response = vmanage.client.apiCall("POST", endpoint, payload)
    return response

def generateDeviceList(vmanage, deviceType, groupId):
    """
    Get list of installed devices
    
    Parameters:
    Parameter Description
	Parameter Description
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/action/install/devices/{deviceType}?groupId={groupId}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def generateDeviceActionList(vmanage):
    """
    Get device action list
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/action/list"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def processLxcActivate(vmanage, payload):
    """
    Process an activation operation
    
    Parameters:
    payload:	Activation request payload
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/action/lxcactivate"
    response = vmanage.client.apiCall("POST", endpoint, payload)
    return response

def processLxcDelete(vmanage, payload):
    """
    Process a delete operation
    
    Parameters:
    payload:	Delete request payload
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/action/lxcdelete"
    response = vmanage.client.apiCall("POST", endpoint, payload)
    return response

def processLxcInstall(vmanage, payload):
    """
    Process an installation operation
    
    Parameters:
    payload:	Installation request payload
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/action/lxcinstall"
    response = vmanage.client.apiCall("POST", endpoint, payload)
    return response

def processLxcReload(vmanage, payload):
    """
    Process a reload operation
    
    Parameters:
    payload:	Reload request payload
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/action/lxcreload"
    response = vmanage.client.apiCall("POST", endpoint, payload)
    return response

def processLxcReset(vmanage, payload):
    """
    Process a reset operation
    
    Parameters:
    payload:	Reset request payload
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/action/lxcreset"
    response = vmanage.client.apiCall("POST", endpoint, payload)
    return response

def processLxcUpgrade(vmanage, payload):
    """
    Process an upgrade operation
    
    Parameters:
    payload:	Upgrade request payload
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/action/lxcupgrade"
    response = vmanage.client.apiCall("POST", endpoint, payload)
    return response

def generateRebootInfo(vmanage, deviceId):
    """
    Get device reboot information
    
    Parameters:
    deviceId	 (array):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/action/reboot?deviceId={deviceId}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def processReboot(vmanage, payload):
    """
    Process a reboot operation
    
    Parameters:
    payload:	Device reboot request payload
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/action/reboot"
    response = vmanage.client.apiCall("POST", endpoint, payload)
    return response

def generateRebootDeviceList(vmanage, deviceType, deviceId):
    """
    Get list of rebooted devices
    
    Parameters:
    Parameter Description
	Parameter Description
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/action/reboot/devices/{deviceType}?deviceId={deviceId}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def generateRediscoverInfo(vmanage):
    """
    Get rediscover operation information
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/action/rediscover"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def reDiscoverDevices(vmanage, payload):
    """
    Rediscover device
    
    Parameters:
    payload:	Rediscover device request payload
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/action/rediscover"
    response = vmanage.client.apiCall("POST", endpoint, payload)
    return response

def reDiscoverAllDevice(vmanage, payload):
    """
    Rediscover all devices
    
    Parameters:
    payload:	Rediscover device request payload
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/action/rediscoverall"
    response = vmanage.client.apiCall("POST", endpoint, payload)
    return response

def generateRemovePartitionInfo(vmanage, deviceId):
    """
    Get remove partition information
    
    Parameters:
    deviceId	 (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/action/removepartition?deviceId={deviceId}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def processRemovePartition(vmanage, payload):
    """
    Process remove partition operation
    
    Parameters:
    payload:	Device remove partition request payload
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/action/removepartition"
    response = vmanage.client.apiCall("POST", endpoint, payload)
    return response

def processDeleteAmpApiKey(vmanage, uuid):
    """
    Process amp api key deletion operation
    
    Parameters:
    uuid	 (string):	Uuid
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/action/security/amp/apikey/{uuid}"
    response = vmanage.client.apiCall("DELETE", endpoint)
    return response

def processAmpApiReKey(vmanage, payload):
    """
    Process amp api re-key operation
    
    Parameters:
    ampapire-keyrequestpayload:	AMP API re-key request payload
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/action/security/amp/rekey"
    response = vmanage.client.apiCall("POST", endpoint, payload)
    return response

def testApiKey(vmanage, uuid):
    """
    Get API key from device
    
    Parameters:
    uuid	 (string):	Device uuid
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/action/security/apikey/{uuid}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def generateSecurityDevicesList(vmanage, policyType, groupId):
    """
    Get list of devices by security policy type
    
    Parameters:
    policyType	 (string):	Policy type
	Parameter Description
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/action/security/devices/{policyType}?groupId={groupId}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def triggerPendingTasksMonitoring(vmanage):
    """
    Triggers global monitoring thread
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/action/startmonitor"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def testIoxConfig(vmanage, deviceIP):
    """
    testIoxConfig
    
    Parameters:
    Parameter Description
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/action/test/ioxconfig/{deviceIP}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def createUniqueVPNList(vmanage, deviceips):
    """
    Create unique VPN list
    
    Parameters:
    deviceips:	Device IPs
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/action/uniquevpnlist"
    response = vmanage.client.apiCall("POST", endpoint, deviceips)
    return response

def processVnfInstall(vmanage, payload):
    """
    Process an installation operation
    
    Parameters:
    payload:	Installation request payload
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/action/vnfinstall"
    response = vmanage.client.apiCall("POST", endpoint, payload)
    return response

def createVPNList(vmanage):
    """
    Create VPN list
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/action/vpn"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def getZTPUpgradeConfig(vmanage):
    """
    Get ZTP upgrade configuration
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/action/ztp/upgrade"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def processZTPUpgradeConfig(vmanage, ztpConfig):
    """
    Process ZTP upgrade configuration
    
    Parameters:
    ztpConfig:	ZTP upgrade config
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/action/ztp/upgrade"
    response = vmanage.client.apiCall("POST", endpoint, ztpConfig)
    return response

def getZTPUpgradeConfigSetting(vmanage):
    """
    Get ZTP upgrade configuration setting
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/action/ztp/upgrade/setting"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def processZTPUpgradeConfigSetting(vmanage, ztpSetting):
    """
    Process ZTP upgrade configuration setting
    
    Parameters:
    ztpSetting:	ZTP upgrade setting
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/action/ztp/upgrade/setting"
    response = vmanage.client.apiCall("POST", endpoint, ztpSetting)
    return response
