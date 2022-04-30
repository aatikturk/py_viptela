from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class Cexp(object):
    """
    Real-Time Monitoring - CloudExpress API
    
    Implements GET POST DEL PUT methods for CloudExpress endpoints

    """

    def __init__(self, session, host, port):
        self.host = host
        self.port = port
        self.client = HttpMethods.HttpClient(session=session)
    
    
    def createApplicationsDetailList(self, vpnId, application, query):
        """
        Get list of cloudexpress applications from device (Real Time)
        
        Parameters:
        vpnId	 (string):	VPN Id
		application	 (string):	Application
		query	 (string):	Query
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/cloudx/application/detail?vpnId={vpnId}&application={application}&query={query}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def createApplicationsList(self, vpnId, application, query):
        """
        Get list of cloudexpress applications from device (Real Time)
        
        Parameters:
        vpnId	 (string):	VPN Id
		application	 (string):	Application
		query	 (string):	Query
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/cloudx/applications?vpnId={vpnId}&application={application}&query={query}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def createGatewayExitsList(self, vpnId, application, deviceId):
        """
        Get list of cloudexpress gateway exits from device (Real Time)
        
        Parameters:
        vpnId	 (string):	VPN Id
		application	 (string):	Application
		deviceId	 (string):	Device IP
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/cloudx/gatewayexits?vpnId={vpnId}&application={application}&deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def createLbApplicationsList(self, vpnId, application, query):
        """
        Get list of cloudexpress load balance applications from device (Real Time)
        
        Parameters:
        vpnId	 (string):	VPN Id
		application	 (string):	Application
		query	 (string):	Query
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/cloudx/loadbalance?vpnId={vpnId}&application={application}&query={query}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def createLocalExitsList(self, vpnId, application, deviceId):
        """
        Get list of cloudexpress local exits from device (Real Time)
        
        Parameters:
        vpnId	 (string):	VPN Id
		application	 (string):	Application
		deviceId	 (string):	Device IP
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/cloudx/localexits?vpnId={vpnId}&application={application}&deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


