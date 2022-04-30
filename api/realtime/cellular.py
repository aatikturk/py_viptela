from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class Cellular(object):
    """
    Real-Time Monitoring - Cellular API
    
    Implements GET POST DEL PUT methods for Cellular endpoints

    """

    def __init__(self, session, host, port):
        self.host = host
        self.port = port
        self.client = HttpMethods.HttpClient(session=session)
    
    
    def getConnections(self, deviceId):
        """
        Get cellular connection list from device
        
        Parameters:
        deviceId	 (string):	Device IP
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/cellular/connection?deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getHardwareList(self, deviceId):
        """
        Get cellular hardware list from device
        
        Parameters:
        deviceId	 (string):	Device IP
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/cellular/hardware?deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getModemList(self, policyId):
        """
        Get cellular modem list from device
        
        Parameters:
        policyId	 (string):	Policy IP
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/cellular/modem?policyId={policyId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getNetworkList(self, deviceId):
        """
        Get cellular network list from device
        
        Parameters:
        deviceId	 (string):	Device IP
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/cellular/network?deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getProfileList(self, deviceId):
        """
        Get cellular profile list from device
        
        Parameters:
        deviceId	 (string):	Device IP
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/cellular/profiles?deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getRadioList(self, deviceId):
        """
        Get cellular radio list from device
        
        Parameters:
        deviceId	 (string):	Device IP
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/cellular/radio?deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getSessionsList(self, ifName, priDns, deviceId):
        """
        Get cellular session list from device
        
        Parameters:
        ifName	 (string):	Interface name
		priDns	 (string):	DNS primary IP
		deviceId	 (string):	Device IP
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/cellular/sessions?ifName={ifName}&priDns={priDns}&deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getCellularStatusList(self, deviceId):
        """
        Get cellular status list from device
        
        Parameters:
        deviceId	 (string):	Device IP
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/cellular/status?deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


