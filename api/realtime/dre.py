from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class DRE(object):
    """
    Real-Time Monitoring - DRE API
    
    Implements GET POST DEL PUT methods for DRE endpoints

    """

    def __init__(self, session, host, port):
        self.host = host
        self.port = port
        self.client = HttpMethods.HttpClient(session=session)
    
    
    def getDreAutoBypassStats(self, ip, port, deviceId):
        """
        Get DRE auto-bypass statistics
        
        Parameters:
        ip	            (string):	Server IP
		port	        (number):	Port
		deviceId	    (string):	Device IP
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/dre/auto-bypass-stats?appqoe-dre-auto-bypass-server-ip={ip}&appqoe-dre-auto-bypass-port={port}&deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getDreStats(self, deviceId):
        """
        Get DRE statistics
        
        Parameters:
        deviceId	 (string):	Device IP
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/dre/dre-stats?deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getDreStatus(self, deviceId):
        """
        Get DRE status
        
        Parameters:
        deviceId	 (string):	Device IP
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/dre/dre-status?deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getDrePeerStats(self, ip, peerNo, deviceId):
        """
        Get DRE peer statistics
        
        Parameters:
        ip	 (string):	System IP
		peerNo	 (number):	Peer Number
		deviceId	 (string):	Device IP
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/dre/peer-stats?appqoe-dre-stats-peer-system-ip={ip}&appqoe-dre-stats-peer-peer-no={peerNo}&deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


