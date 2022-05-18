from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class Segments(object):
    """
    Configuration - Segments API
    
    Implements GET POST DEL PUT methods for Segments endpoints

    """

    def __init__(self, session, host, port):
        self.client = HttpMethods.HttpClient(session=session)
        self.host = host
        self.port = port
    
    
    def getSegments(self):
        """
        Get network segments
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/segment"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def createSegment(self, segmen):
        """
        Create network segment
        
        Parameters:
        segmen:	Network segment
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/segment"
        response = self.client.apiCall(HttpMethods.POST, endpoint, segmen)
        return response


    def getSegment(self, id):
        """
        Get network segment
        
        Parameters:
        id	 (string):	Segment Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/segment/{id}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def editSegment(self, segmen, id):
        """
        Edit network segment
        
        Parameters:
        segmen:	Network segment
		id	 (string):	Segment Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/segment/{id}"
        response = self.client.apiCall(HttpMethods.PUT, endpoint, segmen)
        return response


    def deleteSegment(self, id):
        """
        Delete network segment
        
        Parameters:
        id	 (string):	Segment Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/segment/{id}"
        response = self.client.apiCall(HttpMethods.DELETE, endpoint)
        return response


