from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class Feature(object):
    """
    Real-Time Monitoring - Device Feature List API
    
    Implements GET POST DEL PUT methods for DeviceFeatureList endpoints

    """

    def __init__(self, session, host, port):
        self.host = host
        self.port = port
        self.client = HttpMethods.HttpClient(session=session)
    
    
    def getList(self, deviceId):
        """
        Get feature lists from device (Real Time)
        
        Parameters:
        deviceId	 (string):	Device Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/featurelist?deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getSyncedList(self, deviceId):
        """
        Get feature lists synchronously from device
        
        Parameters:
        deviceId	 (string):	Device Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/featurelist/synced?deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


