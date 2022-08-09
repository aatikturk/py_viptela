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
    endpoint     = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/history?query={query_string}"
    response     = vmanage.client.apiCall(HttpMethods.GET, endpoint)
    return response

def getStatsRawData(vmanage, query):
    """
    Get stats raw data
    
    Parameters:
    query:	Stats query string
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/history"
    response = vmanage.client.apiCall(HttpMethods.POST, endpoint, query)
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
    endpoint     = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/history/aggregation?query={query_string}"
    response     = vmanage.client.apiCall(HttpMethods.GET, endpoint)
    return response

def getPostAggregationDataByQuery(vmanage, query):
    """
    Get aggregated data based on input query and filters. The data can be filtered on time and other unique parameters based upon necessity and intended usage
    
    Parameters:
    query:	Stats query string
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/history/aggregation"
    response = vmanage.client.apiCall(HttpMethods.POST, endpoint, query)
    return response

def getPostAggregationAppDataByQuery(vmanage, query):
    """
    Get aggregated data based on input query and filters. The data can be filtered on time and other unique parameters based upon necessity and intended usage
    
    Parameters:
    query:	Stats query string
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/history/app-agg/aggregation"
    response = vmanage.client.apiCall(HttpMethods.POST, endpoint, query)
    return response

def getLastThousandConfigList(vmanage, deviceId, query):
    """
    Get device config history
    
    Parameters:
    deviceId	 (string):	Device Id
	query	 (string):	Query filter
    
    Returns
    response    (dict)
    
    
    """
    query_string = vmanage.builder.generateQuery(query)
    endpoint     = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/history/config?deviceId={deviceId}&query={query_string}"
    response     = vmanage.client.apiCall(HttpMethods.GET, endpoint)
    return response

def getConfigDiff(vmanage, config_id1, config_id2):
    """
    Get diff of two configs
    
    Parameters:
    config_id1	 (string):	Config Id one
	config_id2	 (string):	Config Id two
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/history/config/diff/list?config_id1={config_id1}&config_id2={config_id2}"
    response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
    return response

def getDeviceConfig(vmanage, config_id):
    """
    Get device config
    
    Parameters:
    config_id	 (string):	Config Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/history/config/{config_id}"
    response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
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
    endpoint     = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/history/csv?query={query_string}"
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
    endpoint     = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/history/doccount?query={query_string}"
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
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/history/doccount"
    response = vmanage.client.apiCall(HttpMethods.POST, endpoint, query)
    return response

def getStatDataFields(vmanage):
    """
    Get fields and type
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/history/fields"
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
    endpoint     = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/history/page?query={query_string}&scrollId={scrollId}&count={count}"
    response     = vmanage.client.apiCall(HttpMethods.GET, endpoint)
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
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/history/page?scrollId={scrollId}&count={count}"
    response = vmanage.client.apiCall(HttpMethods.POST, endpoint, query)
    return response

def getStatQueryFields(vmanage):
    """
    Get query fields
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/history/query/fields"
    response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
    return response
