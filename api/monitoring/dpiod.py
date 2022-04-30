from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class DpiOD(object):
    """
    Monitoring - DPI - On-demand troubleshooting API
    
    Implements GET POST DEL PUT methods for demandtroubleshooting endpoints

    """

    def __init__(self, session, host, port):
        self.client = HttpMethods.HttpClient(session=session)
        self.host = host
        self.port = port
    
    
    def getQueueEntries(self):
        """
        gets current on-demand queue entries
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/statistics/on-demand/queue"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def createQueueEntry(self, queue):
        """
        Create on-demand troubleshooting queue entry
        
        Parameters:
        queue:	On-demand queue entry
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/statistics/on-demand/queue"
        response = self.client.apiCall(HttpMethods.POST, endpoint, queue)
        return response


    def getQueueProperties(self):
        """
        gets current size of on-demand queue
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/statistics/on-demand/queue/properties"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def updateQueueEntry(self, queue, entryId):
        """
        Updates on-demand troubleshooting queue entry
        
        Parameters:
        queue:	On-demand queue entry
		entryId	 (string):	Entry Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/statistics/on-demand/queue/{entryId}"
        response = self.client.apiCall(HttpMethods.PUT, endpoint, queue)
        return response


    def deleteQueueEntry(self, entryId):
        """
        removes on-demand queue entry
        
        Parameters:
        entryId	 (string):	Entry Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/statistics/on-demand/queue/{entryId}"
        response = self.client.apiCall(HttpMethods.DELETE, endpoint)
        return response


