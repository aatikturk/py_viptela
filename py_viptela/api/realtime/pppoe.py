from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class PPPOE(object):
    """
    Real-Time Monitoring - PPPoE API
    
    Implements GET POST DEL PUT methods for PPPoE endpoints

    """

    def __init__(self, session, host, port):
        self.client = HttpMethods.HttpClient(session=session)
        self.host = host
        self.port = port
    
    
    def getInterfaceList(self, deviceId):
        """
        Get PPPoE session list from device
        
        Parameters:
        Parameter Description
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/pppoe/session?deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getNeighborList(self, deviceId):
        """
        Get PPPoE statistics from device
        
        Parameters:
        Parameter Description
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/pppoe/statistic?deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


