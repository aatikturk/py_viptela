from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class Umbrella(object):
    """
    Umbrella API
    
    Implements GET POST DEL PUT methods for Umbrella endpoints

    """

    def __init__(self, session, host, port):
        self.host = host
        self.port = port
        self.client = HttpMethods.HttpClient(session=session)
    
    
    def getAllKeys(self):
        """
        Get keys from Umbrella
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/umbrella/getkeys"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getManagementKeys(self):
        """
        Get management keys from Umbrella
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/umbrella/getkeys/management"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getNetworkKeys(self):
        """
        Get network devices keys from Umbrella
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/umbrella/getkeys/networkdevices"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getReportingKeys(self):
        """
        Get reporting keys from Umbrella
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/umbrella/getkeys/reporting"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


