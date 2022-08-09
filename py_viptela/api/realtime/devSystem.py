def getStatDataRawData(vmanage, query):
    """
    Get stats raw data
    
    Parameters:
    query	 (string):	Query string
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/statistics/system?query={query}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getStatsRawData(vmanage, query):
    """
    Get stats raw data
    
    Parameters:
    query:	Stats query string
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/statistics/system"
    response = vmanage.apiCall("POST", endpoint, query)
    return response
def getAggregationDataByQuery(vmanage, query):
    """
    Get aggregated data based on input query and filters. The data can be filtered on time and other unique parameters based upon necessity and intended usage
    
    Parameters:
    query	 (string):	Query filter
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/statistics/system/aggregation?query={query}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getPostAggregationDataByQuery(vmanage, query):
    """
    Get aggregated data based on input query and filters. The data can be filtered on time and other unique parameters based upon necessity and intended usage
    
    Parameters:
    query:	Stats query string
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/statistics/system/aggregation"
    response = vmanage.apiCall("POST", endpoint, query)
    return response
def getPostAggregationAppDataByQuery(vmanage, query):
    """
    Get aggregated data based on input query and filters. The data can be filtered on time and other unique parameters based upon necessity and intended usage
    
    Parameters:
    query:	Stats query string
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/statistics/system/app-agg/aggregation"
    response = vmanage.apiCall("POST", endpoint, query)
    return response
def createDeviceSystemCPUStat(vmanage, query, deviceId):
    """
    Get device system CPU stats list
    
    Parameters:
    query	 (string):	Query filter
	deviceId	 (string):	Device IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/statistics/system/cpu?query={query}&deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getStatDataRawDataAsCSV(vmanage, query):
    """
    Get raw data with optional query as CSV
    
    Parameters:
    query	 (string):	Query string
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/statistics/system/csv?query={query}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getCount(vmanage, query):
    """
    Get response count of a query
    
    Parameters:
    query	 (string):	Query
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/statistics/system/doccount?query={query}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getCountPost(vmanage, query):
    """
    Get response count of a query
    
    Parameters:
    query:	Query
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/statistics/system/doccount"
    response = vmanage.apiCall("POST", endpoint, query)
    return response
def getStatDataFields(vmanage):
    """
    Get fields and type
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/statistics/system/fields"
    response = vmanage.apiCall("GET", endpoint)
    return response
def createDeviceSystemMemoryStat(vmanage, query, deviceId):
    """
    Get device system memory stats list
    
    Parameters:
    query	 (string):	Query filter
	deviceId	 (string):	Device IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/statistics/system/memory?query={query}&deviceId={deviceId}"
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
    
    endpoint = f"dataservice/statistics/system/page?query={query}&scrollId={scrollId}&count={count}"
    response = vmanage.apiCall("GET", endpoint)
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
    
    endpoint = f"dataservice/statistics/system/page?scrollId={scrollId}&count={count}"
    response = vmanage.apiCall("POST", endpoint, query)
    return response
def getStatQueryFields(vmanage):
    """
    Get query fields
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/statistics/system/query/fields"
    response = vmanage.apiCall("GET", endpoint)
    return response