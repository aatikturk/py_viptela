from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class List(object):
    """
    Configuration - Policy List Builder API
    
    Implements GET POST DEL PUT methods for PolicyListBuilder endpoints

    """

    def __init__(self, session, host, port):
        self.host = host
        self.port = port
        self.client = HttpMethods.HttpClient(session=session)
    
    
    def getAll(self):
        """
        Get all policy lists
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/policy/list"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


