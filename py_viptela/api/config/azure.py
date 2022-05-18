from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

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


    def authAzureCredAndAdd(self, credential):
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


    def getMappedWanRG(self, accountid, cloudregion):
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


    def syncWanRG(self, wanRG):
        """
        Sync WAN Resource Groups
        
        Parameters:
        wanRG:	WAN resource group
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/cortex/sync"
        response = self.client.apiCall(HttpMethods.POST, endpoint, wanRG)
        return response


    def getWanRG(self, accountid):
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


    def editWanRG(self, wanRG):
        """
        Edit WAN Resource Groups
        
        Parameters:
        wanRG:	WAN resource group
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/cortex/wanrg"
        response = self.client.apiCall(HttpMethods.PUT, endpoint, wanRG)
        return response


    def saveWanRG(self, wanRG):
        """
        Create WAN Resource Groups
        
        Parameters:
        wanRG:	WAN resource group
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/cortex/wanrg"
        response = self.client.apiCall(HttpMethods.POST, endpoint, wanRG)
        return response


    def deleteWanRG(self, wanRG):
        """
        Delete WAN Resource Groups
        
        Parameters:
        wanRG:	WAN resource group
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/cortex/wanrg"
        response = self.client.apiCall(HttpMethods.DELETE, endpoint, wanRG)
        return response


