from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class History(object):
    """
    Real-Time Monitoring - Reboot History API
    
    Implements GET POST DEL PUT methods for RebootHistory endpoints

    """

    def __init__(self, session, host, port):
        self.client = HttpMethods.HttpClient(session=session)
        self.host = host
        self.port = port
    
    
    def getList(self, deviceId):
        """
        Get device reboot history
        
        Parameters:
        deviceId	 (string):	Device IP
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/reboothistory?deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getDetails(self):
        """
        Get detailed reboot history list
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/reboothistory/details"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getSyncedList(self, deviceId):
        """
        Get device reboot history synchronously
        
        Parameters:
        deviceId	 (string):	Device IP
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/reboothistory/synced?deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


