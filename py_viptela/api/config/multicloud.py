def getAllCloudAccounts(vmanage, cloudType, cgEnable):
    """
    Get All cloud accounts
    
    Parameters:
    cloudType	 (string):	Cloud type
	cgEnable	 (boolean):	Cloud gateway enabled flag
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/multicloud/accounts?cloudType={cloudType}&cloudGatewayEnabled={cgEnable}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def validateAccountAdd(vmanage, account):
    """
    Authenticate cloud account credentials
    
    Parameters:
    account:	Multicloud account info
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/multicloud/accounts"
    response = vmanage.client.apiCall("POST", endpoint, account)
    return response

def getEdgeAccounts(vmanage, edgeType):
    """
    Get all Multicloud edge accounts
    
    Parameters:
    edgeType	 (string):	Edge type
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/multicloud/accounts/edge?edgeType={edgeType}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def validateEdgeAccountAdd(vmanage, account):
    """
    Authenticate edge account credentials
    
    Parameters:
    account:	Multicloud edge account info
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/multicloud/accounts/edge"
    response = vmanage.client.apiCall("POST", endpoint, account)
    return response

def getEdgeAccountDetails(vmanage, accountId):
    """
    Get edge account by account Id
    
    Parameters:
    accountId	 (string):	Edge Account Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/multicloud/accounts/edge/{accountId}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def updateEdgeAccount(vmanage, account, accountId):
    """
    Update Multicloud edge account
    
    Parameters:
    account:	Multicloud edge account info
	accountId	 (string):	Multicloud Edge Account Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/multicloud/accounts/edge/{accountId}"
    response = vmanage.client.apiCall("PUT", endpoint, account)
    return response

def deleteEdgeAccount(vmanage, accountId):
    """
    Delete edge account
    
    Parameters:
    accountId	 (string):	Edge Account Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/multicloud/accounts/edge/{accountId}"
    response = vmanage.client.apiCall("DELETE", endpoint)
    return response

def validateEdgeAccountUpdateCred(vmanage, account, accountId):
    """
    Update Multicloud edge account credential
    
    Parameters:
    account:	Multicloud edge account info
	accountId	 (string):	Multicloud Edge Account Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/multicloud/accounts/edge/{accountId}/credentials"
    response = vmanage.client.apiCall("PUT", endpoint, account)
    return response

def getCloudAccountDetails(vmanage, accountId):
    """
    Get cloud account by account Id
    
    Parameters:
    accountId	 (string):	Account Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/multicloud/accounts/{accountId}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def updateAccount(vmanage, account, accountId):
    """
    Update multicloud account
    
    Parameters:
    account:	Multicloud account info
	accountId	 (string):	Account Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/multicloud/accounts/{accountId}"
    response = vmanage.client.apiCall("PUT", endpoint, account)
    return response

def deleteAccount(vmanage, accountId):
    """
    Delete cloud account
    
    Parameters:
    accountId	 (string):	Account Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/multicloud/accounts/{accountId}"
    response = vmanage.client.apiCall("DELETE", endpoint)
    return response

def validateAccountUpdateCred(vmanage, account, accountId):
    """
    Update multicloud account credential
    
    Parameters:
    account:	Multicloud account info
	accountId	 (string):	Account Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/multicloud/accounts/{accountId}/credentials"
    response = vmanage.client.apiCall("PUT", endpoint, account)
    return response

def auditDryRun(vmanage, cloudType, cloudRegion):
    """
    Call an audit with dry run
    
    Parameters:
    cloudType	 (string):	Cloud type
	cloudRegion	 (string):	Region
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/multicloud/audit?cloudType={cloudType}&cloudRegion={cloudRegion}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def audit(vmanage, audit):
    """
    Call an audit
    
    Parameters:
    audit:	Audit
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/multicloud/audit"
    response = vmanage.client.apiCall("POST", endpoint, audit)
    return response

def getEdgeBillingAccounts(vmanage, edgeType, edgeAccountId, region):
    """
    Get Edge Billing Accounts
    
    Parameters:
    edgeType	 (string):	Interconnect Provider
	edgeAccountId	 (string):	Interconnect Provider Account ID
	region	 (string):	Region
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/multicloud/billingaccounts/edge/{edgeType}/{edgeAccountId}?region={region}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def getCgws(vmanage, cloudType, accountId, region, cgName):
    """
    Get cloud gateways
    
    Parameters:
    cloudType	 (string):	Cloud type
	accountId	 (string):	Account Id
	region	 (string):	Region
	cgName	 (string):	Cloud gateway name
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/multicloud/cloudgateway?cloudType={cloudType}&accountId={accountId}&region={region}&cloudGatewayName={cgName}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def createCgw(vmanage, cg):
    """
    Create cloud gateway
    
    Parameters:
    cg:	Cloud gateway
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/multicloud/cloudgateway"
    response = vmanage.client.apiCall("POST", endpoint, cg)
    return response

def getAzureNetworkVirtualAppliances(vmanage, cloudType, accoundId, region, rgName, rgSource, vhubName, vhubSource):
    """
    Discover Azure Virtual NVAs
    
    Parameters:
    cloudType	 (string):	Cloud type
	accoundId	 (string):	Account ID
	region	 (string):	Region
	rgName	 (string):	Resource Group Name
	rgSource	 (string):	Resource Group Source
	vhubName	 (string):	VHUB name
	vhubSource	 (string):	VHUB source
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/multicloud/cloudgateway/nvas?cloudType={cloudType}&accoundId={accoundId}&region={region}&resourceGroupName={rgName}&resourceGroupSource={rgSource}&vhubName={vhubName}&vhubSource={vhubSource}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def getAzureNvaSkuList(vmanage):
    """
    Get Azure NVA SKUs
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/multicloud/cloudgateway/nvasku"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def getCgwOrgResources(vmanage, cgName):
    """
    Get cloud gateways
    
    Parameters:
    cgName	 (string):	Cloud gateway name
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/multicloud/cloudgateway/resource?cloudGatewayName={cgName}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def getAzureResourceGroups(vmanage, cloudType, accountId):
    """
    Discover Azure Resource Groups
    
    Parameters:
    cloudType	 (string):	Cloud type
	accountId	 (string):	Account ID
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/multicloud/cloudgateway/resourceGroups?cloudType={cloudType}&accountId={accountId}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def getAzureVirtualHubs(vmanage, cloudType, accoundId, region, rgName, rgSource, vwanName, vwanSource):
    """
    Discover Azure Virtual HUBs
    
    Parameters:
    cloudType	 (string):	Cloud type
	accoundId	 (string):	Account ID
	region	 (string):	Region
	rgName	 (string):	Resource Group Name
	rgSource	 (string):	Resource Group Source
	vwanName	 (string):	VWAN name
	vwanSource	 (string):	VWAN source
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/multicloud/cloudgateway/vhubs?cloudType={cloudType}&accoundId={accoundId}&region={region}&resourceGroupName={rgName}&resourceGroupSource={rgSource}&vwanName={vwanName}&vwanSource={vwanSource}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def getAzureVirtualWans(vmanage, cloudType, accoundId, rgName, rgSource):
    """
    Discover Azure Virtual WANs
    
    Parameters:
    cloudType	 (string):	Cloud type
	accoundId	 (string):	Account ID
	rgName	 (string):	Resource Group Name
	rgSource	 (string):	Resource Group Source
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/multicloud/cloudgateway/vwans?cloudType={cloudType}&accoundId={accoundId}&resourceGroupName={rgName}&resourceGroupSource={rgSource}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def getCgwDetails(vmanage, cgName):
    """
    Get cloud gateway by name
    
    Parameters:
    cgName	 (string):	Cloud gateway name
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/multicloud/cloudgateway/{cgName}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def updateCgw(vmanage, cloudgateway, cgName):
    """
    Update cloud gateway
    
    Parameters:
    cloudgateway:	Cloud gateway
	cgName	 (string):	Cloud gateway name
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/multicloud/cloudgateway/{cgName}"
    response = vmanage.client.apiCall("PUT", endpoint, cloudgateway)
    return response

def deleteCgw(vmanage, cgName):
    """
    Delete cloud gateway
    
    Parameters:
    cgName	 (string):	Cloud gateway name
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/multicloud/cloudgateway/{cgName}"
    response = vmanage.client.apiCall("DELETE", endpoint)
    return response

def getSitesAttached(vmanage, cgName, systemIp, siteId, color, vpnTunnelStatus):
    """
    Get sites attached to CGW
    
    Parameters:
    cgName	 (string):	Cloud gateway name
	systemIp	 (string):	System IP
	siteId	 (string):	Site Id
	color	 (string):	Color
	vpnTunnelStatus	 (boolean):	Fetch vpnTunnelStatus
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/multicloud/cloudgateway/{cgName}/site?systemIp={systemIp}&siteId={siteId}&color={color}&vpnTunnelStatus={vpnTunnelStatus}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def TunnelScaling(vmanage, siteinformation, cgName):
    """
    Update tunnel scaling and accelerated vpn parameter for a branch endpoint
    
    Parameters:
    siteinformation:	Site information
	cgName	 (string):	Cloud gateway name
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/multicloud/cloudgateway/{cgName}/site"
    response = vmanage.client.apiCall("PUT", endpoint, siteinformation)
    return response

def attachSites(vmanage, siteinformation, cgName):
    """
    Attach sites to cloud gateway
    
    Parameters:
    siteinformation:	Site information
	cgName	 (string):	Cloud gateway name
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/multicloud/cloudgateway/{cgName}/site"
    response = vmanage.client.apiCall("POST", endpoint, siteinformation)
    return response

def detachSites(vmanage, siteinformation, cgName):
    """
    Detach sites from cloud gateway
    
    Parameters:
    siteinformation:	Site information
	cgName	 (string):	Cloud gateway name
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/multicloud/cloudgateway/{cgName}/site"
    response = vmanage.client.apiCall("DELETE", endpoint, siteinformation)
    return response

def getCloudGateways(vmanage, cloudType):
    """
    Get sites with connectivity to the cloud by cloud type
    
    Parameters:
    cloudType	 (string):	Cloud type
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/multicloud/cloudgateways/{cloudType}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def getCgwCustomSettingDetails(vmanage, cgName):
    """
    Get cloud gateway custom setting by cloud gateway name
    
    Parameters:
    cgName	 (string):	Cloud gateway name
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/multicloud/cloudgatewaysetting/{cgName}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def getCgwTypes(vmanage, cloudType):
    """
    Get cloud gateway types for specified cloudType
    
    Parameters:
    cloudType	 (string):	Cloud type
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/multicloud/cloudgatewaytype?cloudType={cloudType}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def getCloudConnectedSitesByEdgeType(vmanage, edgeType, edgeGatewayName):
    """
    Get sites with connectivity to the interconnect gateways by edge type
    
    Parameters:
    edgeType	 (string):	Edge type
	edgeGatewayName	 (string):	Interconnect Gateway Name
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/multicloud/connected-sites/edge/{edgeType}?edgeGatewayName={edgeGatewayName}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def getCloudConnectedSitesByCloudType(vmanage, cloudType, cgName):
    """
    Get sites with connectivity to the cloud by cloud type
    
    Parameters:
    cloudType	 (string):	Cloud type
	cgName	 (string):	Cloud Gateway Name
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/multicloud/connected-sites/{cloudType}?cloudGatewayName={cgName}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def getEdgeConnectivityDetails(vmanage, edgeType, connectivityName, connectivityType, edgeGatewayName):
    """
    Get Interconnect Connectivity details
    
    Parameters:
    edgeType	 (string):	Edge type
	connectivityName	 (string):	Connectivity Name
	connectivityType	 (string):	Connectivity Type
	edgeGatewayName	 (string):	Interconnect Gateway name
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/multicloud/connectivity/edge?edgeType={edgeType}&connectivityName={connectivityName}&connectivityType={connectivityType}&edgeGatewayName={edgeGatewayName}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def updateEdgeConnectivity(vmanage, edgeconnectivity):
    """
    Update Interconnect connectivity
    
    Parameters:
    edgeconnectivity:	Edge connectivity
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/multicloud/connectivity/edge"
    response = vmanage.client.apiCall("PUT", endpoint, edgeconnectivity)
    return response

def createEdgeConnectivity(vmanage, edgeconnectivity):
    """
    Create Interconnect connectivity
    
    Parameters:
    edgeconnectivity:	Edge connectivity
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/multicloud/connectivity/edge"
    response = vmanage.client.apiCall("POST", endpoint, edgeconnectivity)
    return response

def deleteEdgeConnectivity(vmanage, connectionName):
    """
    Delete Interconnect connectivity
    
    Parameters:
    connectionName	 (string):	Edge connectivity name
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/multicloud/connectivity/edge/{connectionName}"
    response = vmanage.client.apiCall("DELETE", endpoint)
    return response

def getEdgeConnectivityDetailByName(vmanage, connectivityName):
    """
    Get Interconnect Connectivity by name
    
    Parameters:
    connectivityName	 (string):	IC-GW connectivity name
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/multicloud/connectivity/edge/{connectivityName}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def getConnectivityGateways(vmanage, accountId, cloudType, connectivityType, connectivityGatewayName, region, network, state, refresh):
    """
    Get all Connectivity Gateways
    
    Parameters:
    accountId	 (string):	Account Id
	cloudType	 (string):	Cloud Type
	connectivityType	 (string):	Cloud Connectivity Type
	connectivityGatewayName	 (string):	Connectivity Gateway Name
	region	 (string):	Region
	network	 (string):	Network
	state	 (string):	State
	refresh	 (string):	Refresh
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/multicloud/connectivitygateway?accountId={accountId}&cloudType={cloudType}&connectivityType={connectivityType}&connectivityGatewayName={connectivityGatewayName}&region={region}&network={network}&state={state}&refresh={refresh}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def createConnectivityGateway(vmanage, connectivitygateway):
    """
    Create Connectivity gateway
    
    Parameters:
    connectivitygateway:	Connectivity gateway
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/multicloud/connectivitygateway"
    response = vmanage.client.apiCall("POST", endpoint, connectivitygateway)
    return response

def cleanUpAllConnectivityGatewaysInLocalDB(vmanage, deletionType):
    """
    Delete all Connectivity Gateways in local DB
    
    Parameters:
    deletionType	 (string):	Deletion Type
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/multicloud/connectivitygateway?deletionType={deletionType}"
    response = vmanage.client.apiCall("DELETE", endpoint)
    return response

def deleteConnectivityGateway(vmanage, cloudProvider, connectivityGatewayName, connectivityType):
    """
    Delete Connectivity Gateway
    
    Parameters:
    cloudProvider	 (string):	Cloud Provider
	connectivityGatewayName	 (string):	Connectivity gateway name
	connectivityType	 (string):	Cloud Connectivity Type
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/multicloud/connectivitygateway/{cloudProvider}/{connectivityGatewayName}?connectivityType={connectivityType}"
    response = vmanage.client.apiCall("DELETE", endpoint)
    return response

def getConnectivityGatewayCreationOptions(vmanage, accountId, cloudType, connectivityType, refresh):
    """
    Get connectivity gateway creation options
    
    Parameters:
    accountId	 (string):	Account Id
	cloudType	 (string):	Cloud Type
	connectivityType	 (string):	Cloud Connectivity Type
	refresh	 (string):	Refresh
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/multicloud/connectivitygatewaycreationoptions?accountId={accountId}&cloudType={cloudType}&connectivityType={connectivityType}&refresh={refresh}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def getDashboardEdgeInfo(vmanage):
    """
    Get interconnect edge gateway dashboard info
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/multicloud/dashboard/edge"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def getWanDevices(vmanage):
    """
    Get available WAN edge devices
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/multicloud/device"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def getCloudDevicesByEdgeType(vmanage, edgeType, edgeGatewayName):
    """
    Get cloud devices by edge type
    
    Parameters:
    edgeType	 (string):	Edge type
	edgeGatewayName	 (string):	Edge Gateway Name
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/multicloud/devices/edge/{edgeType}?edgeGatewayName={edgeGatewayName}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def getCloudDevicesCloudType(vmanage, cloudType, cgName):
    """
    Get cloud devices by cloud type
    
    Parameters:
    cloudType	 (string):	Cloud type
	cgName	 (string):	Cloud Gateway Name
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/multicloud/devices/{cloudType}?cloudGatewayName={cgName}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def getEdgeWanDevices(vmanage, edgeType):
    """
    Get available WAN edge devices
    
    Parameters:
    edgeType	 (string):	Edge Type
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/multicloud/edge/{edgeType}/device"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def getIcgws(vmanage, edgeType, accountId, region, regionId, resourceState, edgeGatewayName):
    """
    Get Interconnect Gateways
    
    Parameters:
    edgeType	 (string):	Edge type
	accountId	 (string):	Account Id
	region	 (string):	Region
	regionId	 (string):	Region Id
	resourceState	 (string):	Resource State
	edgeGatewayName	 (string):	Edge gateway name
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/multicloud/gateway/edge?edgeType={edgeType}&accountId={accountId}&region={region}&regionId={regionId}&resourceState={resourceState}&edgeGatewayName={edgeGatewayName}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def createIcgw(vmanage, interconnectgateway):
    """
    Create Interconnect Gateway
    
    Parameters:
    interconnectgateway:	Interconnect Gateway
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/multicloud/gateway/edge"
    response = vmanage.client.apiCall("POST", endpoint, interconnectgateway)
    return response

def getIcgwCustomSettingDetails(vmanage, edgeGatewayName):
    """
    Get Interconnect Gateway custom setting by Interconnect Gateway name
    
    Parameters:
    edgeGatewayName	 (string):	Edge gateway name
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/multicloud/gateway/edge/setting/{edgeGatewayName}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def getIcgwTypes(vmanage, edgeType):
    """
    Get Interconnect Gateway type for specified Edge Provider
    
    Parameters:
    edgeType	 (string):	Edge type
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/multicloud/gateway/edge/types?edgeType={edgeType}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def getIcgwDetails(vmanage, edgeGatewayName):
    """
    Get Interconnect Gateway by name
    
    Parameters:
    edgeGatewayName	 (string):	Edge gateway name
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/multicloud/gateway/edge/{edgeGatewayName}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def updateIcgw(vmanage, gatewayInfo, edgeGatewayName):
    """
    Update Interconnect Gateway
    
    Parameters:
    gatewayInfo:	Description
	edgeGatewayName	 (string):	Edge gateway name
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/multicloud/gateway/edge/{edgeGatewayName}"
    response = vmanage.client.apiCall("PUT", endpoint, gatewayInfo)
    return response

def deleteIcgw(vmanage, edgeGatewayName):
    """
    Delete Interconnect Gateway
    
    Parameters:
    edgeGatewayName	 (string):	Edge gateway name
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/multicloud/gateway/edge/{edgeGatewayName}"
    response = vmanage.client.apiCall("DELETE", endpoint)
    return response

def getEdgeGateways(vmanage, edgeType):
    """
    Get sites with connectivity to the interconnect gateways by edge type
    
    Parameters:
    edgeType	 (string):	Edge type
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/multicloud/gateways/edge/{edgeType}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def getHostVpcs(vmanage, cloudType, accountIds, region, untagged):
    """
    Get tagged, untagged, or all Host VPCs
    
    Parameters:
    cloudType	 (string):	Cloud type
	accountIds	 (string):	Account Id
	region	 (string):	Region
	untagged	 (string):	Untagged flag
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/multicloud/hostvpc?cloudType={cloudType}&accountIds={accountIds}&region={region}&untagged={untagged}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def getVpcTags(vmanage, cloudType, region, tagName):
    """
    Get vpc tags
    
    Parameters:
    cloudType	 (string):	Cloud type
	region	 (string):	Region
	tagName	 (string):	Tag name
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/multicloud/hostvpc/tags?cloudType={cloudType}&region={region}&tagName={tagName}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def editTag(vmanage, vpctag):
    """
    Edit VPCs for a tag
    
    Parameters:
    vpctag:	VPC tag
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/multicloud/hostvpc/tags"
    response = vmanage.client.apiCall("PUT", endpoint, vpctag)
    return response

def hostvpcTagging(vmanage, vpctag):
    """
    Tag a VPC
    
    Parameters:
    vpctag:	VPC tag
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/multicloud/hostvpc/tags"
    response = vmanage.client.apiCall("POST", endpoint, vpctag)
    return response

def unTag(vmanage, tagName):
    """
    Delete a tag
    
    Parameters:
    tagName	 (string):	Tag name
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/multicloud/hostvpc/tags/{tagName}"
    response = vmanage.client.apiCall("DELETE", endpoint)
    return response

def getSupportedEdgeImageNames(vmanage, edgeType):
    """
    Get Edge provider supported images
    
    Parameters:
    edgeType	 (string):	Edge type
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/multicloud/imagename/edge?edgeType={edgeType}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def getSupportedInstanceSize(vmanage, cloudType, accountId, cloudRegion):
    """
    Get Transit VPC supported size
    
    Parameters:
    Parameter Description
	Parameter Description
	Parameter Description
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/multicloud/instancesize?cloudType={cloudType}&accountId={accountId}&cloudRegion={cloudRegion}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def getSupportedEdgeInstanceSize(vmanage, edgeType):
    """
    Get Edge provider supported size
    
    Parameters:
    edgeType	 (string):	Edge type
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/multicloud/instancesize/edge?edgeType={edgeType}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def getWanInterfaceColors(vmanage):
    """
    Get WAN interface colors
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/multicloud/interfacecolor"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def getEdgeLocationsInfo(vmanage, edgeType, accountId, region):
    """
    Get Edge Locations
    
    Parameters:
    edgeType	 (string):	Edge Type
	accountId	 (string):	Edge Account Id
	region	 (string):	Region
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/multicloud/locations/edge/{edgeType}?accountId={accountId}&region={region}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def deleteEdge(vmanage, edgeType):
    """
    Delete edge
    
    Parameters:
    edgeType	 (string):	Edge Type
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/multicloud/locations/edge/{edgeType}"
    response = vmanage.client.apiCall("DELETE", endpoint)
    return response

def updateEdgeLocationsInfo(vmanage, edgeType, accountId):
    """
    Update Edge Locations
    
    Parameters:
    edgeType	 (string):	Edge Type
	accountId	 (string):	Edge Account Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/multicloud/locations/edge/{edgeType}/accountId/{accountId}"
    response = vmanage.client.apiCall("PUT", endpoint)
    return response

def getMappingMatrix(vmanage, cloudType):
    """
    Get default mapping values
    
    Parameters:
    cloudType	 (string):	Cloud type
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/multicloud/map?cloudType={cloudType}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def processMapping(vmanage, vpcmapping):
    """
    Process intent of connecting VPNs with VPCs through cloud gateway
    
    Parameters:
    vpcmapping:	VPC mapping
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/multicloud/map"
    response = vmanage.client.apiCall("POST", endpoint, vpcmapping)
    return response

def getDefaultMappingValues(vmanage, cloudType):
    """
    Get default mapping values
    
    Parameters:
    cloudType	 (string):	Cloud type
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/multicloud/map/defaults?cloudType={cloudType}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def getMappingStatus(vmanage, cloudType, region):
    """
    Get mapping status
    
    Parameters:
    cloudType	 (string):	Cloud type
	region	 (string):	Region
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/multicloud/map/status?cloudType={cloudType}&region={region}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def getMappingSummary(vmanage, vpnTunnelStatus, cloudType):
    """
    Get mapping summary
    
    Parameters:
    vpnTunnelStatus	 (boolean):	VPN tunnel status
	cloudType	 (string):	Cloud type
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/multicloud/map/summary?vpnTunnelStatus={vpnTunnelStatus}&cloudType={cloudType}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def getMappingTags(vmanage, cloudType):
    """
    Get default mapping values
    
    Parameters:
    cloudType	 (string):	Cloud type
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/multicloud/map/tags?cloudType={cloudType}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def getEdgeMappingTags(vmanage, cloudType, accountId):
    """
    Get default Interconnect mapping tag values
    
    Parameters:
    cloudType	 (string):	Cloud type
	accountId	 (string):	Cloud Account Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/multicloud/map/tags/edge?cloudType={cloudType}&accountId={accountId}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def getMappingVpns(vmanage):
    """
    Get default mapping values
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/multicloud/map/vpns"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def getCgwAssociatedMappings(vmanage, cloudType, cgName, siteUuid):
    """
    Get associated mappings to the CGW
    
    Parameters:
    cloudType	 (string):	Cloud type
	cgName	 (string):	Cloud Gateway Name
	siteUuid	 (string):	Site Device UUID
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/multicloud/mapping/{cloudType}?cloudGatewayName={cgName}&siteUuid={siteUuid}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def getPartnerPorts(vmanage, edgeType, accountId, cloudType, connectType, vxcPermitted, authorizationKey, refresh):
    """
    Get partner ports
    
    Parameters:
    edgeType	 (string):	Edge type
	accountId	 (string):	Edge Account Id
	cloudType	 (string):	Cloud Type
	connectType	 (string):	Connect Type filter
	vxcPermitted	 (string):	VXC Permitted on the port
	authorizationKey	 (string):	authorization Key
	refresh	 (string):	Refresh
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/multicloud/partnerports/edge?edgeType={edgeType}&accountId={accountId}&cloudType={cloudType}&connectType={connectType}&vxcPermitted={vxcPermitted}&authorizationKey={authorizationKey}&refresh={refresh}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def getPortSpeed(vmanage, edgeType, edgeAccountId, connectivityType, cloudType, cloudAccountId, connectType, connectSubType, connectivityGateway, partnerPort):
    """
    Get supported port speed
    
    Parameters:
    edgeType	 (string):	Interconnect Provider
	edgeAccountId	 (string):	Interconnect Provider Account ID
	connectivityType	 (string):	Interconnect Connectivity Type
	cloudType	 (string):	Cloud Service Provider
	cloudAccountId	 (string):	Cloud Service Provider Account ID
	connectType	 (string):	Connection Type filter
	connectSubType	 (string):	Connection Sub-Type filter
	connectivityGateway	 (string):	Connectivity Gateway
	partnerPort	 (string):	partnerPort
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/multicloud/portSpeed/edge/{edgeType}/{edgeAccountId}/{connectivityType}?cloudType={cloudType}&cloudAccountId={cloudAccountId}&connectType={connectType}&connectSubType={connectSubType}&connectivityGateway={connectivityGateway}&partnerPort={partnerPort}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def getCloudRegions(vmanage, cloudType):
    """
    Get cloud regions
    
    Parameters:
    cloudType	 (string):	Cloud type
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/multicloud/regions?cloudType={cloudType}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def getEdgeGlobalSettings(vmanage, edgeType):
    """
    Get edge global settings
    
    Parameters:
    edgeType	 (string):	Edge type
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/multicloud/settings/edge/global?edgeType={edgeType}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def updateEdgeGlobalSettings(vmanage, globalsetting):
    """
    Update edge global settings for Edge provider
    
    Parameters:
    globalsetting:	Global setting
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/multicloud/settings/edge/global"
    response = vmanage.client.apiCall("PUT", endpoint, globalsetting)
    return response

def addEdgeGlobalSettings(vmanage, globalsetting):
    """
    Add global settings for Edge provider
    
    Parameters:
    globalsetting:	Global setting
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/multicloud/settings/edge/global"
    response = vmanage.client.apiCall("POST", endpoint, globalsetting)
    return response

def getGlobalSettings(vmanage, cloudType):
    """
    Get global settings
    
    Parameters:
    cloudType	 (string):	Cloud type
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/multicloud/settings/global?cloudType={cloudType}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def updateGlobalSettings(vmanage, globalsetting):
    """
    Update ip in resource pool
    
    Parameters:
    globalsetting:	Global setting
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/multicloud/settings/global"
    response = vmanage.client.apiCall("PUT", endpoint, globalsetting)
    return response

def addGlobalSettings(vmanage, globalsetting):
    """
    Acquire ip from resource pool
    
    Parameters:
    globalsetting:	Global setting
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/multicloud/settings/global"
    response = vmanage.client.apiCall("POST", endpoint, globalsetting)
    return response

def getSites(vmanage, color, attached):
    """
    Get available sites
    
    Parameters:
    color	 (string):	Color
	attached	 (boolean):	Is endpoint attached
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/multicloud/site?color={color}&attached={attached}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def getSshKeyList(vmanage, cloudType, accountId, cloudRegion):
    """
    Get SSH keys
    
    Parameters:
    cloudType	 (string):	Cloud type
	accountId	 (string):	Account Id
	cloudRegion	 (string):	Region
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/multicloud/sshkeys?cloudType={cloudType}&accountId={accountId}&cloudRegion={cloudRegion}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def getPostAggregationDataByQuery(vmanage, statsquerystring):
    """
    Get aggregated data based on input query and filters. The data can be filtered on time and other unique parameters based upon necessity and intended usage
    
    Parameters:
    statsquerystring:	Stats query string
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/multicloud/statistics/interface/aggregation"
    response = vmanage.client.apiCall("POST", endpoint, statsquerystring)
    return response

def getSupportedSoftwareImageList(vmanage, cloudType, accountId, cloudRegion):
    """
    Get software image list
    
    Parameters:
    cloudType	 (string):	Cloud type
	accountId	 (string):	Account Id
	cloudRegion	 (string):	Region
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/multicloud/swimages?cloudType={cloudType}&accountId={accountId}&cloudRegion={cloudRegion}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def telemetry(vmanage, telemetry):
    """
    reports telemetry data
    
    Parameters:
    telemetry:	telemetry
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/multicloud/telemetry"
    response = vmanage.client.apiCall("POST", endpoint, telemetry)
    return response

def getTunnelNames(vmanage, cloudType, cgName):
    """
    Get tunnel names
    
    Parameters:
    cloudType	 (string):	Cloud type
	cgName	 (string):	Cloud gateway name
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/multicloud/tunnels/{cloudType}?cloudGatewayName={cgName}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def getCloudTypes(vmanage):
    """
    Get cloud types
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/multicloud/types"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def getEdgeTypes(vmanage):
    """
    Get edge types
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/multicloud/types/edge"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def getVHubs(vmanage, cloudType, accountId, resourceGroup, vWanName, vNetTags):
    """
    Get Virtual Hubs
    
    Parameters:
    cloudType	 (string):	Cloud Type
	accountId	 (string):	Account Id
	resourceGroup	 (string):	Resource Group
	vWanName	 (string):	VWan Name
	vNetTags	 (string):	VNet Tags
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/multicloud/vhubs?cloudType={cloudType}&accountId={accountId}&resourceGroup={resourceGroup}&vWanName={vWanName}&vNetTags={vNetTags}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def createVirtualWan(vmanage, virtualwan):
    """
    Create Virtual WAN
    
    Parameters:
    virtualwan:	Virtual WAN
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/multicloud/vwan"
    response = vmanage.client.apiCall("POST", endpoint, virtualwan)
    return response

def deleteVirtualWan(vmanage, cloudProvider, vWanName):
    """
    Delete Virtual Wan
    
    Parameters:
    cloudProvider	 (string):	Cloud Provider
	vWanName	 (string):	Virtual Wan name
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/multicloud/vwan/{cloudProvider}/{vWanName}"
    response = vmanage.client.apiCall("DELETE", endpoint)
    return response

def getVWans(vmanage, accountId, cloudType, resourceGroup, refresh):
    """
    Get Virtual Wans
    
    Parameters:
    accountId	 (string):	Account Id
	cloudType	 (string):	Cloud Type
	resourceGroup	 (string):	Resource Group
	refresh	 (string):	Refresh
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/multicloud/vwans?accountId={accountId}&cloudType={cloudType}&resourceGroup={resourceGroup}&refresh={refresh}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def getEdgeWidget(vmanage, edgeType):
    """
    Get Interconnect Edge widget by edge type
    
    Parameters:
    edgeType	 (string):	Edge type
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/multicloud/widget/edge/{edgeType}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def getCloudWidget(vmanage, cloudType):
    """
    Get cloud widget by cloud type
    
    Parameters:
    cloudType	 (string):	Cloud type
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/multicloud/widget/{cloudType}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response
