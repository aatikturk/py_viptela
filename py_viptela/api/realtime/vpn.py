from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class VPN(object):
    """
    Real-Time Monitoring - VPN API
    
    Implements GET POST DEL PUT methods for VPN endpoints

    """

    def __init__(self, session, host, port):
        self.client = HttpMethods.HttpClient(session=session)
        self.host = host
        self.port = port
    
    
    def getVPNInstances(self, deviceId):
        """
        Get VPN instance list from device (Real Time)
        
        Parameters:
        deviceId	 (string):	Device Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/vpn?deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


