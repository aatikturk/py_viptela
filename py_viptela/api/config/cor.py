def getCORStatus(vmanage):
    """
    Get Cloud On Ramp list
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/cor"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response

def createAndMap(vmanage, request):
    """
    Map Host to Transit VPC/VNet
    
    Parameters:
    request:	Map host to transit VPC request
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/cor"
    response = vmanage.client.apiCall(vmanage.POST, endpoint, request)
    return response

def raiseAlarmForAccount(vmanage, accountobject):
    """
    Raise alarm for account
    
    Parameters:
    accountobject:	Account object
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/cor/account/alarm"
    response = vmanage.client.apiCall(vmanage.POST, endpoint, accountobject)
    return response

def removeTransitVPC(vmanage, accountid, transitvpcid, cloudregion, cloudtype):
    """
    Delete transit VPC/VNet
    
    Parameters:
    accountid	 (string):	Account Id
	transitvpcid	 (string):	Cloud VPC Id
	cloudregion	 (string):	Cloud region
	cloudtype	 (string):	Cloud type
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/cor/accountid/{accountid}?transitvpcid={transitvpcid}&cloudregion={cloudregion}&cloudtype={cloudtype}"
    response = vmanage.client.apiCall(vmanage.DELETE, endpoint)
    return response

def acquireRP(vmanage, request):
    """
    Acquire IP from resource pool
    
    Parameters:
    request:	Add IP from resource pool request
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/cor/acquireResourcePool"
    response = vmanage.client.apiCall(vmanage.POST, endpoint, request)
    return response

def getAmiList(vmanage, accountid, cloudregion, cloudtype):
    """
    Get AMI list
    
    Parameters:
    accountid	 (string):	Account Id
	cloudregion	 (string):	Cloud region
	cloudtype	 (string):	Cloud type
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/cor/ami?accountid={accountid}&cloudregion={cloudregion}&cloudtype={cloudtype}"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response

def getCloudList(vmanage):
    """
    Get cloud list
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/cor/cloud"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response

def getCloudAccounts(vmanage, cloudtype, cloudEnvironment):
    """
    Get cloud accounts
    
    Parameters:
    cloudtype	 (string):	Cloud type
	cloudEnvironment	 (string):	Cloud environment
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/cor/cloud/account?cloudtype={cloudtype}&cloudEnvironment={cloudEnvironment}"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response

def authCredAndUpdate(vmanage, credential):
    """
    Authenticate and update cloud account credentials
    
    Parameters:
    credential:	Cloud account credential
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/cor/cloud/authenticate"
    response = vmanage.client.apiCall(vmanage.PUT, endpoint, credential)
    return response

def authCORCredAndAdd(vmanage, credential):
    """
    Authenticate cloud account credentials
    
    Parameters:
    credential:	Cloud account credential
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/cor/cloud/authenticate"
    response = vmanage.client.apiCall(vmanage.POST, endpoint, credential)
    return response

def getCloudHostVpcAccountDetails(vmanage):
    """
    Get cloud host VPC account details
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/cor/cloud/host/accountdetails"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response

def getCloudMappedHostAccounts(vmanage, accountid, cloudtype):
    """
    Get cloud mapped accounts view
    
    Parameters:
    accountid	 (string):	Account Id
	cloudtype	 (string):	Cloud type
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/cor/cloud/mappedhostaccounts?accountid={accountid}&cloudtype={cloudtype}"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response

def createRP(vmanage, request):
    """
    Add resource pool
    
    Parameters:
    request:	Add resource pool request
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/cor/createResourcePool"
    response = vmanage.client.apiCall(vmanage.POST, endpoint, request)
    return response

def removeDeviceId(vmanage, accountid, transitvpcid, transitvpcname, cloudregion, cloudtype, devicePairId):
    """
    Remove device pair
    
    Parameters:
    accountid	 (string):	Account Id
	transitvpcid	 (string):	VPC Id
	transitvpcname	 (string):	VPC Name
	cloudregion	 (string):	Cloud region
	cloudtype	 (string):	Cloud type
	devicePairId	 (string):	Device pair Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/cor/deleteDevicepair?accountid={accountid}&transitvpcid={transitvpcid}&transitvpcname={transitvpcname}&cloudregion={cloudregion}&cloudtype={cloudtype}&devicePairId={devicePairId}"
    response = vmanage.client.apiCall(vmanage.DELETE, endpoint)
    return response

def getCORDevices(vmanage):
    """
    Get available device list
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/cor/device"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response

def addDevicePair(vmanage, request):
    """
    Add device pair
    
    Parameters:
    request:	Add device pair request
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/cor/devicepair"
    response = vmanage.client.apiCall(vmanage.POST, endpoint, request)
    return response

def getHostVPCs(vmanage, transitVpcId, devicePairId):
    """
    Get host VPC details
    
    Parameters:
    transitVpcId	 (string):	Transit VPC Id
	devicePairId	 (string):	Device pair Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/cor/devicepair/hostvpc?transitVpcId={transitVpcId}&devicePairId={devicePairId}"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response

def getExternalId(vmanage):
    """
    Get the vManage external ID for AWS
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/cor/externalId"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response

def getTransitDevicePairAndHostList(vmanage, accountId, cloudRegion):
    """
    Get device and host details
    
    Parameters:
    accountId	 (string):	Account Id
	cloudRegion	 (string):	Cloud region
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/cor/getTransitDevicePairAndHostList?accountId={accountId}&cloudRegion={cloudRegion}"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response

def getTransitVpcVpnList(vmanage, accountId):
    """
    Get transit VPN list
    
    Parameters:
    accountId	 (string):	Account Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/cor/getTransitVpnList?accountId={accountId}"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response

def getCloudHostVPCs(vmanage, accountid, cloudregion, cloudtype):
    """
    Get host VPC/VNet list
    
    Parameters:
    accountid	 (string):	Account Id
	cloudregion	 (string):	Cloud region
	cloudtype	 (string):	Cloud type
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/cor/hostvpc?accountid={accountid}&cloudregion={cloudregion}&cloudtype={cloudtype}"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response

def getTenantAndHostVpcList(vmanage, intent):
    """
    Get tenant and host VPC list
    
    Parameters:
    intent	 (string):	Intent
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/cor/hostvpclist?intent={intent}"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response

def updateHostVpcReachability(vmanage, updatevpcstatus):
    """
    Update host VPC reachability
    
    Parameters:
    updatevpcstatus:	Update VPC status
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/cor/hostvpclist"
    response = vmanage.client.apiCall(vmanage.PUT, endpoint, updatevpcstatus)
    return response

def getMappedVPCs(vmanage, accountid, cloudregion):
    """
    Get mapped VPC/VNet list
    
    Parameters:
    accountid	 (string):	Account Id
	cloudregion	 (string):	Cloud region
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/cor/map?accountid={accountid}&cloudregion={cloudregion}"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response

def mapVPCs(vmanage, host):
    """
    Map host to transit VPC/VNet
    
    Parameters:
    host:	Map host to VPC/VNet
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/cor/map"
    response = vmanage.client.apiCall(vmanage.POST, endpoint, host)
    return response

def unmapVPCs(vmanage, host):
    """
    Unmap host from transit VPC/VNet
    
    Parameters:
    host:	Unmap host to VPC/VNet
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/cor/map"
    response = vmanage.client.apiCall(vmanage.DELETE, endpoint, host)
    return response

def getPemKeyList(vmanage, accountid, cloudregion, cloudtype):
    """
    Get transit VPC PEM key list
    
    Parameters:
    accountid	 (string):	Account Id
	cloudregion	 (string):	Cloud region
	cloudtype	 (string):	Cloud type
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/cor/pem?accountid={accountid}&cloudregion={cloudregion}&cloudtype={cloudtype}"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response

def scaleDown(vmanage, updatevpc):
    """
    Scale down cloud on ramp
    
    Parameters:
    updatevpc:	Update VPC
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/cor/scale/down"
    response = vmanage.client.apiCall(vmanage.POST, endpoint, updatevpc)
    return response

def scaleUp(vmanage, updatevpc):
    """
    Scale up cloud on ramp
    
    Parameters:
    updatevpc:	Update VPC
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/cor/scale/up"
    response = vmanage.client.apiCall(vmanage.POST, endpoint, updatevpc)
    return response

def updatestatus(vmanage, statusobject):
    """
    Update task status
    
    Parameters:
    statusobject:	Status object
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/cor/status"
    response = vmanage.client.apiCall(vmanage.POST, endpoint, statusobject)
    return response

def getTransitVPCs(vmanage, accountid, cloudregion, cloudtype):
    """
    Get transit VPC/VNet list
    
    Parameters:
    accountid	 (string):	Account Id
	cloudregion	 (string):	Cloud region
	cloudtype	 (string):	Cloud type
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/cor/transitvpc?accountid={accountid}&cloudregion={cloudregion}&cloudtype={cloudtype}"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response

def updateTransitVPC(vmanage, vpc):
    """
    Update transit VPC/VNet
    
    Parameters:
    vpc:	VPC
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/cor/transitvpc"
    response = vmanage.client.apiCall(vmanage.PUT, endpoint, vpc)
    return response

def addTransitVPC(vmanage, vpc):
    """
    Create transit VPC/VNet
    
    Parameters:
    vpc:	VPC
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/cor/transitvpc"
    response = vmanage.client.apiCall(vmanage.POST, endpoint, vpc)
    return response

def updateTransitVpcAutoscaleProperties(vmanage, vpc):
    """
    Update transit VPC autoscale properties
    
    Parameters:
    vpc:	VPC
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/cor/transitvpc/autoscale-properties"
    response = vmanage.client.apiCall(vmanage.PUT, endpoint, vpc)
    return response

def getTransitVPCSupportedSize(vmanage, cloudtype, cloudEnvironment):
    """
    Get transit VPC supported size
    
    Parameters:
    cloudtype	 (string):	Cloud type
	cloudEnvironment	 (string):	Cloud environment
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/cor/transitvpc/size?cloudtype={cloudtype}&cloudEnvironment={cloudEnvironment}"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response
