from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class AppLogs(object):
    """
    Real-Time Monitoring - App Logs API
    
    Implements GET POST DEL PUT methods for AppLogs endpoints

    """

    def __init__(self, session, host, port):
        self.host = host
        self.port = port
        self.client = HttpMethods.HttpClient(session=session)
    
    
    def getFlowCount(self, deviceId):
        """
        Get App log flows count from device (Real Time)
        
        Parameters:
        deviceId	 (string):	Device IP
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/app/log/flow-count?deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getFlows(self, deviceId):
        """
        Get App log flows from device (Real Time)
        
        Parameters:
        deviceId	 (string):	Device IP
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/app/log/flows?deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


