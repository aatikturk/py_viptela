from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class Resource(object):
    """
    Real-Time Monitoring - NetworkHub Resources API
    
    Implements GET POST DEL PUT methods for NetworkHubResources endpoints

    """

    def __init__(self, session, host, port):
        self.client = HttpMethods.HttpClient(session=session)
        self.host = host
        self.port = port
    
    
    def getAllocInfo(self, deviceId):
        """
        Get NetworkHub CPU allocation info from device
        
        Parameters:
        deviceId	 (string):	Device Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/csp/resources/cpu-info/allocation?deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getCPUInfo(self, deviceId):
        """
        Get NetworkHub CPU info from device
        
        Parameters:
        deviceId	 (string):	Device Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/csp/resources/cpu-info/cpus?deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getVNFInfo(self, deviceId):
        """
        Get NetworkHub CPU VNF info from device
        
        Parameters:
        deviceId	 (string):	Device Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/csp/resources/cpu-info/vnfs?deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


