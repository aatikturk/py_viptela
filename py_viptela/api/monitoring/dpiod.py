from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class DpiOD(object):
    """
    Monitoring - DPI - On-demand troubleshooting API
    
    Implements GET POST DEL PUT methods for demandtroubleshooting endpoints

    """

    def __init__(vmanage, session, host, port):
        vmanage.client = HttpMethods.HttpClient(session=session)
        vmanage.host = host
        vmanage.port = port
    
    
    def getQueueEntries(vmanage):
        """
        gets current on-demand queue entries
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/statistics/on-demand/queue"
        response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def createQueueEntry(vmanage, queue):
        """
        Create on-demand troubleshooting queue entry
        
        Parameters:
        queue:	On-demand queue entry
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/statistics/on-demand/queue"
        response = vmanage.client.apiCall(HttpMethods.POST, endpoint, queue)
        return response


    def getQueueProperties(vmanage):
        """
        gets current size of on-demand queue
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/statistics/on-demand/queue/properties"
        response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def updateQueueEntry(vmanage, queue, entryId):
        """
        Updates on-demand troubleshooting queue entry
        
        Parameters:
        queue:	On-demand queue entry
		entryId	 (string):	Entry Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/statistics/on-demand/queue/{entryId}"
        response = vmanage.client.apiCall(HttpMethods.PUT, endpoint, queue)
        return response


    def deleteQueueEntry(vmanage, entryId):
        """
        removes on-demand queue entry
        
        Parameters:
        entryId	 (string):	Entry Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/statistics/on-demand/queue/{entryId}"
        response = vmanage.client.apiCall(HttpMethods.DELETE, endpoint)
        return response


