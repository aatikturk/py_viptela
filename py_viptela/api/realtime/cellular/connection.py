from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class Connection(object):
    """
    Real-Time Monitoring - Cellular EIOLTE Connection Service API
    
    Implements GET POST DEL PUT methods for CellularEIOLTEConnectionService endpoints

    """

    def __init__(self, session, host, port):
        self.host = host
        self.port = port
        self.client = HttpMethods.HttpClient(session=session)
    
    
    def getConnInfo(self, deviceId):
        """
        Get cellular connection info from device
        
        Parameters:
        deviceId	 (string):	Device Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/cellularEiolte/connections?deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getRadioInfo(self, deviceId):
        """
        Get cellular radio info from device
        
        Parameters:
        deviceId	 (string):	Device Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/cellularEiolte/radio?deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


