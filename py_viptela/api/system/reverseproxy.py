from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class ReverseProxy(object):
    """
    System - Reverse Proxy API
    
    Implements GET POST DEL PUT methods for Reverse Proxy endpoints

    """

    def __init__(self, session, host, port):
        self.host = host
        self.port = port
        self.client = HttpMethods.HttpClient(session=session)
    
    
    def get(self, uuid):
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


    def create(self, mapping, uuid):
        """
        Create reverse proxy IP/Port mappings for controller
        
        Parameters:
        mapping:	Device reverse proxy mappings
		uuid	 (string):	Device uuid
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/system/reverseproxy/{uuid}"
        response = self.client.apiCall(HttpMethods.POST, endpoint, mapping)
        return response


