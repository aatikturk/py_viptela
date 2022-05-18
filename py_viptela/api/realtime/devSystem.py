from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class Stat(object):
    """
    Real-Time Monitoring - Device System Stats API
    
    Implements GET POST DEL PUT methods for DeviceSystemStats endpoints

    """

    def __init__(self, session, host, port):
        self.host = host
        self.port = port
        self.client = HttpMethods.HttpClient(session=session)
    
    
    def getStatDataRawData(self, query):
        """
        Get stats raw data
        
        Parameters:
        query	 (string):	Query string
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/statistics/system?query={query}"
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
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/statistics/system"
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
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/statistics/system/aggregation?query={query}"
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
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/statistics/system/aggregation"
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
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/statistics/system/app-agg/aggregation"
        response = self.client.apiCall(HttpMethods.POST, endpoint, query)
        return response


    def createDeviceSystemCPUStat(self, query, deviceId):
        """
        Get device system CPU stats list
        
        Parameters:
        query	 (string):	Query filter
		deviceId	 (string):	Device IP
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/statistics/system/cpu?query={query}&deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getStatDataRawDataAsCSV(self, query):
        """
        Get raw data with optional query as CSV
        
        Parameters:
        query	 (string):	Query string
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/statistics/system/csv?query={query}"
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
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/statistics/system/doccount?query={query}"
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
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/statistics/system/doccount"
        response = self.client.apiCall(HttpMethods.POST, endpoint, query)
        return response


    def getStatDataFields(self):
        """
        Get fields and type
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/statistics/system/fields"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def createDeviceSystemMemoryStat(self, query, deviceId):
        """
        Get device system memory stats list
        
        Parameters:
        query	 (string):	Query filter
		deviceId	 (string):	Device IP
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/statistics/system/memory?query={query}&deviceId={deviceId}"
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
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/statistics/system/page?query={query}&scrollId={scrollId}&count={count}"
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
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/statistics/system/page?scrollId={scrollId}&count={count}"
        response = self.client.apiCall(HttpMethods.POST, endpoint, query)
        return response


    def getStatQueryFields(self):
        """
        Get query fields
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/statistics/system/query/fields"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


