from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class Neighbor(object):
    """
    Real-Time Monitoring - IPv6 Neighbours API
    
    Implements GET POST DEL PUT methods for IPv6Neighbours endpoints

    """

    def __init__(self, session, host, port):
        self.host = host
        self.port = port
        self.client = HttpMethods.HttpClient(session=session)
    
    
    def getInterface(self, vpnId, ifname, mac, deviceId):
        """
        Get IPv6 Neighbors from device (Real Time)
        
        Parameters:
        vpnId	        (string):	VPN Id
		ifname	        (string):	Interface name
		mac	            (string):	Mac address
		deviceId	    (string):	Device IP
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/ndv6?vpn-id={vpnId}&if-name={ifname}&mac={mac}&deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


