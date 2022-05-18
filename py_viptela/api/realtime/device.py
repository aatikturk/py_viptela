from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class Device(object):
    """
    Real-Time Monitoring - Device API
    
    Implements GET POST DEL PUT methods for Device endpoints

    """

    def __init__(self, session, host, port):
        self.host = host
        self.port = port
        self.client = HttpMethods.HttpClient(session=session)
    
    
    def getV6Data(self, deviceId):
        """
        Get ipv6 data from device
        
        Parameters:
        Parameter Description
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/ipv6/nd6?deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


