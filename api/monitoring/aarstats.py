from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class AarStats(object):
    """
    Monitoring - Application-Aware Routing Statistics API
    
    Implements GET POST DEL PUT methods for AwareRoutingStatistics endpoints

    """

    def __init__(self, session, host, port):
        self.client = HttpMethods.HttpClient(session=session)
        self.host = host
        self.port = port
    
    
    def getHealthSummary(self, type, limit, query):
        """
        Get application-aware routing statistics summary from device
        
        Parameters:
        type	 (string):	Type
		limit	 (integer):	Query result size
		query	 (string):	Query filter
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/statistics/approute/transport/summary/{type}?limit={limit}&query={query}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getHealth(self, type, query, limit):
        """
        Get application-aware routing statistics from device
        
        Parameters:
        type	 (string):	Type
		query    (string):  Query filter
		limit	 (string):	Query result size
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/statistics/approute/transport/{type}?query={query}&limit={limit}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


