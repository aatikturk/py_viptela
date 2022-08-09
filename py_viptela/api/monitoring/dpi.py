def getStatDataRawData(vmanage, query):
    """
    Get stats raw data
    
    Parameters:
    query	 (string):	Query string
    
    Returns
    response    (dict)
    
    
    """
    query_string = vmanage.builder.generateQuery(query)
    endpoint     = f"https://{vmanage.host}:{vmanage.port}/dataservice/statistics/dpi?query={query_string}"
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
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/statistics/dpi"
    response = vmanage.client.apiCall("POST", endpoint, statsquerystring)
    return response
def getPostAggregationAppData(vmanage, queryfilter):
    """
    Get raw aggregated data and display applications with the highest utilization for a device
    
    Parameters:
    queryfilter:	Query filter
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/statistics/dpi/agg-app/aggregation"
    response = vmanage.client.apiCall("POST", endpoint, queryfilter)
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
    endpoint     = f"https://{vmanage.host}:{vmanage.port}/dataservice/statistics/dpi/aggregation?query={query_string}"
    response     = vmanage.client.apiCall("GET", endpoint)
    return response
def getPostAggregationData(vmanage, queryfilter):
    """
    Get raw aggregated data and display applications with the highest utilization for a device
    
    Parameters:
    queryfilter:	Query filter
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/statistics/dpi/aggregation"
    response = vmanage.client.apiCall("POST", endpoint, queryfilter)
    return response
def createDPIFlowsGridListQuery(vmanage, query, limit):
    """
    Get detailed DPI application flows list in a grid table
    
    Parameters:
    query	 (string):	Query string
	limit	 (string):	Query size
    
    Returns
    response    (dict)
    
    
    """
    query_string = vmanage.builder.generateQuery(query)
    endpoint     = f"https://{vmanage.host}:{vmanage.port}/dataservice/statistics/dpi/applications?query={query_string}&limit={limit}"
    response     = vmanage.client.apiCall("GET", endpoint)
    return response
def createDPISummary(vmanage, query, limit):
    """
    Get detailed DPI application flows summary
    
    Parameters:
    query	 (string):	Query string
	limit	 (string):	Query size
    
    Returns
    response    (dict)
    
    
    """
    query_string = vmanage.builder.generateQuery(query)
    endpoint     = f"https://{vmanage.host}:{vmanage.port}/dataservice/statistics/dpi/applications/summary?query={query_string}&limit={limit}"
    response     = vmanage.client.apiCall("GET", endpoint)
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
    endpoint     = f"https://{vmanage.host}:{vmanage.port}/dataservice/statistics/dpi/csv?query={query_string}"
    response     = vmanage.client.apiCall("GET", endpoint)
    return response
def getUniqueFlowCount(vmanage, deviceId, interval, application, window, family):
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
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/statistics/dpi/device/application/flowcount?deviceId={deviceId}&interval={interval}&application={application}&window={window}&family={family}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response
def createDPIDeviceGridData(vmanage, query, limit):
    """
    Get detailed DPI flows list
    
    Parameters:
    query	 (string):	Query string
	limit	 (string):	Query size
    
    Returns
    response    (dict)
    
    
    """
    query_string = vmanage.builder.generateQuery(query)
    endpoint     = f"https://{vmanage.host}:{vmanage.port}/dataservice/statistics/dpi/device/applications?query={query_string}&limit={limit}"
    response     = vmanage.client.apiCall("GET", endpoint)
    return response
def createDPIDeviceAndAppDetails(vmanage, query):
    """
    Get detailed DPI device and app list
    
    Parameters:
    query	 (string):	Query string
    
    Returns
    response    (dict)
    
    
    """
    query_string = vmanage.builder.generateQuery(query)
    endpoint     = f"https://{vmanage.host}:{vmanage.port}/dataservice/statistics/dpi/device/details/applications?query={query_string}"
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
    endpoint     = f"https://{vmanage.host}:{vmanage.port}/dataservice/statistics/dpi/doccount?query={query_string}"
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
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/statistics/dpi/doccount"
    response = vmanage.client.apiCall("POST", endpoint, query)
    return response
def getStatDataFields(vmanage):
    """
    Get fields and type
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/statistics/dpi/fields"
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
    endpoint     = f"https://{vmanage.host}:{vmanage.port}/dataservice/statistics/dpi/page?query={query_string}&scrollId={scrollId}&count={count}"
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
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/statistics/dpi/page?scrollId={scrollId}&count={count}"
    response = vmanage.client.apiCall("POST", endpoint, statsquerystring)
    return response
def getAggregationDataForPacketDup(vmanage, querystring):
    """
    Get time series aggregation data for packet duplication for an application over TLOCs if available
    
    Parameters:
    querystring:	Query string
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/statistics/dpi/pktdup/aggregation"
    response = vmanage.client.apiCall("POST", endpoint, querystring)
    return response
def getStatQueryFields(vmanage):
    """
    Get query fields
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/statistics/dpi/query/fields"
    response = vmanage.client.apiCall("GET", endpoint)
    return response
def getAggregationDataDPI(vmanage, querystring):
    """
    Get aggregation data and fec recovery rate if available
    
    Parameters:
    querystring:	Query string
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/statistics/dpi/recovery/aggregation"
    response = vmanage.client.apiCall("POST", endpoint, querystring)
    return response
