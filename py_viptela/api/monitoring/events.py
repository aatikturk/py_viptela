def getStatDataRawData(vmanage, query):
    """
    Get stats raw data
    
    Parameters:
    query	 (string):	Query string
    
    Returns
    response    (dict)
    
    
    """
    query_string = vmanage.builder.generateQuery(query)
    endpoint     = f"https://{vmanage.host}:{vmanage.port}/dataservice/event?query={query_string}"
    response     = vmanage.client.apiCall("GET", endpoint)
    return response
def getStatsRawData(vmanage, statsquerystring):
    """
    Get stats raw data
    
    Parameters:
    statsquerystring:	Stats query string
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/event"
    response = vmanage.client.apiCall("POST", endpoint, statsquerystring)
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
    endpoint     = f"https://{vmanage.host}:{vmanage.port}/dataservice/event/aggregation?query={query_string}"
    response     = vmanage.client.apiCall("GET", endpoint)
    return response
def getPostAggregationDataByQuery(vmanage, statsquerystring):
    """
    Get aggregated data based on input query and filters. The data can be filtered on time and other unique parameters based upon necessity and intended usage
    
    Parameters:
    statsquerystring:	Stats query string
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/event/aggregation"
    response = vmanage.client.apiCall("POST", endpoint, statsquerystring)
    return response
def getPostAggregationAppDataByQuery(vmanage, statsquerystring):
    """
    Get aggregated data based on input query and filters. The data can be filtered on time and other unique parameters based upon necessity and intended usage
    
    Parameters:
    statsquerystring:	Stats query string
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/event/app-agg/aggregation"
    response = vmanage.client.apiCall("POST", endpoint, statsquerystring)
    return response
def getComponentsAsKeyValue(vmanage):
    """
    Retrieve components as key/value pairs
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/event/component/keyvalue"
    response = vmanage.client.apiCall("GET", endpoint)
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
    endpoint     = f"https://{vmanage.host}:{vmanage.port}/dataservice/event/csv?query={query_string}"
    response     = vmanage.client.apiCall("GET", endpoint)
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
    endpoint     = f"https://{vmanage.host}:{vmanage.port}/dataservice/event/doccount?query={query_string}"
    response     = vmanage.client.apiCall("GET", endpoint)
    return response
def getCountPost(vmanage, query):
    """
    Get response count of a query
    
    Parameters:
    query:	Query
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/event/doccount"
    response = vmanage.client.apiCall("POST", endpoint, query)
    return response
def enableEventsFromFile(vmanage):
    """
    Set enable events from file flag
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/event/enable/fileprocess"
    response = vmanage.client.apiCall("GET", endpoint)
    return response
def getStatDataFields(vmanage):
    """
    Get fields and type
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/event/fields"
    response = vmanage.client.apiCall("GET", endpoint)
    return response
def getListenersInfo(vmanage):
    """
    Retrieve listener information
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/event/listeners"
    response = vmanage.client.apiCall("GET", endpoint)
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
    endpoint     = f"https://{vmanage.host}:{vmanage.port}/dataservice/event/page?query={query_string}&scrollId={scrollId}&count={count}"
    response     = vmanage.client.apiCall("GET", endpoint)
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
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/event/page?scrollId={scrollId}&count={count}"
    response = vmanage.client.apiCall("POST", endpoint, statsquerystring)
    return response
def getStatQueryFields(vmanage):
    """
    Get query fields
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/event/query/fields"
    response = vmanage.client.apiCall("GET", endpoint)
    return response
def createEventsQueryConfig(vmanage):
    """
    Create query configuration
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/event/query/input"
    response = vmanage.client.apiCall("GET", endpoint)
    return response
def findEvents(vmanage, level, deviceId, query):
    """
    Retrieve events
    
    Parameters:
    level	 (array):	Severity level
	deviceId	 (string):	Device IP
	query	 (string):	Query filter
    
    Returns
    response    (dict)
    
    
    """
    query_string = vmanage.builder.generateQuery(query)
    endpoint     = f"https://{vmanage.host}:{vmanage.port}/dataservice/event/severity?severity-level={level}&deviceId={deviceId}&query={query_string}"
    response     = vmanage.client.apiCall("GET", endpoint)
    return response
def getSeverityHistogram(vmanage, deviceId, query):
    """
    Retrieve severity histogram
    
    Parameters:
    deviceId	 (string):	Device IP
	query	 (string):	Query filter
    
    Returns
    response    (dict)
    
    
    """
    query_string = vmanage.builder.generateQuery(query)
    endpoint     = f"https://{vmanage.host}:{vmanage.port}/dataservice/event/severity/summary?deviceId={deviceId}&query={query_string}"
    response     = vmanage.client.apiCall("GET", endpoint)
    return response
def getEventTypesAsKeyValue(vmanage):
    """
    Retrieve event types as key/value pairs
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/event/types/keyvalue"
    response = vmanage.client.apiCall("GET", endpoint)
    return response
