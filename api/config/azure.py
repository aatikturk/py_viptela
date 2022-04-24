from query_builder import Builder
import HttpMethods

class Azure(object):
    """
    Configuration - Azure Connect API
    
    Implements GET POST DEL PUT methods for AzureConnect endpoints

    """

    def __init__(self, session, host, port):
        self.client = HttpMethods.HttpClient(session=session)
        self.host = host
        self.port = port
    
    
    def getCortexStatus(self):
        """
        Get Cortex List
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/cortex"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def authenticateAzureConnectCredAndAdd(self, credential):
        """
        Authenticate Cloud Account Credentials
        
        Parameters:
        credential:	Credential
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/cortex/cloud/authenticate"
        response = self.client.apiCall(HttpMethods.POST, endpoint, credential)
        return response


    def getMappedWanResourceGroups(self, accountid, cloudregion):
        """
        Get Mapped WAN Resource Groups
        
        Parameters:
        accountid	 (string):	Account Id
		cloudregion	 (string):	Cloud region
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/cortex/map?accountid={accountid}&cloudregion={cloudregion}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def syncWanResourceGroups(self, wanresourcegroup):
        """
        Sync WAN Resource Groups
        
        Parameters:
        wanresourcegroup:	WAN resource group
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/cortex/sync"
        response = self.client.apiCall(HttpMethods.POST, endpoint, wanresourcegroup)
        return response


    def getWanResourceGroups(self, accountid):
        """
        Get WAN Resource Groups
        
        Parameters:
        accountid	 (string):	Account Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/cortex/wanrg?accountid={accountid}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def editWanResourceGroups(self, wanresourcegroup):
        """
        Edit WAN Resource Groups
        
        Parameters:
        wanresourcegroup:	WAN resource group
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/cortex/wanrg"
        response = self.client.apiCall(HttpMethods.PUT, endpoint, wanresourcegroup)
        return response


    def saveWanResourceGroups(self, wanresourcegroup):
        """
        Create WAN Resource Groups
        
        Parameters:
        wanresourcegroup:	WAN resource group
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/cortex/wanrg"
        response = self.client.apiCall(HttpMethods.POST, endpoint, wanresourcegroup)
        return response


    def deleteWanResourceGroups(self, wanresourcegroup):
        """
        Delete WAN Resource Groups
        
        Parameters:
        wanresourcegroup:	WAN resource group
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/cortex/wanrg"
        response = self.client.apiCall(HttpMethods.DELETE, endpoint, wanresourcegroup)
        return response


