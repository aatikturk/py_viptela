from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class ServiceChainStatistics(object):
    """
    Monitoring - Service Chain Statistics API
    
    Implements GET POST DEL PUT methods for ServiceChainStatistics endpoints

    """

    def __init__(self, session, host, port):
        self.client  = HttpMethods.HttpClient(session=session)
        self.host    = host
        self.port    = port
        self.builder = Builder()
    
    def getStatDataRawData(self, query):
        """
        Get stats raw data
        
        Parameters:
        query	 (string):	Query string
        
        Returns
        response    (dict)
        
        
        """
        query_string = self.builder.generateQuery(query)
        endpoint     = f"https://{self.host}:{self.port}/dataservice/statistics/vnfstatistics?query={query_string}"
        response     = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getStatsRawData(self, statsquerystring):
        """
        Get stats raw data
        
        Parameters:
        statsquerystring:	Stats query string
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/statistics/vnfstatistics"
        response = self.client.apiCall(HttpMethods.POST, endpoint, statsquerystring)
        return response


    def getAggregationDataByQuery(self, query):
        """
        Get aggregated data based on input query and filters. The data can be filtered on time and other unique parameters based upon necessity and intended usage
        
        Parameters:
        query	 (string):	Query filter
        
        Returns
        response    (dict)
        
        
        """
        query_string = self.builder.generateQuery(query)
        endpoint     = f"https://{self.host}:{self.port}/dataservice/statistics/vnfstatistics/aggregation?query={query_string}"
        response     = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getPostAggregationDataByQuery(self, statsquerystring):
        """
        Get aggregated data based on input query and filters. The data can be filtered on time and other unique parameters based upon necessity and intended usage
        
        Parameters:
        statsquerystring:	Stats query string
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/statistics/vnfstatistics/aggregation"
        response = self.client.apiCall(HttpMethods.POST, endpoint, statsquerystring)
        return response


    def getPostAggregationAppDataByQuery(self, statsquerystring):
        """
        Get aggregated data based on input query and filters. The data can be filtered on time and other unique parameters based upon necessity and intended usage
        
        Parameters:
        statsquerystring:	Stats query string
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/statistics/vnfstatistics/app-agg/aggregation"
        response = self.client.apiCall(HttpMethods.POST, endpoint, statsquerystring)
        return response


    def getStatDataRawDataAsCSV(self, query):
        """
        Get raw data with optional query as CSV
        
        Parameters:
        query	 (string):	Query string
        
        Returns
        response    (dict)
        
        
        """
        query_string = self.builder.generateQuery(query)
        endpoint     = f"https://{self.host}:{self.port}/dataservice/statistics/vnfstatistics/csv?query={query_string}"
        response     = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getCount(self, query):
        """
        Get response count of a query
        
        Parameters:
        query	 (string):	Query
        
        Returns
        response    (dict)
        
        
        """
        query_string = self.builder.generateQuery(query)
        endpoint     = f"https://{self.host}:{self.port}/dataservice/statistics/vnfstatistics/doccount?query={query_string}"
        response     = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getCountPost(self, query):
        """
        Get response count of a query
        
        Parameters:
        query:	Query
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/statistics/vnfstatistics/doccount"
        response = self.client.apiCall(HttpMethods.POST, endpoint, query)
        return response


    def getStatDataFields(self):
        """
        Get fields and type
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/statistics/vnfstatistics/fields"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getStatBulkRawData(self, query, scrollId, count):
        """
        Get stats raw data
        
        Parameters:
        query	     (string):	Query string
		scrollId	 (string):	ES scroll Id
		count	     (string):	Result size
        
        Returns
        response    (dict)
        
        
        """
        query_string = self.builder.generateQuery(query)
        endpoint     = f"https://{self.host}:{self.port}/dataservice/statistics/vnfstatistics/page?query={query_string}&scrollId={scrollId}&count={count}"
        response     = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getPostStatBulkRawData(self, statsquerystring, scrollId, count):
        """
        Get stats raw data
        
        Parameters:
        statsquerystring:	Stats query string
		scrollId	 (string):	ES scroll Id
		count	 (string):	Result size
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/statistics/vnfstatistics/page?scrollId={scrollId}&count={count}"
        response = self.client.apiCall(HttpMethods.POST, endpoint, statsquerystring)
        return response


    def getStatQueryFields(self):
        """
        Get query fields
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/statistics/vnfstatistics/query/fields"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


