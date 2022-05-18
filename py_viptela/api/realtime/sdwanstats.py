from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class SDWAN(object):
    """
    Real-Time Monitoring - SDWAN Statistics API
    
    Implements GET POST DEL PUT methods for SDWANStatistics endpoints

    """

    def __init__(self, session, host, port):
        self.client = HttpMethods.HttpClient(session=session)
        self.host = host
        self.port = port
    
    
    def getGlobalDropStats(self, deviceId):
        """
        Get SD-WAN global drop statistics detail from device (Real Time)
        
        Parameters:
        deviceId	 (string):	Device IP
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/sdwan-global-drop-statistics?deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getStats(self, deviceId):
        """
        Get SD-WAN statistics detail from device (Real Time)
        
        Parameters:
        deviceId	 (string):	Device IP
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/sdwan-stats?deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


