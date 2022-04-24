from query_builder import Builder
import HttpMethods

class ReverseProxy(object):
    """
    System - Reverse Proxy API
    
    Implements GET POST DEL PUT methods for ReverseProxy endpoints

    """

    def __init__(self, session, host, port):
        self.host = host
        self.port = port
        self.client = HttpMethods.HttpClient(session=session)
    
    
    def getReverseProxyMappings(self, uuid):
        """
        Get reverse proxy IP/Port mappings for controller
        
        Parameters:
        uuid	 (string):	Device uuid
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/system/reverseproxy/{uuid}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def createReverseProxyMappings(self, devicereverseproxymappings, uuid):
        """
        Create reverse proxy IP/Port mappings for controller
        
        Parameters:
        devicereverseproxymappings:	Device reverse proxy mappings
		uuid	 (string):	Device uuid
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/system/reverseproxy/{uuid}"
        response = self.client.apiCall(HttpMethods.POST, endpoint, devicereverseproxymappings)
        return response


