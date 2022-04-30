from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class Server(object):
    """
    Monitoring - Server Info API
    
    Implements GET POST DEL PUT methods for ServerInfo endpoints

    """

    def __init__(self, session, host, port):
        self.client = HttpMethods.HttpClient(session=session)
        self.host = host
        self.port = port
    
    
    def createServerInfo(self):
        """
        Get Server info
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/server/info"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


