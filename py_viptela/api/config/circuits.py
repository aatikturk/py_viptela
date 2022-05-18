from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class Circuits(object):
    """
    Configuration - Circuits API
    
    Implements GET POST DEL PUT methods for Circuits endpoints

    """

    def __init__(self, session, host, port):
        self.client = HttpMethods.HttpClient(session=session)
        self.host = host
        self.port = port
    
    
    def get(self):
        """
        Get network circuits
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/networkdesign/circuit"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def create(self, networkcircuit):
        """
        Create network circuits
        
        Parameters:
        networkcircuit:	Network circuit
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/networkdesign/circuit"
        response = self.client.apiCall(HttpMethods.POST, endpoint, networkcircuit)
        return response


    def edit(self, networkcircuit, id):
        """
        Edit network circuits
        
        Parameters:
        networkcircuit:	Network circuit
		id	 (string):	Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/networkdesign/circuit/{id}"
        response = self.client.apiCall(HttpMethods.PUT, endpoint, networkcircuit)
        return response


    def delete(self, id):
        """
        Delete network circuits
        
        Parameters:
        id	 (string):	Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/networkdesign/circuit/{id}"
        response = self.client.apiCall(HttpMethods.DELETE, endpoint)
        return response


