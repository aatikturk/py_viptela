from query_builder import Builder
import HttpMethods

class Umbrella(object):
    """
    Umbrella API
    
    Implements GET POST DEL PUT methods for Umbrella endpoints

    """

    def __init__(self, session, host, port):
        self.host = host
        self.port = port
        self.client = HttpMethods.HttpClient(session=session)
    
    
    def getAllKeysFromUmbrella(self):
        """
        Get keys from Umbrella
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/umbrella/getkeys"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getManagementKeysFromUmbrella(self):
        """
        Get management keys from Umbrella
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/umbrella/getkeys/management"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getNetworkKeysFromUmbrella(self):
        """
        Get network devices keys from Umbrella
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/umbrella/getkeys/networkdevices"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getReportingKeysFromUmbrella(self):
        """
        Get reporting keys from Umbrella
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/umbrella/getkeys/reporting"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


