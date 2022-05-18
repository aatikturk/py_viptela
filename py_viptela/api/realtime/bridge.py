from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class Bridge(object):
    """
    Real-Time Monitoring - Bridge API
    
    Implements GET POST DEL PUT methods for Bridge endpoints

    """

    def __init__(self, session, host, port):
        self.host = host
        self.port = port
        self.client = HttpMethods.HttpClient(session=session)
    
    
    def getInterfaces(self, deviceId):
        """
        Get device bridge interface list (Real Time)
        
        Parameters:
        deviceId	 (string):	Device IP
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/bridge/interface?deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getInterfaceMac(self, bridgeId, ifName, macAddr, deviceId):
        """
        Get device bridge interface MAC (Real Time)
        
        Parameters:
        bridgeId	 (string):	Bridge ID
		ifName	 (string):	Interface name
		macAddr	 (string):	MAC address
		deviceId	 (string):	Device IP
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/bridge/mac?bridgeId={bridgeId}&ifName={ifName}&macAddr={macAddr}&deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getBridgeInterfaceTable(self, deviceId):
        """
        Get device bridge interface table (Real Time)
        
        Parameters:
        deviceId	 (string):	Device IP
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/bridge/table?deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


