from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class Topology(object):
    """
    Configuration - Topology API
    
    Implements GET POST DEL PUT methods for Topology endpoints

    """

    def __init__(self, session, host, port):
        self.client = HttpMethods.HttpClient(session=session)
        self.host = host
        self.port = port
    
    
    def createFull(self):
        """
        Create full topology
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/topology"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def createDevice(self, deviceId):
        """
        Create device topology
        
        Parameters:
        deviceId	 (array):	Device Id list
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/topology/device?deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def createPhysical(self, deviceId):
        """
        Create pysical topology
        
        Parameters:
        deviceId	 (array):	Device Id list
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/topology/physical?deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


