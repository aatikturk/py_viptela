from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class Network(object):
    """
    Real-Time Monitoring - Cellular EIOLTE Network Service API
    
    Implements GET POST DEL PUT methods for CellularEIOLTENetworkService endpoints

    """

    def __init__(self, session, host, port):
        self.host = host
        self.port = port
        self.client = HttpMethods.HttpClient(session=session)
    
    
    def getNetworkInfo(self, deviceId):
        """
        Get cellular network  info from device
        
        Parameters:
        deviceId	 (string):	Device Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/cellularEiolte/network?deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


