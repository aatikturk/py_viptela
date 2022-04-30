from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class Status(object):
    """
    Monitoring - Status API
    
    Implements GET POST DEL PUT methods for Status endpoints

    """

    def __init__(self, session, host, port):
        self.client = HttpMethods.HttpClient(session=session)
        self.host = host
        self.port = port
    
    
    def getDisabledDeviceList(self, indexName):
        """
        Get list of disabled devices for a statistics index
        
        Parameters:
        indexName	 (string):	Index name
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/statistics/settings/disable/devicelist/{indexName}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def updateDeviceList(self, disableddevice, indexName):
        """
        Update list of disabled devices for a statistics index
        
        Parameters:
        disableddevice:	Disabled device
		indexName	 (string):	Index name
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/statistics/settings/disable/devicelist/{indexName}"
        response = self.client.apiCall(HttpMethods.PUT, endpoint, disableddevice)
        return response


    def getSettings(self):
        """
        Get statistics settings
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/statistics/settings/status"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def updateSettings(self, statssetting):
        """
        Update statistics settings
        
        Parameters:
        statssetting:	Stats setting
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/statistics/settings/status"
        response = self.client.apiCall(HttpMethods.PUT, endpoint, statssetting)
        return response


    def getEnabledIndex(self, deviceId):
        """
        Get list of enabled device for statistics index
        
        Parameters:
        deviceId	 (string):	Device IP
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/statistics/settings/status/device?deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


