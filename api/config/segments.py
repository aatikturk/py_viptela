from query_builder import Builder
import HttpMethods

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


    def createSegment(self, networksegment):
        """
        Create network segment
        
        Parameters:
        networksegment:	Network segment
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/segment"
        response = self.client.apiCall(HttpMethods.POST, endpoint, networksegment)
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


    def editSegment(self, networksegment, id):
        """
        Edit network segment
        
        Parameters:
        networksegment:	Network segment
		id	 (string):	Segment Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/segment/{id}"
        response = self.client.apiCall(HttpMethods.PUT, endpoint, networksegment)
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


