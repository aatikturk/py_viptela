from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class Sim(object):
    """
    Real-Time Monitoring - Cellular EIOLTE Sim Service API
    
    Implements GET POST DEL PUT methods for CellularEIOLTESimService endpoints

    """

    def __init__(self, session, host, port):
        self.host = host
        self.port = port
        self.client = HttpMethods.HttpClient(session=session)
    
    
    def getSimInfo(self, deviceId):
        """
        Get cellular sim info from device
        
        Parameters:
        deviceId	 (string):	Device Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/cellularEiolte/sim?deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


