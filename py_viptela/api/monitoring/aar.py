import json

def getStatDataRawData(vmanage, query=None):
    """
    Get stats raw data
    
    Parameters:
    query	 (string):	Query dict
    
    Returns
    response    (dict)
    
    
    """
    if query:
        query_string = vmanage.builder.generateQuery(query)
        endpoint = f"dataservice/statistics/approute?query={query_string}"
    else:
        endpoint = f"dataservice/statistics/approute"
    response     = vmanage.apiCall("GET", endpoint)
    return response
def getStatsRawData(vmanage, query):
    """
    Get stats raw data
    
    Parameters:
    query:	Stats query dict
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/statistics/approute"
    response     = vmanage.apiCall("POST", endpoint, json.dumps(query))
    return response
def getAggregationDataByQuery(vmanage, query):
    """
    Get aggregated data based on input query and filters. The data can be filtered on time and other unique parameters based upon necessity and intended usage
    
    Parameters:
    query	 (string):	Query filter dict
    
    Returns
    response    (dict)
    
    
    """
    query_string = vmanage.builder.generateQuery(query)
    endpoint = f"dataservice/statistics/approute/aggregation?query={query_string}"
    response     = vmanage.apiCall("GET", endpoint)
    return response
def getPostAggregationDataByQuery(vmanage, query):
    """
    Get aggregated data based on input query and filters. The data can be filtered on time and other unique parameters based upon necessity and intended usage
    
    Parameters:
    query:	Stats query dict
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/statistics/approute/aggregation"
    response     = vmanage.apiCall("POST", endpoint, json.dumps(query))
    return response
def getPostAggregationAppDataByQuery(vmanage, query):
    """
    Get aggregated data based on input query and filters. The data can be filtered on time and other unique parameters based upon necessity and intended usage
    
    Parameters:
    query:	Stats query dict
    
    Returns
    response    (dict)
    
    
    """
    endpoint = f"dataservice/statistics/approute/app-agg/aggregation"
    response     = vmanage.apiCall("POST", endpoint, query)
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
    endpoint = f"dataservice/statistics/approute/csv?query={query_string}"
    response     = vmanage.apiCall("GET", endpoint)
    return response
def getApprouteGridStat(vmanage, query):
    """
    Get statistics for top applications per tunnel in a grid table
    
    Parameters:
    query	 (string):	Query filter
    
    Returns
    response    (dict)
    
    
    """
    query_string = vmanage.builder.generateQuery(query)
    endpoint = f"dataservice/statistics/approute/device/tunnel/summary?query={query_string}"
    response     = vmanage.apiCall("GET", endpoint)
    return response
def getTunnel(vmanage, query):
    """
    Get statistics for top applications per tunnel in a grid table
    
    Parameters:
    query	 (string):	Query filter
    
    Returns
    response    (dict)
    
    
    """
    query_string = vmanage.builder.generateQuery(query)
    endpoint = f"dataservice/statistics/approute/device/tunnels?query={query_string}"
    response     = vmanage.apiCall("GET", endpoint)
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
    endpoint = f"dataservice/statistics/approute/doccount?query={query_string}"
    response     = vmanage.apiCall("GET", endpoint)
    return response
def getCountPost(vmanage, query):
    """
    Get response count of a query
    
    Parameters:
    query:	Query
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/statistics/approute/doccount"
    response = vmanage.apiCall("POST", endpoint, query)
    return response
def getAggregationDataAppRoute(vmanage, queryfilter):
    """
    Get aggregation data and fec recovery rate
    
    Parameters:
    queryfilter:	Query filter
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/statistics/approute/fec/aggregation"
    response = vmanage.apiCall("POST", endpoint, queryfilter)
    return response
def getStatDataFields(vmanage):
    """
    Get fields and type
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/statistics/approute/fields"
    response = vmanage.apiCall("GET", endpoint)
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
    endpoint = f"dataservice/statistics/approute/page?query={query_string}&scrollId={scrollId}&count={count}"
    response     = vmanage.apiCall("GET", endpoint)
    return response
def getPostStatBulkRawData(vmanage, query, scrollId, count):
    """
    Get stats raw data
    
    Parameters:
    query:	Stats query string
	scrollId	 (string):	ES scroll Id
	count	 (string):	Result size
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/statistics/approute/page?scrollId={scrollId}&count={count}"
    response = vmanage.apiCall("POST", endpoint, query)
    return response
def getStatQueryFields(vmanage):
    """
    Get query fields
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/statistics/approute/query/fields"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getTunnelChart(vmanage, type, query):
    """
    Get tunnel top statistics in as chart
    
    Parameters:
    type	 (string):	Type
	query	 (string):	Query filter
    
    Returns
    response    (dict)
    
    
    """
    query_string = vmanage.builder.generateQuery(query)
    endpoint = f"dataservice/statistics/approute/tunnel/{type}/summary?query={query_string}"
    response     = vmanage.apiCall("GET", endpoint)
    return response
def getTunnelsSummary(vmanage, type, query, limit):
    """
    Get tunnel top statistics from device
    
    Parameters:
    type	 (string):	Type
	query	 (string):	Query filter
	limit	 (integer):	Query result size
    
    Returns
    response    (dict)
    
    
    """
    query_string = vmanage.builder.generateQuery(query)
    endpoint = f"dataservice/statistics/approute/tunnels/summary/{type}?query={query_string}&limit={limit}"
    response     = vmanage.apiCall("GET", endpoint)
    return response
def getTunnels(vmanage, type, query, limit):
    """
    Get tunnel top statistics from device
    
    Parameters:
    type	 (string):	Type
	query	 (string):	Query filter
	limit	 (integer):	Query result size
    
    Returns
    response    (dict)
    
    
    """
    query_string = vmanage.builder.generateQuery(query)
    endpoint = f"dataservice/statistics/approute/tunnels/{type}?query={query_string}&limit={limit}"
    response     = vmanage.apiCall("GET", endpoint)
    return response

def getTunnelsHealth(vmanage, dtype, limit):
    endpoint = f"dataservice/statistics/approute/tunnels/health/{dtype}?limit={limit}"
    response = vmanage.apiCall("GET", endpoint)
    return response