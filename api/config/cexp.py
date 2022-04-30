from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class CloudExpress(object):
    """
    Configuration - CloudExpress API
    
    Implements GET POST DEL PUT methods for CloudExpress endpoints

    """

    def __init__(self, session, host, port):
        self.client = HttpMethods.HttpClient(session=session)
        self.host = host
        self.port = port
    
    
    def getCloudXStatus(self):
        """
        Get CloudX feature list
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/cloudx"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def addCloudxType(self, cloudx, type):
        """
        Add cloudx gateway
        
        Parameters:
        cloudx:	Cloudx
		type	 (string):	Cloudx type
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/cloudx/addcloudx/{type}"
        response = self.client.apiCall(HttpMethods.POST, endpoint, cloudx)
        return response


    def getAttachedClientList(self):
        """
        Get attached client site list
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/cloudx/attachedclient"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getAttachedDiaList(self):
        """
        Get attached Dia site list
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/cloudx/attacheddia"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getAttachedGwList(self):
        """
        Get attached gateway list
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/cloudx/attachedgateway"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getCloudXAvailableApps(self):
        """
        Get CloudX available apps list
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/cloudx/availableapps"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getSiteList(self):
        """
        Get site list
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/cloudx/clientlist"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getDiaList(self):
        """
        Get Dia site list
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/cloudx/dialist"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getGwList(self):
        """
        Get gateway list
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/cloudx/gatewaylist"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def addCloudxInterfaces(self, cloudx):
        """
        Enable cloudx gateway
        
        Parameters:
        cloudx:	Cloudx
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/cloudx/interfaces"
        response = self.client.apiCall(HttpMethods.POST, endpoint, cloudx)
        return response


    def getApps(self):
        """
        Get apps and vpns
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/cloudx/manage/apps"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def editApps(self, appVPN):
        """
        Edit apps and vpns
        
        Parameters:
        appVPN:	Cloudx apps and vpns
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/cloudx/manage/apps"
        response = self.client.apiCall(HttpMethods.PUT, endpoint, appVPN)
        return response


    def addApps(self, appVPN):
        """
        Add apps and vpns
        
        Parameters:
        appVPN:	Cloudx apps and vpns
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/cloudx/manage/apps"
        response = self.client.apiCall(HttpMethods.POST, endpoint, appVPN)
        return response


    def sitePerApp(self, appName, vpnId):
        """
        Get sites per application per vpn
        
        Parameters:
        appName	 (string):	App name
		vpnId	 (integer):	VPN Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/cloudx/status?appName={appName}&vpnId={vpnId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


