from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class AwareRoute(object):
    """
    Real-Time Monitoring - Application-Aware Route API
    
    Implements GET POST DEL PUT methods for AwareRoute endpoints

    """

    def __init__(self, session, host, port):
        self.host = host
        self.port = port
        self.client = HttpMethods.HttpClient(session=session)
    
    
    def getSlaList(self, deviceId):
        """
        Get SLA class list from device (Real Time)
        
        Parameters:
        deviceId	 (string):	Device IP
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/app-route/sla-class?deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getStatList(self, remote_system_ip, local_color, remote_color, deviceId):
        """
        Get application-aware routing statistics from device (Real Time)
        
        Parameters:
        remote-system-ip	 (string):	Remote system IP
		local-color	 (string):	Local color
		remote-color	 (string):	Remote color
		deviceId	 (string):	Device IP
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/app-route/statistics?remote-system-ip={remote_system_ip}&local-color={local_color}&remote-color={remote_color}&deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


