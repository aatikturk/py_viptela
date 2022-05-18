from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class DPI(object):
    """
    Monitoring - DPI API
    
    Implements GET POST DEL PUT methods for DPI endpoints

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
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/statistics/dpi?query={query}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getStatsRawData(self, statsquerystring):
        """
        Get stats raw data
        
        Parameters:
        statsquerystring:	Stats query string
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/statistics/dpi"
        response = self.client.apiCall(HttpMethods.POST, endpoint, statsquerystring)
        return response


    def getPostAggregationAppData(self, queryfilter):
        """
        Get raw aggregated data and display applications with the highest utilization for a device
        
        Parameters:
        queryfilter:	Query filter
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/statistics/dpi/agg-app/aggregation"
        response = self.client.apiCall(HttpMethods.POST, endpoint, queryfilter)
        return response


    def getAggregationDataByQuery(self, query):
        """
        Get aggregated data based on input query and filters. The data can be filtered on time and other unique parameters based upon necessity and intended usage
        
        Parameters:
        query	 (string):	Query filter
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/statistics/dpi/aggregation?query={query}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getPostAggregationData(self, queryfilter):
        """
        Get raw aggregated data and display applications with the highest utilization for a device
        
        Parameters:
        queryfilter:	Query filter
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/statistics/dpi/aggregation"
        response = self.client.apiCall(HttpMethods.POST, endpoint, queryfilter)
        return response


    def createDPIFlowsGridListQuery(self, query, limit):
        """
        Get detailed DPI application flows list in a grid table
        
        Parameters:
        query	 (string):	Query string
		limit	 (string):	Query size
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/statistics/dpi/applications?query={query}&limit={limit}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def createDPISummary(self, query, limit):
        """
        Get detailed DPI application flows summary
        
        Parameters:
        query	 (string):	Query string
		limit	 (string):	Query size
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/statistics/dpi/applications/summary?query={query}&limit={limit}"
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
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/statistics/dpi/csv?query={query}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getUniqueFlowCount(self, deviceId, interval, application, window, family):
        """
        Get application flow count per tunnel
        
        Parameters:
        deviceId	 (string):	Device Id
		interval	 (string):	Interval
		application	 (string):	Application
		window	 (string):	Window
		family	 (string):	Family
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/statistics/dpi/device/application/flowcount?deviceId={deviceId}&interval={interval}&application={application}&window={window}&family={family}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def createDPIDeviceGridData(self, query, limit):
        """
        Get detailed DPI flows list
        
        Parameters:
        query	 (string):	Query string
		limit	 (string):	Query size
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/statistics/dpi/device/applications?query={query}&limit={limit}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def createDPIDeviceAndAppDetails(self, query):
        """
        Get detailed DPI device and app list
        
        Parameters:
        query	 (string):	Query string
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/statistics/dpi/device/details/applications?query={query}"
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
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/statistics/dpi/doccount?query={query}"
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
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/statistics/dpi/doccount"
        response = self.client.apiCall(HttpMethods.POST, endpoint, query)
        return response


    def getStatDataFields(self):
        """
        Get fields and type
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/statistics/dpi/fields"
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
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/statistics/dpi/page?query={query}&scrollId={scrollId}&count={count}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
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
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/statistics/dpi/page?scrollId={scrollId}&count={count}"
        response = self.client.apiCall(HttpMethods.POST, endpoint, statsquerystring)
        return response


    def getAggregationDataForPacketDup(self, querystring):
        """
        Get time series aggregation data for packet duplication for an application over TLOCs if available
        
        Parameters:
        querystring:	Query string
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/statistics/dpi/pktdup/aggregation"
        response = self.client.apiCall(HttpMethods.POST, endpoint, querystring)
        return response


    def getStatQueryFields(self):
        """
        Get query fields
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/statistics/dpi/query/fields"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getAggregationDataDPI(self, querystring):
        """
        Get aggregation data and fec recovery rate if available
        
        Parameters:
        querystring:	Query string
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/statistics/dpi/recovery/aggregation"
        response = self.client.apiCall(HttpMethods.POST, endpoint, querystring)
        return response


