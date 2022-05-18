from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class Dot1x(object):
    """
    Real-Time Monitoring - DOT1x API
    
    Implements GET POST DEL PUT methods for DOT1x endpoints

    """

    def __init__(self, session, host, port):
        self.host = host
        self.port = port
        self.client = HttpMethods.HttpClient(session=session)
    
    
    def getClients(self, deviceId):
        """
        Get DOT1x client from device (Real Time)
        
        Parameters:
        deviceId	 (string):	Device IP
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/dot1x/clients?deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getInterfaces(self, deviceId):
        """
        Get DOT1x interface from device (Real Time)
        
        Parameters:
        deviceId	 (string):	Device IP
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/dot1x/interfaces?deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getRadius(self, deviceId):
        """
        Get DOT1x Radius from device (Real Time)
        
        Parameters:
        deviceId	 (string):	Device IP
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/dot1x/radius?deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


