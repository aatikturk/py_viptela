from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class VRRP(object):
    """
    Real-Time Monitoring - VRRP API
    
    Implements GET POST DEL PUT methods for VRRP endpoints

    """

    def __init__(self, session, host, port):
        self.client = HttpMethods.HttpClient(session=session)
        self.host = host
        self.port = port
    
    
    def getIf(self, deviceId):
        """
        Get VRRP interface list from device
        
        Parameters:
        deviceId	 (string):	Device IP
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/vrrp?deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


