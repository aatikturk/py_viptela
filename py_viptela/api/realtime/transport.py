from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class Transport(object):
    """
    Real-Time Monitoring - Transport API
    
    Implements GET POST DEL PUT methods for Transport endpoints

    """

    def __init__(self, session, host, port):
        self.client = HttpMethods.HttpClient(session=session)
        self.host = host
        self.port = port
    
    
    def getConnList(self, deviceId):
        """
        Get transport connection list from device
        
        Parameters:
        deviceId	 (string):	Device Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/transport/connection?deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


