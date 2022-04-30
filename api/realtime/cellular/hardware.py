from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class Hardware(object):
    """
    Real-Time Monitoring - Cellular EIOLTE Hardware Service  API
    
    Implements GET POST DEL PUT methods for CellularEIOLTEHardwareService endpoints

    """

    def __init__(self, session, host, port):
        self.host = host
        self.port = port
        self.client = HttpMethods.HttpClient(session=session)
    
    
    def getHardwareInfo(self, deviceId):
        """
        Get cellular hardware info from device
        
        Parameters:
        deviceId	 (string):	Device Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/cellularEiolte/hardware?deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


