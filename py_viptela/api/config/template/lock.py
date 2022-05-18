from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class Lock(object):
    """
    Configuration - Template Lock API
    
    Implements GET POST DEL PUT methods for TemplateLock endpoints

    """

    def __init__(self, session, host, port):
        self.host = host
        self.port = port
        self.client = HttpMethods.HttpClient(session=session)
    
    
    def updateLeaseTime(self, processId):
        """
        Update lease
        
        Parameters:
        processId	 (string):	Process Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/lock/{processId}"
        response = self.client.apiCall(HttpMethods.PUT, endpoint)
        return response


    def removeLock(self, processId):
        """
        Remove lock
        
        Parameters:
        processId	 (string):	Process Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/lock/{processId}"
        response = self.client.apiCall(HttpMethods.DELETE, endpoint)
        return response


