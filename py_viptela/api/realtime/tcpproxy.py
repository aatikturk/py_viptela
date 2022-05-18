from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class Tcpproxy(object):
    """
    Real-Time Monitoring - Tcpproxy API
    
    Implements GET POST DEL PUT methods for Tcpproxy endpoints

    """

    def __init__(self, session, host, port):
        self.client = HttpMethods.HttpClient(session=session)
        self.host = host
        self.port = port
    
    
    def getStats(self, deviceId):
        """
        Get tcp proxy statistics from device
        
        Parameters:
        deviceId	 (string):	Device Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/tcpproxy/statistics?deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getStatus(self, deviceId):
        """
        Get tcp proxy status from device
        
        Parameters:
        deviceId	 (string):	Device Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/tcpproxy/status?deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


