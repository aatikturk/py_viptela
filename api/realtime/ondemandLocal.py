from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class OdLocal(object):
    """
    Real-Time Monitoring - Show On Demand Local API
    
    Implements GET POST DEL PUT methods for ShowOnDemandLocal endpoints

    """

    def __init__(self, session, host, port):
        self.client = HttpMethods.HttpClient(session=session)
        self.host = host
        self.port = port
    
    
    def get(self, deviceId):
        """
        Get on-demand local (Real Time)
        
        Parameters:
        deviceId	 (string):	Device Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/ondemand/local?deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


