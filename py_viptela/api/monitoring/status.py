from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class Status(object):
    """
    Monitoring - Status API
    
    Implements GET POST DEL PUT methods for Status endpoints

    """

    def __init__(vmanage, session, host, port):
        vmanage.client = HttpMethods.HttpClient(session=session)
        vmanage.host = host
        vmanage.port = port
    
    
    def getDisabledDeviceList(vmanage, indexName):
        """
        Get list of disabled devices for a statistics index
        
        Parameters:
        indexName	 (string):	Index name
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/statistics/settings/disable/devicelist/{indexName}"
        response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def updateDeviceList(vmanage, disableddevice, indexName):
        """
        Update list of disabled devices for a statistics index
        
        Parameters:
        disableddevice:	Disabled device
		indexName	 (string):	Index name
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/statistics/settings/disable/devicelist/{indexName}"
        response = vmanage.client.apiCall(HttpMethods.PUT, endpoint, disableddevice)
        return response


    def getSettings(vmanage):
        """
        Get statistics settings
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/statistics/settings/status"
        response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def updateSettings(vmanage, statssetting):
        """
        Update statistics settings
        
        Parameters:
        statssetting:	Stats setting
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/statistics/settings/status"
        response = vmanage.client.apiCall(HttpMethods.PUT, endpoint, statssetting)
        return response


    def getEnabledIndex(vmanage, deviceId):
        """
        Get list of enabled device for statistics index
        
        Parameters:
        deviceId	 (string):	Device IP
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/statistics/settings/status/device?deviceId={deviceId}"
        response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
        return response


