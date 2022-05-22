from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class MultiCloud(object):
    """
    Configuration - Multi Cloud API
    
    Implements GET POST DEL PUT methods for MultiCloud endpoints

    """

    def __init__(self, session, host, port):
        self.client = HttpMethods.HttpClient(session=session)
        self.host = host
        self.port = port
    
    
    def getAllCloudAccounts(self, cloudType, cgEnable):
        """
        Get All cloud accounts
        
        Parameters:
        cloudType	 (string):	Cloud type
		cgEnable	 (boolean):	Cloud gateway enabled flag
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/multicloud/accounts?cloudType={cloudType}&cloudGatewayEnabled={cgEnable}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def validateAccountAdd(self, account):
        """
        Authenticate cloud account credentials
        
        Parameters:
        account:	Multicloud account info
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/multicloud/accounts"
        response = self.client.apiCall(HttpMethods.POST, endpoint, account)
        return response


    def getEdgeAccounts(self, edgeType):
        """
        Get all Multicloud edge accounts
        
        Parameters:
        edgeType	 (string):	Edge type
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/multicloud/accounts/edge?edgeType={edgeType}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def validateEdgeAccountAdd(self, account):
        """
        Authenticate edge account credentials
        
        Parameters:
        account:	Multicloud edge account info
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/multicloud/accounts/edge"
        response = self.client.apiCall(HttpMethods.POST, endpoint, account)
        return response


    def getEdgeAccountDetails(self, accountId):
        """
        Get edge account by account Id
        
        Parameters:
        accountId	 (string):	Edge Account Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/multicloud/accounts/edge/{accountId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def updateEdgeAccount(self, account, accountId):
        """
        Update Multicloud edge account
        
        Parameters:
        account:	Multicloud edge account info
		accountId	 (string):	Multicloud Edge Account Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/multicloud/accounts/edge/{accountId}"
        response = self.client.apiCall(HttpMethods.PUT, endpoint, account)
        return response


    def deleteEdgeAccount(self, accountId):
        """
        Delete edge account
        
        Parameters:
        accountId	 (string):	Edge Account Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/multicloud/accounts/edge/{accountId}"
        response = self.client.apiCall(HttpMethods.DELETE, endpoint)
        return response


    def validateEdgeAccountUpdateCred(self, account, accountId):
        """
        Update Multicloud edge account credential
        
        Parameters:
        account:	Multicloud edge account info
		accountId	 (string):	Multicloud Edge Account Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/multicloud/accounts/edge/{accountId}/credentials"
        response = self.client.apiCall(HttpMethods.PUT, endpoint, account)
        return response


    def getCloudAccountDetails(self, accountId):
        """
        Get cloud account by account Id
        
        Parameters:
        accountId	 (string):	Account Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/multicloud/accounts/{accountId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def updateAccount(self, account, accountId):
        """
        Update multicloud account
        
        Parameters:
        account:	Multicloud account info
		accountId	 (string):	Account Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/multicloud/accounts/{accountId}"
        response = self.client.apiCall(HttpMethods.PUT, endpoint, account)
        return response


    def deleteAccount(self, accountId):
        """
        Delete cloud account
        
        Parameters:
        accountId	 (string):	Account Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/multicloud/accounts/{accountId}"
        response = self.client.apiCall(HttpMethods.DELETE, endpoint)
        return response


    def validateAccountUpdateCred(self, account, accountId):
        """
        Update multicloud account credential
        
        Parameters:
        account:	Multicloud account info
		accountId	 (string):	Account Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/multicloud/accounts/{accountId}/credentials"
        response = self.client.apiCall(HttpMethods.PUT, endpoint, account)
        return response


    def auditDryRun(self, cloudType, cloudRegion):
        """
        Call an audit with dry run
        
        Parameters:
        cloudType	 (string):	Cloud type
		cloudRegion	 (string):	Region
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/multicloud/audit?cloudType={cloudType}&cloudRegion={cloudRegion}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def audit(self, audit):
        """
        Call an audit
        
        Parameters:
        audit:	Audit
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/multicloud/audit"
        response = self.client.apiCall(HttpMethods.POST, endpoint, audit)
        return response


    def getEdgeBillingAccounts(self, edgeType, edgeAccountId, region):
        """
        Get Edge Billing Accounts
        
        Parameters:
        edgeType	 (string):	Interconnect Provider
		edgeAccountId	 (string):	Interconnect Provider Account ID
		region	 (string):	Region
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/multicloud/billingaccounts/edge/{edgeType}/{edgeAccountId}?region={region}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getCgws(self, cloudType, accountId, region, cgName):
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
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/multicloud/cloudgateway?cloudType={cloudType}&accountId={accountId}&region={region}&cloudGatewayName={cgName}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def createCgw(self, cg):
        """
        Create cloud gateway
        
        Parameters:
        cg:	Cloud gateway
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/multicloud/cloudgateway"
        response = self.client.apiCall(HttpMethods.POST, endpoint, cg)
        return response


    def getAzureNetworkVirtualAppliances(self, cloudType, accoundId, region, rgName, rgSource, vhubName, vhubSource):
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
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/multicloud/cloudgateway/nvas?cloudType={cloudType}&accoundId={accoundId}&region={region}&resourceGroupName={rgName}&resourceGroupSource={rgSource}&vhubName={vhubName}&vhubSource={vhubSource}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getAzureNvaSkuList(self):
        """
        Get Azure NVA SKUs
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/multicloud/cloudgateway/nvasku"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getCgwOrgResources(self, cgName):
        """
        Get cloud gateways
        
        Parameters:
        cgName	 (string):	Cloud gateway name
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/multicloud/cloudgateway/resource?cloudGatewayName={cgName}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getAzureResourceGroups(self, cloudType, accountId):
        """
        Discover Azure Resource Groups
        
        Parameters:
        cloudType	 (string):	Cloud type
		accountId	 (string):	Account ID
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/multicloud/cloudgateway/resourceGroups?cloudType={cloudType}&accountId={accountId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getAzureVirtualHubs(self, cloudType, accoundId, region, rgName, rgSource, vwanName, vwanSource):
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
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/multicloud/cloudgateway/vhubs?cloudType={cloudType}&accoundId={accoundId}&region={region}&resourceGroupName={rgName}&resourceGroupSource={rgSource}&vwanName={vwanName}&vwanSource={vwanSource}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getAzureVirtualWans(self, cloudType, accoundId, rgName, rgSource):
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
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/multicloud/cloudgateway/vwans?cloudType={cloudType}&accoundId={accoundId}&resourceGroupName={rgName}&resourceGroupSource={rgSource}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getCgwDetails(self, cgName):
        """
        Get cloud gateway by name
        
        Parameters:
        cgName	 (string):	Cloud gateway name
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/multicloud/cloudgateway/{cgName}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def updateCgw(self, cloudgateway, cgName):
        """
        Update cloud gateway
        
        Parameters:
        cloudgateway:	Cloud gateway
		cgName	 (string):	Cloud gateway name
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/multicloud/cloudgateway/{cgName}"
        response = self.client.apiCall(HttpMethods.PUT, endpoint, cloudgateway)
        return response


    def deleteCgw(self, cgName):
        """
        Delete cloud gateway
        
        Parameters:
        cgName	 (string):	Cloud gateway name
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/multicloud/cloudgateway/{cgName}"
        response = self.client.apiCall(HttpMethods.DELETE, endpoint)
        return response


    def getSitesAttached(self, cgName, systemIp, siteId, color, vpnTunnelStatus):
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
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/multicloud/cloudgateway/{cgName}/site?systemIp={systemIp}&siteId={siteId}&color={color}&vpnTunnelStatus={vpnTunnelStatus}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def TunnelScaling(self, siteinformation, cgName):
        """
        Update tunnel scaling and accelerated vpn parameter for a branch endpoint
        
        Parameters:
        siteinformation:	Site information
		cgName	 (string):	Cloud gateway name
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/multicloud/cloudgateway/{cgName}/site"
        response = self.client.apiCall(HttpMethods.PUT, endpoint, siteinformation)
        return response


    def attachSites(self, siteinformation, cgName):
        """
        Attach sites to cloud gateway
        
        Parameters:
        siteinformation:	Site information
		cgName	 (string):	Cloud gateway name
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/multicloud/cloudgateway/{cgName}/site"
        response = self.client.apiCall(HttpMethods.POST, endpoint, siteinformation)
        return response


    def detachSites(self, siteinformation, cgName):
        """
        Detach sites from cloud gateway
        
        Parameters:
        siteinformation:	Site information
		cgName	 (string):	Cloud gateway name
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/multicloud/cloudgateway/{cgName}/site"
        response = self.client.apiCall(HttpMethods.DELETE, endpoint, siteinformation)
        return response


    def getCloudGateways(self, cloudType):
        """
        Get sites with connectivity to the cloud by cloud type
        
        Parameters:
        cloudType	 (string):	Cloud type
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/multicloud/cloudgateways/{cloudType}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getCgwCustomSettingDetails(self, cgName):
        """
        Get cloud gateway custom setting by cloud gateway name
        
        Parameters:
        cgName	 (string):	Cloud gateway name
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/multicloud/cloudgatewaysetting/{cgName}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getCgwTypes(self, cloudType):
        """
        Get cloud gateway types for specified cloudType
        
        Parameters:
        cloudType	 (string):	Cloud type
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/multicloud/cloudgatewaytype?cloudType={cloudType}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getCloudConnectedSitesByEdgeType(self, edgeType, edgeGatewayName):
        """
        Get sites with connectivity to the interconnect gateways by edge type
        
        Parameters:
        edgeType	 (string):	Edge type
		edgeGatewayName	 (string):	Interconnect Gateway Name
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/multicloud/connected-sites/edge/{edgeType}?edgeGatewayName={edgeGatewayName}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getCloudConnectedSitesByCloudType(self, cloudType, cgName):
        """
        Get sites with connectivity to the cloud by cloud type
        
        Parameters:
        cloudType	 (string):	Cloud type
		cgName	 (string):	Cloud Gateway Name
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/multicloud/connected-sites/{cloudType}?cloudGatewayName={cgName}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getEdgeConnectivityDetails(self, edgeType, connectivityName, connectivityType, edgeGatewayName):
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
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/multicloud/connectivity/edge?edgeType={edgeType}&connectivityName={connectivityName}&connectivityType={connectivityType}&edgeGatewayName={edgeGatewayName}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def updateEdgeConnectivity(self, edgeconnectivity):
        """
        Update Interconnect connectivity
        
        Parameters:
        edgeconnectivity:	Edge connectivity
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/multicloud/connectivity/edge"
        response = self.client.apiCall(HttpMethods.PUT, endpoint, edgeconnectivity)
        return response


    def createEdgeConnectivity(self, edgeconnectivity):
        """
        Create Interconnect connectivity
        
        Parameters:
        edgeconnectivity:	Edge connectivity
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/multicloud/connectivity/edge"
        response = self.client.apiCall(HttpMethods.POST, endpoint, edgeconnectivity)
        return response


    def deleteEdgeConnectivity(self, connectionName):
        """
        Delete Interconnect connectivity
        
        Parameters:
        connectionName	 (string):	Edge connectivity name
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/multicloud/connectivity/edge/{connectionName}"
        response = self.client.apiCall(HttpMethods.DELETE, endpoint)
        return response


    def getEdgeConnectivityDetailByName(self, connectivityName):
        """
        Get Interconnect Connectivity by name
        
        Parameters:
        connectivityName	 (string):	IC-GW connectivity name
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/multicloud/connectivity/edge/{connectivityName}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getConnectivityGateways(self, accountId, cloudType, connectivityType, connectivityGatewayName, region, network, state, refresh):
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
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/multicloud/connectivitygateway?accountId={accountId}&cloudType={cloudType}&connectivityType={connectivityType}&connectivityGatewayName={connectivityGatewayName}&region={region}&network={network}&state={state}&refresh={refresh}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def createConnectivityGateway(self, connectivitygateway):
        """
        Create Connectivity gateway
        
        Parameters:
        connectivitygateway:	Connectivity gateway
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/multicloud/connectivitygateway"
        response = self.client.apiCall(HttpMethods.POST, endpoint, connectivitygateway)
        return response


    def cleanUpAllConnectivityGatewaysInLocalDB(self, deletionType):
        """
        Delete all Connectivity Gateways in local DB
        
        Parameters:
        deletionType	 (string):	Deletion Type
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/multicloud/connectivitygateway?deletionType={deletionType}"
        response = self.client.apiCall(HttpMethods.DELETE, endpoint)
        return response


    def deleteConnectivityGateway(self, cloudProvider, connectivityGatewayName, connectivityType):
        """
        Delete Connectivity Gateway
        
        Parameters:
        cloudProvider	 (string):	Cloud Provider
		connectivityGatewayName	 (string):	Connectivity gateway name
		connectivityType	 (string):	Cloud Connectivity Type
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/multicloud/connectivitygateway/{cloudProvider}/{connectivityGatewayName}?connectivityType={connectivityType}"
        response = self.client.apiCall(HttpMethods.DELETE, endpoint)
        return response


    def getConnectivityGatewayCreationOptions(self, accountId, cloudType, connectivityType, refresh):
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
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/multicloud/connectivitygatewaycreationoptions?accountId={accountId}&cloudType={cloudType}&connectivityType={connectivityType}&refresh={refresh}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getDashboardEdgeInfo(self):
        """
        Get interconnect edge gateway dashboard info
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/multicloud/dashboard/edge"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getWanDevices(self):
        """
        Get available WAN edge devices
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/multicloud/device"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getCloudDevicesByEdgeType(self, edgeType, edgeGatewayName):
        """
        Get cloud devices by edge type
        
        Parameters:
        edgeType	 (string):	Edge type
		edgeGatewayName	 (string):	Edge Gateway Name
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/multicloud/devices/edge/{edgeType}?edgeGatewayName={edgeGatewayName}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getCloudDevicesCloudType(self, cloudType, cgName):
        """
        Get cloud devices by cloud type
        
        Parameters:
        cloudType	 (string):	Cloud type
		cgName	 (string):	Cloud Gateway Name
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/multicloud/devices/{cloudType}?cloudGatewayName={cgName}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getEdgeWanDevices(self, edgeType):
        """
        Get available WAN edge devices
        
        Parameters:
        edgeType	 (string):	Edge Type
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/multicloud/edge/{edgeType}/device"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getIcgws(self, edgeType, accountId, region, regionId, resourceState, edgeGatewayName):
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
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/multicloud/gateway/edge?edgeType={edgeType}&accountId={accountId}&region={region}&regionId={regionId}&resourceState={resourceState}&edgeGatewayName={edgeGatewayName}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def createIcgw(self, interconnectgateway):
        """
        Create Interconnect Gateway
        
        Parameters:
        interconnectgateway:	Interconnect Gateway
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/multicloud/gateway/edge"
        response = self.client.apiCall(HttpMethods.POST, endpoint, interconnectgateway)
        return response


    def getIcgwCustomSettingDetails(self, edgeGatewayName):
        """
        Get Interconnect Gateway custom setting by Interconnect Gateway name
        
        Parameters:
        edgeGatewayName	 (string):	Edge gateway name
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/multicloud/gateway/edge/setting/{edgeGatewayName}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getIcgwTypes(self, edgeType):
        """
        Get Interconnect Gateway type for specified Edge Provider
        
        Parameters:
        edgeType	 (string):	Edge type
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/multicloud/gateway/edge/types?edgeType={edgeType}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getIcgwDetails(self, edgeGatewayName):
        """
        Get Interconnect Gateway by name
        
        Parameters:
        edgeGatewayName	 (string):	Edge gateway name
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/multicloud/gateway/edge/{edgeGatewayName}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def updateIcgw(self, gatewayInfo, edgeGatewayName):
        """
        Update Interconnect Gateway
        
        Parameters:
        gatewayInfo:	Description
		edgeGatewayName	 (string):	Edge gateway name
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/multicloud/gateway/edge/{edgeGatewayName}"
        response = self.client.apiCall(HttpMethods.PUT, endpoint, gatewayInfo)
        return response


    def deleteIcgw(self, edgeGatewayName):
        """
        Delete Interconnect Gateway
        
        Parameters:
        edgeGatewayName	 (string):	Edge gateway name
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/multicloud/gateway/edge/{edgeGatewayName}"
        response = self.client.apiCall(HttpMethods.DELETE, endpoint)
        return response


    def getEdgeGateways(self, edgeType):
        """
        Get sites with connectivity to the interconnect gateways by edge type
        
        Parameters:
        edgeType	 (string):	Edge type
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/multicloud/gateways/edge/{edgeType}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getHostVpcs(self, cloudType, accountIds, region, untagged):
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
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/multicloud/hostvpc?cloudType={cloudType}&accountIds={accountIds}&region={region}&untagged={untagged}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getVpcTags(self, cloudType, region, tagName):
        """
        Get vpc tags
        
        Parameters:
        cloudType	 (string):	Cloud type
		region	 (string):	Region
		tagName	 (string):	Tag name
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/multicloud/hostvpc/tags?cloudType={cloudType}&region={region}&tagName={tagName}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def editTag(self, vpctag):
        """
        Edit VPCs for a tag
        
        Parameters:
        vpctag:	VPC tag
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/multicloud/hostvpc/tags"
        response = self.client.apiCall(HttpMethods.PUT, endpoint, vpctag)
        return response


    def hostvpcTagging(self, vpctag):
        """
        Tag a VPC
        
        Parameters:
        vpctag:	VPC tag
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/multicloud/hostvpc/tags"
        response = self.client.apiCall(HttpMethods.POST, endpoint, vpctag)
        return response


    def unTag(self, tagName):
        """
        Delete a tag
        
        Parameters:
        tagName	 (string):	Tag name
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/multicloud/hostvpc/tags/{tagName}"
        response = self.client.apiCall(HttpMethods.DELETE, endpoint)
        return response


    def getSupportedEdgeImageNames(self, edgeType):
        """
        Get Edge provider supported images
        
        Parameters:
        edgeType	 (string):	Edge type
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/multicloud/imagename/edge?edgeType={edgeType}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getSupportedInstanceSize(self, cloudType, accountId, cloudRegion):
        """
        Get Transit VPC supported size
        
        Parameters:
        Parameter Description
		Parameter Description
		Parameter Description
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/multicloud/instancesize?cloudType={cloudType}&accountId={accountId}&cloudRegion={cloudRegion}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getSupportedEdgeInstanceSize(self, edgeType):
        """
        Get Edge provider supported size
        
        Parameters:
        edgeType	 (string):	Edge type
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/multicloud/instancesize/edge?edgeType={edgeType}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getWanInterfaceColors(self):
        """
        Get WAN interface colors
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/multicloud/interfacecolor"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getEdgeLocationsInfo(self, edgeType, accountId, region):
        """
        Get Edge Locations
        
        Parameters:
        edgeType	 (string):	Edge Type
		accountId	 (string):	Edge Account Id
		region	 (string):	Region
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/multicloud/locations/edge/{edgeType}?accountId={accountId}&region={region}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def deleteEdge(self, edgeType):
        """
        Delete edge
        
        Parameters:
        edgeType	 (string):	Edge Type
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/multicloud/locations/edge/{edgeType}"
        response = self.client.apiCall(HttpMethods.DELETE, endpoint)
        return response


    def updateEdgeLocationsInfo(self, edgeType, accountId):
        """
        Update Edge Locations
        
        Parameters:
        edgeType	 (string):	Edge Type
		accountId	 (string):	Edge Account Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/multicloud/locations/edge/{edgeType}/accountId/{accountId}"
        response = self.client.apiCall(HttpMethods.PUT, endpoint)
        return response


    def getMappingMatrix(self, cloudType):
        """
        Get default mapping values
        
        Parameters:
        cloudType	 (string):	Cloud type
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/multicloud/map?cloudType={cloudType}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def processMapping(self, vpcmapping):
        """
        Process intent of connecting VPNs with VPCs through cloud gateway
        
        Parameters:
        vpcmapping:	VPC mapping
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/multicloud/map"
        response = self.client.apiCall(HttpMethods.POST, endpoint, vpcmapping)
        return response


    def getDefaultMappingValues(self, cloudType):
        """
        Get default mapping values
        
        Parameters:
        cloudType	 (string):	Cloud type
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/multicloud/map/defaults?cloudType={cloudType}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getMappingStatus(self, cloudType, region):
        """
        Get mapping status
        
        Parameters:
        cloudType	 (string):	Cloud type
		region	 (string):	Region
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/multicloud/map/status?cloudType={cloudType}&region={region}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getMappingSummary(self, vpnTunnelStatus, cloudType):
        """
        Get mapping summary
        
        Parameters:
        vpnTunnelStatus	 (boolean):	VPN tunnel status
		cloudType	 (string):	Cloud type
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/multicloud/map/summary?vpnTunnelStatus={vpnTunnelStatus}&cloudType={cloudType}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getMappingTags(self, cloudType):
        """
        Get default mapping values
        
        Parameters:
        cloudType	 (string):	Cloud type
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/multicloud/map/tags?cloudType={cloudType}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getEdgeMappingTags(self, cloudType, accountId):
        """
        Get default Interconnect mapping tag values
        
        Parameters:
        cloudType	 (string):	Cloud type
		accountId	 (string):	Cloud Account Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/multicloud/map/tags/edge?cloudType={cloudType}&accountId={accountId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getMappingVpns(self):
        """
        Get default mapping values
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/multicloud/map/vpns"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getCgwAssociatedMappings(self, cloudType, cgName, siteUuid):
        """
        Get associated mappings to the CGW
        
        Parameters:
        cloudType	 (string):	Cloud type
		cgName	 (string):	Cloud Gateway Name
		siteUuid	 (string):	Site Device UUID
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/multicloud/mapping/{cloudType}?cloudGatewayName={cgName}&siteUuid={siteUuid}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getPartnerPorts(self, edgeType, accountId, cloudType, connectType, vxcPermitted, authorizationKey, refresh):
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
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/multicloud/partnerports/edge?edgeType={edgeType}&accountId={accountId}&cloudType={cloudType}&connectType={connectType}&vxcPermitted={vxcPermitted}&authorizationKey={authorizationKey}&refresh={refresh}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getPortSpeed(self, edgeType, edgeAccountId, connectivityType, cloudType, cloudAccountId, connectType, connectSubType, connectivityGateway, partnerPort):
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
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/multicloud/portSpeed/edge/{edgeType}/{edgeAccountId}/{connectivityType}?cloudType={cloudType}&cloudAccountId={cloudAccountId}&connectType={connectType}&connectSubType={connectSubType}&connectivityGateway={connectivityGateway}&partnerPort={partnerPort}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getCloudRegions(self, cloudType):
        """
        Get cloud regions
        
        Parameters:
        cloudType	 (string):	Cloud type
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/multicloud/regions?cloudType={cloudType}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getEdgeGlobalSettings(self, edgeType):
        """
        Get edge global settings
        
        Parameters:
        edgeType	 (string):	Edge type
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/multicloud/settings/edge/global?edgeType={edgeType}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def updateEdgeGlobalSettings(self, globalsetting):
        """
        Update edge global settings for Edge provider
        
        Parameters:
        globalsetting:	Global setting
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/multicloud/settings/edge/global"
        response = self.client.apiCall(HttpMethods.PUT, endpoint, globalsetting)
        return response


    def addEdgeGlobalSettings(self, globalsetting):
        """
        Add global settings for Edge provider
        
        Parameters:
        globalsetting:	Global setting
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/multicloud/settings/edge/global"
        response = self.client.apiCall(HttpMethods.POST, endpoint, globalsetting)
        return response


    def getGlobalSettings(self, cloudType):
        """
        Get global settings
        
        Parameters:
        cloudType	 (string):	Cloud type
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/multicloud/settings/global?cloudType={cloudType}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def updateGlobalSettings(self, globalsetting):
        """
        Update ip in resource pool
        
        Parameters:
        globalsetting:	Global setting
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/multicloud/settings/global"
        response = self.client.apiCall(HttpMethods.PUT, endpoint, globalsetting)
        return response


    def addGlobalSettings(self, globalsetting):
        """
        Acquire ip from resource pool
        
        Parameters:
        globalsetting:	Global setting
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/multicloud/settings/global"
        response = self.client.apiCall(HttpMethods.POST, endpoint, globalsetting)
        return response


    def getSites(self, color, attached):
        """
        Get available sites
        
        Parameters:
        color	 (string):	Color
		attached	 (boolean):	Is endpoint attached
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/multicloud/site?color={color}&attached={attached}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getSshKeyList(self, cloudType, accountId, cloudRegion):
        """
        Get SSH keys
        
        Parameters:
        cloudType	 (string):	Cloud type
		accountId	 (string):	Account Id
		cloudRegion	 (string):	Region
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/multicloud/sshkeys?cloudType={cloudType}&accountId={accountId}&cloudRegion={cloudRegion}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getPostAggregationDataByQuery(self, statsquerystring):
        """
        Get aggregated data based on input query and filters. The data can be filtered on time and other unique parameters based upon necessity and intended usage
        
        Parameters:
        statsquerystring:	Stats query string
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/multicloud/statistics/interface/aggregation"
        response = self.client.apiCall(HttpMethods.POST, endpoint, statsquerystring)
        return response


    def getSupportedSoftwareImageList(self, cloudType, accountId, cloudRegion):
        """
        Get software image list
        
        Parameters:
        cloudType	 (string):	Cloud type
		accountId	 (string):	Account Id
		cloudRegion	 (string):	Region
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/multicloud/swimages?cloudType={cloudType}&accountId={accountId}&cloudRegion={cloudRegion}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def telemetry(self, telemetry):
        """
        reports telemetry data
        
        Parameters:
        telemetry:	telemetry
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/multicloud/telemetry"
        response = self.client.apiCall(HttpMethods.POST, endpoint, telemetry)
        return response


    def getTunnelNames(self, cloudType, cgName):
        """
        Get tunnel names
        
        Parameters:
        cloudType	 (string):	Cloud type
		cgName	 (string):	Cloud gateway name
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/multicloud/tunnels/{cloudType}?cloudGatewayName={cgName}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getCloudTypes(self):
        """
        Get cloud types
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/multicloud/types"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getEdgeTypes(self):
        """
        Get edge types
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/multicloud/types/edge"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getVHubs(self, cloudType, accountId, resourceGroup, vWanName, vNetTags):
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
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/multicloud/vhubs?cloudType={cloudType}&accountId={accountId}&resourceGroup={resourceGroup}&vWanName={vWanName}&vNetTags={vNetTags}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def createVirtualWan(self, virtualwan):
        """
        Create Virtual WAN
        
        Parameters:
        virtualwan:	Virtual WAN
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/multicloud/vwan"
        response = self.client.apiCall(HttpMethods.POST, endpoint, virtualwan)
        return response


    def deleteVirtualWan(self, cloudProvider, vWanName):
        """
        Delete Virtual Wan
        
        Parameters:
        cloudProvider	 (string):	Cloud Provider
		vWanName	 (string):	Virtual Wan name
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/multicloud/vwan/{cloudProvider}/{vWanName}"
        response = self.client.apiCall(HttpMethods.DELETE, endpoint)
        return response


    def getVWans(self, accountId, cloudType, resourceGroup, refresh):
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
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/multicloud/vwans?accountId={accountId}&cloudType={cloudType}&resourceGroup={resourceGroup}&refresh={refresh}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getEdgeWidget(self, edgeType):
        """
        Get Interconnect Edge widget by edge type
        
        Parameters:
        edgeType	 (string):	Edge type
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/multicloud/widget/edge/{edgeType}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getCloudWidget(self, cloudType):
        """
        Get cloud widget by cloud type
        
        Parameters:
        cloudType	 (string):	Cloud type
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/multicloud/widget/{cloudType}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


