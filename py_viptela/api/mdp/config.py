from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class Config(object):
    """
    MDP - Config Object API
    
    Implements GET POST DEL PUT methods for Config Object endpoints

    """

    def __init__(self, session, host, port):
        self.host = host
        self.port = port
        self.client = HttpMethods.HttpClient(session=session)
    
    
    def getConfig(self, deviceId):
        """
        Retrieve MDP ConfigObject
        
        Parameters:
        Parameter Description
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/mdp/policies/mdpconfig/{deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


