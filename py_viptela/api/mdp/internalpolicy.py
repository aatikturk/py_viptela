from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class Policy(object):
    """
    MDP - Internal Policy Management API
    
    Implements GET POST DEL PUT methods for Internal Policy Management endpoints

    """

    def __init__(self, session, host, port):
        self.host = host
        self.port = port
        self.client = HttpMethods.HttpClient(session=session)
    
    
    def add(self, policy):
        """
        Add internal policy from vmanage
        
        Parameters:
        policy:	    Internal Policy
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/mdp/policies/mdpconfig"
        response = self.client.apiCall(HttpMethods.PUT, endpoint, policy)
        return response


