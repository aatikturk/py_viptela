from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class CloudOnRamp(object):
    """
    Configuration - Cloud On Ramp API
    
    Implements GET POST DEL PUT methods for CloudOnRamp endpoints

    """

    def __init__(self, session, host, port):
        self.client = HttpMethods.HttpClient(session=session)
        self.host = host
        self.port = port
    
    
    def getCORStatus(self):
        """
        Get Cloud On Ramp list
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/cor"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def createAndMap(self, request):
        """
        Map Host to Transit VPC/VNet
        
        Parameters:
        request:	Map host to transit VPC request
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/cor"
        response = self.client.apiCall(HttpMethods.POST, endpoint, request)
        return response


    def raiseAlarmForAccount(self, accountobject):
        """
        Raise alarm for account
        
        Parameters:
        accountobject:	Account object
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/cor/account/alarm"
        response = self.client.apiCall(HttpMethods.POST, endpoint, accountobject)
        return response


    def removeTransitVPC(self, accountid, transitvpcid, cloudregion, cloudtype):
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
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/cor/accountid/{accountid}?transitvpcid={transitvpcid}&cloudregion={cloudregion}&cloudtype={cloudtype}"
        response = self.client.apiCall(HttpMethods.DELETE, endpoint)
        return response


    def acquireRP(self, request):
        """
        Acquire IP from resource pool
        
        Parameters:
        request:	Add IP from resource pool request
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/cor/acquireResourcePool"
        response = self.client.apiCall(HttpMethods.POST, endpoint, request)
        return response


    def getAmiList(self, accountid, cloudregion, cloudtype):
        """
        Get AMI list
        
        Parameters:
        accountid	 (string):	Account Id
		cloudregion	 (string):	Cloud region
		cloudtype	 (string):	Cloud type
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/cor/ami?accountid={accountid}&cloudregion={cloudregion}&cloudtype={cloudtype}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getCloudList(self):
        """
        Get cloud list
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/cor/cloud"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getCloudAccounts(self, cloudtype, cloudEnvironment):
        """
        Get cloud accounts
        
        Parameters:
        cloudtype	 (string):	Cloud type
		cloudEnvironment	 (string):	Cloud environment
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/cor/cloud/account?cloudtype={cloudtype}&cloudEnvironment={cloudEnvironment}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def authCredAndUpdate(self, credential):
        """
        Authenticate and update cloud account credentials
        
        Parameters:
        credential:	Cloud account credential
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/cor/cloud/authenticate"
        response = self.client.apiCall(HttpMethods.PUT, endpoint, credential)
        return response


    def authCORCredAndAdd(self, credential):
        """
        Authenticate cloud account credentials
        
        Parameters:
        credential:	Cloud account credential
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/cor/cloud/authenticate"
        response = self.client.apiCall(HttpMethods.POST, endpoint, credential)
        return response


    def getCloudHostVpcAccountDetails(self):
        """
        Get cloud host VPC account details
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/cor/cloud/host/accountdetails"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getCloudMappedHostAccounts(self, accountid, cloudtype):
        """
        Get cloud mapped accounts view
        
        Parameters:
        accountid	 (string):	Account Id
		cloudtype	 (string):	Cloud type
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/cor/cloud/mappedhostaccounts?accountid={accountid}&cloudtype={cloudtype}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def createRP(self, request):
        """
        Add resource pool
        
        Parameters:
        request:	Add resource pool request
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/cor/createResourcePool"
        response = self.client.apiCall(HttpMethods.POST, endpoint, request)
        return response


    def removeDeviceId(self, accountid, transitvpcid, transitvpcname, cloudregion, cloudtype, devicePairId):
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
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/cor/deleteDevicepair?accountid={accountid}&transitvpcid={transitvpcid}&transitvpcname={transitvpcname}&cloudregion={cloudregion}&cloudtype={cloudtype}&devicePairId={devicePairId}"
        response = self.client.apiCall(HttpMethods.DELETE, endpoint)
        return response


    def getCORDevices(self):
        """
        Get available device list
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/cor/device"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def addDevicePair(self, request):
        """
        Add device pair
        
        Parameters:
        request:	Add device pair request
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/cor/devicepair"
        response = self.client.apiCall(HttpMethods.POST, endpoint, request)
        return response


    def getHostVPCs(self, transitVpcId, devicePairId):
        """
        Get host VPC details
        
        Parameters:
        transitVpcId	 (string):	Transit VPC Id
		devicePairId	 (string):	Device pair Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/cor/devicepair/hostvpc?transitVpcId={transitVpcId}&devicePairId={devicePairId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getExternalId(self):
        """
        Get the vManage external ID for AWS
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/cor/externalId"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getTransitDevicePairAndHostList(self, accountId, cloudRegion):
        """
        Get device and host details
        
        Parameters:
        accountId	 (string):	Account Id
		cloudRegion	 (string):	Cloud region
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/cor/getTransitDevicePairAndHostList?accountId={accountId}&cloudRegion={cloudRegion}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getTransitVpcVpnList(self, accountId):
        """
        Get transit VPN list
        
        Parameters:
        accountId	 (string):	Account Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/cor/getTransitVpnList?accountId={accountId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getCloudHostVPCs(self, accountid, cloudregion, cloudtype):
        """
        Get host VPC/VNet list
        
        Parameters:
        accountid	 (string):	Account Id
		cloudregion	 (string):	Cloud region
		cloudtype	 (string):	Cloud type
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/cor/hostvpc?accountid={accountid}&cloudregion={cloudregion}&cloudtype={cloudtype}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getTenantAndHostVpcList(self, intent):
        """
        Get tenant and host VPC list
        
        Parameters:
        intent	 (string):	Intent
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/cor/hostvpclist?intent={intent}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def updateHostVpcReachability(self, updatevpcstatus):
        """
        Update host VPC reachability
        
        Parameters:
        updatevpcstatus:	Update VPC status
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/cor/hostvpclist"
        response = self.client.apiCall(HttpMethods.PUT, endpoint, updatevpcstatus)
        return response


    def getMappedVPCs(self, accountid, cloudregion):
        """
        Get mapped VPC/VNet list
        
        Parameters:
        accountid	 (string):	Account Id
		cloudregion	 (string):	Cloud region
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/cor/map?accountid={accountid}&cloudregion={cloudregion}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def mapVPCs(self, host):
        """
        Map host to transit VPC/VNet
        
        Parameters:
        host:	Map host to VPC/VNet
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/cor/map"
        response = self.client.apiCall(HttpMethods.POST, endpoint, host)
        return response


    def unmapVPCs(self, host):
        """
        Unmap host from transit VPC/VNet
        
        Parameters:
        host:	Unmap host to VPC/VNet
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/cor/map"
        response = self.client.apiCall(HttpMethods.DELETE, endpoint, host)
        return response


    def getPemKeyList(self, accountid, cloudregion, cloudtype):
        """
        Get transit VPC PEM key list
        
        Parameters:
        accountid	 (string):	Account Id
		cloudregion	 (string):	Cloud region
		cloudtype	 (string):	Cloud type
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/cor/pem?accountid={accountid}&cloudregion={cloudregion}&cloudtype={cloudtype}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def scaleDown(self, updatevpc):
        """
        Scale down cloud on ramp
        
        Parameters:
        updatevpc:	Update VPC
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/cor/scale/down"
        response = self.client.apiCall(HttpMethods.POST, endpoint, updatevpc)
        return response


    def scaleUp(self, updatevpc):
        """
        Scale up cloud on ramp
        
        Parameters:
        updatevpc:	Update VPC
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/cor/scale/up"
        response = self.client.apiCall(HttpMethods.POST, endpoint, updatevpc)
        return response


    def updatestatus(self, statusobject):
        """
        Update task status
        
        Parameters:
        statusobject:	Status object
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/cor/status"
        response = self.client.apiCall(HttpMethods.POST, endpoint, statusobject)
        return response


    def getTransitVPCs(self, accountid, cloudregion, cloudtype):
        """
        Get transit VPC/VNet list
        
        Parameters:
        accountid	 (string):	Account Id
		cloudregion	 (string):	Cloud region
		cloudtype	 (string):	Cloud type
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/cor/transitvpc?accountid={accountid}&cloudregion={cloudregion}&cloudtype={cloudtype}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def updateTransitVPC(self, vpc):
        """
        Update transit VPC/VNet
        
        Parameters:
        vpc:	VPC
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/cor/transitvpc"
        response = self.client.apiCall(HttpMethods.PUT, endpoint, vpc)
        return response


    def addTransitVPC(self, vpc):
        """
        Create transit VPC/VNet
        
        Parameters:
        vpc:	VPC
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/cor/transitvpc"
        response = self.client.apiCall(HttpMethods.POST, endpoint, vpc)
        return response


    def updateTransitVpcAutoscaleProperties(self, vpc):
        """
        Update transit VPC autoscale properties
        
        Parameters:
        vpc:	VPC
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/cor/transitvpc/autoscale-properties"
        response = self.client.apiCall(HttpMethods.PUT, endpoint, vpc)
        return response


    def getTransitVPCSupportedSize(self, cloudtype, cloudEnvironment):
        """
        Get transit VPC supported size
        
        Parameters:
        cloudtype	 (string):	Cloud type
		cloudEnvironment	 (string):	Cloud environment
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/cor/transitvpc/size?cloudtype={cloudtype}&cloudEnvironment={cloudEnvironment}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


