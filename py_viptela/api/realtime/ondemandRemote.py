from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class OdRemote(object):
    """
    Real-Time Monitoring - Show On Demand Remote API
    
    Implements GET POST DEL PUT methods for ShowOnDemandRemote endpoints

    """

    def __init__(self, session, host, port):
        self.client = HttpMethods.HttpClient(session=session)
        self.host = host
        self.port = port
    
    
    def get(self, deviceId):
        """
        Get on-demand remote (Real Time)
        
        Parameters:
        deviceId	 (string):	Device Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/ondemand/remote?deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


