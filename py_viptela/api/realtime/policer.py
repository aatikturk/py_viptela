from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class Policer(object):
    """
    Real-Time Monitoring - Policer API
    
    Implements GET POST DEL PUT methods for Policer endpoints

    """

    def __init__(self, session, host, port):
        self.client = HttpMethods.HttpClient(session=session)
        self.host = host
        self.port = port
    
    
    def getPolicedInterface(self, deviceId):
        """
        Get policed interface list from device
        
        Parameters:
        deviceId	 (string):	Device Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/policer?deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


