from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class SFP(object):
    """
    Real-Time Monitoring - SFP API
    
    Implements GET POST DEL PUT methods for SFP endpoints

    """

    def __init__(self, session, host, port):
        self.client = HttpMethods.HttpClient(session=session)
        self.host = host
        self.port = port
    
    
    def getDetail(self, ifname, deviceId):
        """
        Get SFP detail
        
        Parameters:
        ifname	 (string):	IF Name
		deviceId	 (string):	Device Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/sfp/detail?ifname={ifname}&deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getDiag(self, ifname, deviceId):
        """
        Get SFP diagnostic
        
        Parameters:
        ifname	 (string):	IF Name
		deviceId	 (string):	Device Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/sfp/diagnostic?ifname={ifname}&deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getDiagAlarm(self, ifname, deviceId):
        """
        Get SFP diagnostic measurement alarm
        
        Parameters:
        ifname	 (string):	IF Name
		deviceId	 (string):	Device Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/sfp/diagnosticMeasurementAlarm?ifname={ifname}&deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getDiagValue(self, ifname, deviceId):
        """
        Get SFP diagnostic measurement value
        
        Parameters:
        ifname	 (string):	IF Name
		deviceId	 (string):	Device Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/sfp/diagnosticMeasurementValue?ifname={ifname}&deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


