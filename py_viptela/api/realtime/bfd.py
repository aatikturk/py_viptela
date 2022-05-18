from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class BFD(object):
    """
    Real-Time Monitoring - BFD API
    
    Implements GET POST DEL PUT methods for BFD endpoints

    """

    def __init__(self, session, host, port):
        self.host = host
        self.port = port
        self.client = HttpMethods.HttpClient(session=session)
    
    
    def getHistoryList(self, systemIp, color, deviceId):
        """
        Get BFD session history from device (Real Time)
        
        Parameters:
        systemIp	    (string):	System IP
		color	        (string):	Remote color
		deviceId	    (string):	Device IP
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/bfd/history?system-ip={systemIp}&color={color}&deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getLinkList(self, state):
        """
        Get list of BFD connections
        
        Parameters:
        state	 (string):	Device state
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/bfd/links?state={state}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getSessions(self, systemIp, color, localColor, deviceId):
        """
        Get list of BFD sessions from vManage (Real Time)
        
        Parameters:
        systemIp	    (string):	System IP
		color	        (string):	Remote color
		local-color	    (string):	Source color
		deviceId	    (string):	Device IP
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/bfd/sessions?system-ip={systemIp}&color={color}&local-color={localColor}&deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getSiteStateDetail(self):
        """
        Get detailed BFD site details
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/bfd/sites/detail"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getSitesSummary(self, isCached, vpnId):
        """
        Get BFD site summary
        
        Parameters:
        isCached	 (boolean):	Flag for caching
		vpnId	 (array):	Filter VPN
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/bfd/sites/summary?isCached={isCached}&vpnId={vpnId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getStateSummary(self, deviceId):
        """
        Get device BFD state summary
        
        Parameters:
        deviceId	 (string):	Device Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/bfd/state/device?deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getStateSummaryTloc(self, deviceId):
        """
        Get device BFD state summary with tloc color
        
        Parameters:
        deviceId	 (string):	Device Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/bfd/state/device/tloc?deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getStatus(self):
        """
        Get device BFD status
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/bfd/status"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getSummary(self, deviceId):
        """
        Get BFD summary from device (Real Time)
        
        Parameters:
        deviceId	 (string):	Device IP
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/bfd/summary?deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getStatusSummary(self, deviceId):
        """
        Get device BFD status summary
        
        Parameters:
        deviceId	 (string):	Device Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/bfd/summary/device?deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getSyncSession(self, systemIp, color, localColor, deviceId):
        """
        Get list of BFD sessions from vManage synchronously
        
        Parameters:
        systemIp	    (string):	System IP
		color	        (string):	Remote color
		localColor	    (string):	Source color
		deviceId	    (string):	Device Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/bfd/synced/sessions?system-ip={systemIp}&color={color}&local-color={localColor}&deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getTLOCSummary(self, deviceId):
        """
        Get TLOC summary from device (Real Time)
        
        Parameters:
        deviceId	 (string):	Device IP
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/bfd/tloc?deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


