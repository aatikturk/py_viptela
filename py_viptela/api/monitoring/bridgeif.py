from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

def getStatDataRawData(vmanage, query):
    """
    Get stats raw data
    
    Parameters:
    query	 (string):	Query string
    
    Returns
    response    (dict)
    
    
    """
    query_string = vmanage.builder.generateQuery(query)
    endpoint     = f"https://{vmanage.host}:{vmanage.port}/dataservice/statistics/bridgeinterface?query={query_string}"
    response     = vmanage.client.apiCall(HttpMethods.GET, endpoint)
    return response
def getStatsRawData(vmanage, statsquerystring):
    """
    Get stats raw data
    
    Parameters:
    statsquerystring:	Stats query string
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/statistics/bridgeinterface"
    response = vmanage.client.apiCall(HttpMethods.POST, endpoint, statsquerystring)
    return response
def getAggregationDataByQuery(vmanage, query):
    """
    Get aggregated data based on input query and filters. The data can be filtered on time and other unique parameters based upon necessity and intended usage
    
    Parameters:
    query	 (string):	Query filter
    
    Returns
    response    (dict)
    
    
    """
    query_string = vmanage.builder.generateQuery(query)
    endpoint     = f"https://{vmanage.host}:{vmanage.port}/dataservice/statistics/bridgeinterface/aggregation?query={query_string}"
    response     = vmanage.client.apiCall(HttpMethods.GET, endpoint)
    return response
def getPostAggregationDataByQuery(vmanage, statsquerystring):
    """
    Get aggregated data based on input query and filters. The data can be filtered on time and other unique parameters based upon necessity and intended usage
    
    Parameters:
    statsquerystring:	Stats query string
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/statistics/bridgeinterface/aggregation"
    response = vmanage.client.apiCall(HttpMethods.POST, endpoint, statsquerystring)
    return response
def getPostAggregationAppDataByQuery(vmanage, statsquerystring):
    """
    Get aggregated data based on input query and filters. The data can be filtered on time and other unique parameters based upon necessity and intended usage
    
    Parameters:
    statsquerystring:	Stats query string
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/statistics/bridgeinterface/app-agg/aggregation"
    response = vmanage.client.apiCall(HttpMethods.POST, endpoint, statsquerystring)
    return response
def getStatDataRawDataAsCSV(vmanage, query):
    """
    Get raw data with optional query as CSV
    
    Parameters:
    query	 (string):	Query string
    
    Returns
    response    (dict)
    
    
    """
    query_string = vmanage.builder.generateQuery(query)
    endpoint     = f"https://{vmanage.host}:{vmanage.port}/dataservice/statistics/bridgeinterface/csv?query={query_string}"
    response     = vmanage.client.apiCall(HttpMethods.GET, endpoint)
    return response
def getCount(vmanage, query):
    """
    Get response count of a query
    
    Parameters:
    query	 (string):	Query
    
    Returns
    response    (dict)
    
    
    """
    query_string = vmanage.builder.generateQuery(query)
    endpoint     = f"https://{vmanage.host}:{vmanage.port}/dataservice/statistics/bridgeinterface/doccount?query={query_string}"
    response     = vmanage.client.apiCall(HttpMethods.GET, endpoint)
    return response
def getCountPost(vmanage, query):
    """
    Get response count of a query
    
    Parameters:
    query:	Query
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/statistics/bridgeinterface/doccount"
    response = vmanage.client.apiCall(HttpMethods.POST, endpoint, query)
    return response
def getStatDataFields(vmanage):
    """
    Get fields and type
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/statistics/bridgeinterface/fields"
    response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
    return response
def getStatBulkRawData(vmanage, query, scrollId, count):
    """
    Get stats raw data
    
    Parameters:
    query	 (string):	Query string
	scrollId	 (string):	ES scroll Id
	count	 (string):	Result size
    
    Returns
    response    (dict)
    
    
    """
    query_string = vmanage.builder.generateQuery(query)
    endpoint     = f"https://{vmanage.host}:{vmanage.port}/dataservice/statistics/bridgeinterface/page?query={query_string}&scrollId={scrollId}&count={count}"
    response     = vmanage.client.apiCall(HttpMethods.GET, endpoint)
    return response
def getPostStatBulkRawData(vmanage, statsquerystring, scrollId, count):
    """
    Get stats raw data
    
    Parameters:
    statsquerystring:	Stats query string
	scrollId	 (string):	ES scroll Id
	count	 (string):	Result size
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/statistics/bridgeinterface/page?scrollId={scrollId}&count={count}"
    response = vmanage.client.apiCall(HttpMethods.POST, endpoint, statsquerystring)
    return response
def getStatQueryFields(vmanage):
    """
    Get query fields
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/statistics/bridgeinterface/query/fields"
    response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
    return response
