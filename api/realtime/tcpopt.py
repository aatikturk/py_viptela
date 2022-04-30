from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class TCPOptimization(object):
    """
    Real-Time Monitoring - TCP Optimization API
    
    Implements GET POST DEL PUT methods for TCPOptimization endpoints

    """

    def __init__(self, session, host, port):
        self.client = HttpMethods.HttpClient(session=session)
        self.host = host
        self.port = port
    
    
    def getActiveTCPFlows(self, deviceId):
        """
        Get TCP optimized active flows from device (Real Time)
        
        Parameters:
        deviceId	 (string):	Device IP
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/tcpopt/activeflows?deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getExpiredTCPFlows(self, deviceId):
        """
        Get TCP optimized expired flows from device (Real Time)
        
        Parameters:
        deviceId	 (string):	Device IP
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/tcpopt/expiredflows?deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getTCPSummary(self, deviceId):
        """
        Get TCP optimization summary from device (Real Time)
        
        Parameters:
        deviceId	 (string):	Device IP
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/tcpopt/summary?deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


