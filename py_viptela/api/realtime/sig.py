from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class SIG(object):
    """
    Real-Time Monitoring - SIG API
    
    Implements GET POST DEL PUT methods for SIG endpoints

    """

    def __init__(self, session, host, port):
        self.client = HttpMethods.HttpClient(session=session)
        self.host = host
        self.port = port
    
    
    def getUmbrella(self, deviceId):
        """
        Get SIG Umbrella tunnels from device
        
        Parameters:
        deviceId	 (string):	Device Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/sig/umbrella/tunnels?deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getZscaler(self, deviceId):
        """
        Get SIG Zscaler tunnels from device
        
        Parameters:
        deviceId	 (string):	Device Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/sig/zscaler/tunnels?deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


