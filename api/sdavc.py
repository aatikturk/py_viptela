from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

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


    def disableCloudConnector(self, payload):
        """
        Disable SD_AVC Cloud Connector
        
        Parameters:
        payload:	Request Payload
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/sdavc/cloudconnector"
        response = self.client.apiCall(HttpMethods.PUT, endpoint, payload)
        return response


    def enableCloudConnector(self, payload):
        """
        Enable SD_AVC Cloud Connector
        
        Parameters:
        payload:	Request Payload
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/sdavc/cloudconnector"
        response = self.client.apiCall(HttpMethods.POST, endpoint, payload)
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


