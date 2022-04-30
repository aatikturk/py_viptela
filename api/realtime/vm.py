from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class VM(object):
    """
    Real-Time Monitoring - VM API
    
    Implements GET POST DEL PUT methods for VM endpoints

    """

    def __init__(self, session, host, port):
        self.client = HttpMethods.HttpClient(session=session)
        self.host = host
        self.port = port
    
    
    def getVbranchNics(self, deviceId):
        """
        Get vbranch vm lifecycle state (NIC)
        
        Parameters:
        deviceId	 (string):	Device IP
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/vm/nics?deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getCloudDockNics(self, userGroup):
        """
        Get CloudDock vm lifecycle state
        
        Parameters:
        userGroup	 (string):	userGroup Name
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/vm/notifications?userGroup={userGroup}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getVbranch(self, deviceId):
        """
        Get vbranch vm lifecycle state
        
        Parameters:
        deviceId	 (string):	Device IP
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/vm/oper/state?deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getState(self, deviceId):
        """
        Get vm lifecycle state
        
        Parameters:
        deviceId	 (string):	Device IP
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/vm/state?deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


