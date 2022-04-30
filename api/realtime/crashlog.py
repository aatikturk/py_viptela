from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class CrashLog(object):
    """
    Real-Time Monitoring - Crash Log API
    
    Implements GET POST DEL PUT methods for CrashLog endpoints

    """

    def __init__(self, session, host, port):
        self.host = host
        self.port = port
        self.client = HttpMethods.HttpClient(session=session)
    
    
    def getLogs(self, deviceId):
        """
        Get device crash logs from device
        
        Parameters:
        deviceId	 (string):	Device IP
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/crashlog?deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getAllLogs(self):
        """
        Get device crash logs for all device
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/crashlog/details"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getInfo(self, deviceId, filename):
        """
        Get device crash info from device
        
        Parameters:
        deviceId	 (string):	Device IP
		filename	 (string):	Crash file name
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/crashlog/log?deviceId={deviceId}&filename={filename}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getLogsSynced(self, deviceId):
        """
        Get device crash logs synchronously from device
        
        Parameters:
        deviceId	 (string):	Device IP
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/crashlog/synced?deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


