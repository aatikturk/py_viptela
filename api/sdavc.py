from query_builder import Builder
import HttpMethods

class Sdavc(object):
    """
    SD AVC Cloud Connector API
    
    Implements GET POST DEL PUT methods for SDAVCCloudConnector endpoints

    """

    def __init__(self, session, host, port):
        self.host = host
        self.port = port
        self.client = HttpMethods.HttpClient(session=session)
    
    
    def getCloudConnector(self):
        """
        Get SD_AVC Cloud Connector Config
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/sdavc/cloudconnector"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def disableCloudConnector(self, bodyParameter):
        """
        Disable SD_AVC Cloud Connector
        
        Parameters:
        bodyParameter:	Description
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/sdavc/cloudconnector"
        response = self.client.apiCall(HttpMethods.PUT, endpoint, bodyParameter)
        return response


    def enableCloudConnector(self, bodyParameter):
        """
        Enable SD_AVC Cloud Connector
        
        Parameters:
        bodyParameter:	Description
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/sdavc/cloudconnector"
        response = self.client.apiCall(HttpMethods.POST, endpoint, bodyParameter)
        return response


    def getCloudConnectorStatus(self):
        """
        Get SD_AVC Cloud Connector Status
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/sdavc/cloudconnector/status"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


