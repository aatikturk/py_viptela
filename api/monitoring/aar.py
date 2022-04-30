from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class Aar(object):
    """
    Monitoring - Application Aware Routing API
    
    Implements GET POST DEL PUT methods for ApplicationAwareRouting endpoints

    """

    def __init__(self, session, host, port):
        self.client = HttpMethods.HttpClient(session=session)
        self.host = host
        self.port = port
    
    
    def getStatDataRawData(self, query):
        """
        Get stats raw data
        
        Parameters:
        query	 (string):	Query string
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/statistics/approute?query={query}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getStatsRawData(self, query):
        """
        Get stats raw data
        
        Parameters:
        query:	Stats query string
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/statistics/approute"
        response = self.client.apiCall(HttpMethods.POST, endpoint, query)
        return response


    def getAggregationDataByQuery(self, query):
        """
        Get aggregated data based on input query and filters. The data can be filtered on time and other unique parameters based upon necessity and intended usage
        
        Parameters:
        query	 (string):	Query filter
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/statistics/approute/aggregation?query={query}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getPostAggregationDataByQuery(self, query):
        """
        Get aggregated data based on input query and filters. The data can be filtered on time and other unique parameters based upon necessity and intended usage
        
        Parameters:
        query:	Stats query string
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/statistics/approute/aggregation"
        response = self.client.apiCall(HttpMethods.POST, endpoint, query)
        return response


    def getPostAggregationAppDataByQuery(self, query):
        """
        Get aggregated data based on input query and filters. The data can be filtered on time and other unique parameters based upon necessity and intended usage
        
        Parameters:
        query:	Stats query string
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/statistics/approute/app-agg/aggregation"
        response = self.client.apiCall(HttpMethods.POST, endpoint, query)
        return response


    def getStatDataRawDataAsCSV(self, query):
        """
        Get raw data with optional query as CSV
        
        Parameters:
        query	 (string):	Query string
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/statistics/approute/csv?query={query}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getApprouteGridStat(self, query):
        """
        Get statistics for top applications per tunnel in a grid table
        
        Parameters:
        query	 (string):	Query filter
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/statistics/approute/device/tunnel/summary?query={query}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getTunnel(self, query):
        """
        Get statistics for top applications per tunnel in a grid table
        
        Parameters:
        query	 (string):	Query filter
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/statistics/approute/device/tunnels?query={query}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getCount(self, query):
        """
        Get response count of a query
        
        Parameters:
        query	 (string):	Query
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/statistics/approute/doccount?query={query}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getCountPost(self, query):
        """
        Get response count of a query
        
        Parameters:
        query:	Query
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/statistics/approute/doccount"
        response = self.client.apiCall(HttpMethods.POST, endpoint, query)
        return response


    def getAggregationDataAppRoute(self, queryfilter):
        """
        Get aggregation data and fec recovery rate
        
        Parameters:
        queryfilter:	Query filter
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/statistics/approute/fec/aggregation"
        response = self.client.apiCall(HttpMethods.POST, endpoint, queryfilter)
        return response


    def getStatDataFields(self):
        """
        Get fields and type
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/statistics/approute/fields"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getStatBulkRawData(self, query, scrollId, count):
        """
        Get stats raw data
        
        Parameters:
        query	 (string):	Query string
		scrollId	 (string):	ES scroll Id
		count	 (string):	Result size
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/statistics/approute/page?query={query}&scrollId={scrollId}&count={count}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getPostStatBulkRawData(self, query, scrollId, count):
        """
        Get stats raw data
        
        Parameters:
        query:	Stats query string
		scrollId	 (string):	ES scroll Id
		count	 (string):	Result size
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/statistics/approute/page?scrollId={scrollId}&count={count}"
        response = self.client.apiCall(HttpMethods.POST, endpoint, query)
        return response


    def getStatQueryFields(self):
        """
        Get query fields
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/statistics/approute/query/fields"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getTunnelChart(self, type, query):
        """
        Get tunnel top statistics in as chart
        
        Parameters:
        type	 (string):	Type
		query	 (string):	Query filter
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/statistics/approute/tunnel/{type}/summary?query={query}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getTunnelsSummary(self, type, query, limit):
        """
        Get tunnel top statistics from device
        
        Parameters:
        type	 (string):	Type
		query	 (string):	Query filter
		limit	 (integer):	Query result size
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/statistics/approute/tunnels/summary/{type}?query={query}&limit={limit}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getTunnels(self, type, query, limit):
        """
        Get tunnel top statistics from device
        
        Parameters:
        type	 (string):	Type
		query	 (string):	Query filter
		limit	 (integer):	Query result size
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/statistics/approute/tunnels/{type}?query={query}&limit={limit}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


