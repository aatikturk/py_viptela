from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class ARP(object):
    """
    Real-Time Monitoring - ARP API
    
    Implements GET POST DEL PUT methods for ARP endpoints

    """

    def __init__(self, session, host, port):
        self.host = host
        self.port = port
        self.client = HttpMethods.HttpClient(session=session)
    
    
    def getInterface(self, deviceId):
        """
        Get ARP interfaces from device (Real Time)
        
        Parameters:
        deviceId	 (string):	Device IP
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/arp?deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


