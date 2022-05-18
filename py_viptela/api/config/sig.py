from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class SIG(object):
    """
    Configuration - Secure Internet Gateway Tunnels API
    
    Implements GET POST DEL PUT methods for SecureInternetGatewayTunnels endpoints

    """

    def __init__(self, session, host, port):
        self.client = HttpMethods.HttpClient(session=session)
        self.host = host
        self.port = port
    
    
    def getSigTunnelList(self, deviceId):
        """
        Get Secure Internet Gateway Tunnel List
        
        Parameters:
        deviceId	 (string):	Device Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/cloudx/sig_tunnels?deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


