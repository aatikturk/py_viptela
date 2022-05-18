from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class Security(object):
    """
    Real-Time Monitoring - Security API
    
    Implements GET POST DEL PUT methods for Security endpoints

    """

    def __init__(self, session, host, port):
        self.client = HttpMethods.HttpClient(session=session)
        self.host = host
        self.port = port
    
    
    def getSessionList(self, deviceId):
        """
        Get security information from devices
        
        Parameters:
        deviceId	 (string):	Device Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/security/information?deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


