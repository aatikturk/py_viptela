from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class Offboard(object):
    """
    MDP - Offboarding API
    
    Implements GET POST DEL PUT methods for Offboarding endpoints

    """

    def __init__(self, session, host, port):
        self.host = host
        self.port = port
        self.client = HttpMethods.HttpClient(session=session)
    
    
    def disconnect(self, nmsId):
        """
        disconnect from mpd controller
        
        Parameters:
        Parameter Description
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/mdp/disconnect/{nmsId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def offboard(self, nmsId):
        """
        offboard the mdp application
        
        Parameters:
        Parameter Description
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/mdp/onboard/{nmsId}"
        response = self.client.apiCall(HttpMethods.DELETE, endpoint)
        return response


