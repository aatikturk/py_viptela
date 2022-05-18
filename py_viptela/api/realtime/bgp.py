from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class BGP(object):
    """
    Real-Time Monitoring - BGP API
    
    Implements GET POST DEL PUT methods for BGP endpoints

    """

    def __init__(self, session, host, port):
        self.host = host
        self.port = port
        self.client = HttpMethods.HttpClient(session=session)
    
    
    def getNeighbors(self, vpnId, peerAddr, asNo, deviceId):
        """
        Get BGP neighbors list (Real Time)
        
        Parameters:
        vpnId	 (string):	VPN Id
		peerAddr	 (string):	Peer address
		asNo	 (string):	AS number
		deviceId	 (string):	Device Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/bgp/neighbors?vpnId={vpnId}&peerAddr={peerAddr}&as={asNo}&deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def createBGPRoutesList(self, vpnId, prefix, nexthop, deviceId):
        """
        Get BGP routes list (Real Time)
        
        Parameters:
        vpnId	 (string):	VPN Id
		prefix	 (string):	IP prefix
		nexthop	 (string):	Next hop
		deviceId	 (string):	Device Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/bgp/routes?vpnId={vpnId}&prefix={prefix}&nexthop={nexthop}&deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def createBGPSummary(self, deviceId):
        """
        Get BGP summary (Real Time)
        
        Parameters:
        deviceId	 (string):	Device Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/bgp/summary?deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


