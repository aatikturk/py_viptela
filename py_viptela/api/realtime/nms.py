from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class NMS(object):
    """
    Real-Time Monitoring - NMS API
    
    Implements GET POST DEL PUT methods for NMS endpoints

    """

    def __init__(self, session, host, port):
        self.client = HttpMethods.HttpClient(session=session)
        self.host = host
        self.port = port
    
    
    def getRunning(self, deviceId):
        """
        Get nms running state from device
        
        Parameters:
        deviceId	 (string):	Device Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/nms/running?deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


