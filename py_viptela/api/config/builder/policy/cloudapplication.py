from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class CloudApp(object):
    """
    Configuration - Policy Cloud Application Builder API
    
    Implements GET POST DEL PUT methods for PolicyCloudApplicationBuilder endpoints

    """

    def __init__(self, session, host, port):
        self.host = host
        self.port = port
        self.client = HttpMethods.HttpClient(session=session)
    
    
    def getCloudDiscoveredApps(self):
        """
        Get all cloud discovered applications
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/policy/clouddiscoveredapp"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


