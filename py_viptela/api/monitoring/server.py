from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class Server(object):
    """
    Monitoring - Server Info API
    
    Implements GET POST DEL PUT methods for ServerInfo endpoints

    """

    def __init__(vmanage, session, host, port):
        vmanage.client = HttpMethods.HttpClient(session=session)
        vmanage.host = host
        vmanage.port = port
    
    
    def createServerInfo(vmanage):
        """
        Get Server info
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/server/info"
        response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
        return response


