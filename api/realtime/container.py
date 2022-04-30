from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class Container(object):
    """
    Real-Time Monitoring - Container Lifecycle API
    
    Implements GET POST DEL PUT methods for ContainerLifecycle endpoints

    """

    def __init__(self, session, host, port):
        self.host = host
        self.port = port
        self.client = HttpMethods.HttpClient(session=session)
    
    
    def getDeviceInfo(self, deviceId):
        """
        Get device container from device (Real Time)
        
        Parameters:
        deviceId	 (string):	Device Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/csp/containers/container?deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


