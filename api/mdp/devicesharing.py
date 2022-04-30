from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class DeviceSharing(object):
    """
    MDP - Device Sharing API
    
    Implements GET POST DEL PUT methods for Device Sharing endpoints

    """

    def __init__(self, session, host, port):
        self.host = host
        self.port = port
        self.client = HttpMethods.HttpClient(session=session)
    
    
    def getAttached(self, nmsId):
        """
        Retrieve MDP attached devices
        
        Parameters:
        Parameter Description
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/mdp/attachDevices/{nmsId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def editAttached(self, devicelist, nmsId):
        """
        Edit attached devices
        
        Parameters:
        devicelist:	deviceList
		Parameter Description
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/mdp/attachDevices/{nmsId}"
        response = self.client.apiCall(HttpMethods.PUT, endpoint, devicelist)
        return response


    def attach(self, devicelist, nmsId):
        """
        Share devices with MDP
        
        Parameters:
        devicelist:	deviceList
		Parameter Description
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/mdp/attachDevices/{nmsId}"
        response = self.client.apiCall(HttpMethods.POST, endpoint, devicelist)
        return response


    def detach(self, devicelist, nmsId):
        """
        Disconnect devices from mpd controller
        
        Parameters:
        devicelist:	deviceList
		Parameter Description
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/mdp/detachDevices/{nmsId}"
        response = self.client.apiCall(HttpMethods.POST, endpoint, devicelist)
        return response


    def getSupported(self, nmsId):
        """
        Retrieve MDP supported devices
        
        Parameters:
        Parameter Description
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/mdp/devices/{nmsId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


