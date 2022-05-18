from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class Tracker(object):
    """
    Real-Time Monitoring - Endpoint Tracker Service API
    
    Implements GET POST DEL PUT methods for EndpointTrackerService endpoints

    """

    def __init__(self, session, host, port):
        self.host = host
        self.port = port
        self.client = HttpMethods.HttpClient(session=session)
    
    
    def getInfo(self, deviceId):
        """
        Get endpoint tracker info from device
        
        Parameters:
        deviceId	 (string):	Device Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/endpointTracker?deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


