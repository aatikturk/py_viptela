def getSulStatDataRawData(vmanage, query):
    """
    Get security connection events stats raw data
    
    Parameters:
    query	 (string):	Query string
    
    Returns
    response    (dict)
    
    
    """
    query_string = vmanage.builder.generateQuery(query)
    endpoint     = f"https://{vmanage.host}:{vmanage.port}/dataservice/statistics/sul/connections?query={query_string}"
    response     = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response
def getStatsRawData(vmanage, statsquerystring):
    """
    Get stats raw data
    
    Parameters:
    statsquerystring:	Stats query string
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/statistics/sul/connections"
    response = vmanage.client.apiCall(vmanage.POST, endpoint, statsquerystring)
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
    endpoint     = f"https://{vmanage.host}:{vmanage.port}/dataservice/statistics/sul/connections/aggregation?query={query_string}"
    response     = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response
def getPostAggregationDataByQuery(vmanage, statsquerystring):
    """
    Get aggregated data based on input query and filters. The data can be filtered on time and other unique parameters based upon necessity and intended usage
    
    Parameters:
    statsquerystring:	Stats query string
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/statistics/sul/connections/aggregation"
    response = vmanage.client.apiCall(vmanage.POST, endpoint, statsquerystring)
    return response
def getPostAggregationAppDataByQuery(vmanage, statsquerystring):
    """
    Get aggregated data based on input query and filters. The data can be filtered on time and other unique parameters based upon necessity and intended usage
    
    Parameters:
    statsquerystring:	Stats query string
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/statistics/sul/connections/app-agg/aggregation"
    response = vmanage.client.apiCall(vmanage.POST, endpoint, statsquerystring)
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
    endpoint     = f"https://{vmanage.host}:{vmanage.port}/dataservice/statistics/sul/connections/csv?query={query_string}"
    response     = vmanage.client.apiCall(vmanage.GET, endpoint)
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
    endpoint     = f"https://{vmanage.host}:{vmanage.port}/dataservice/statistics/sul/connections/doccount?query={query_string}"
    response     = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response
def getCountPost(vmanage, query):
    """
    Get response count of a query
    
    Parameters:
    query:	Query
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/statistics/sul/connections/doccount"
    response = vmanage.client.apiCall(vmanage.POST, endpoint, query)
    return response
def getStatDataFields(vmanage):
    """
    Get fields and type
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/statistics/sul/connections/fields"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response
def getFilterPolicyNameList(vmanage, policyType, query):
    """
    Get filter Policy Name list
    
    Parameters:
    policyType	 (string):	Policy type
	query	 (string):	query string
    
    Returns
    response    (dict)
    
    
    """
    query_string = vmanage.builder.generateQuery(query)
    endpoint     = f"https://{vmanage.host}:{vmanage.port}/dataservice/statistics/sul/connections/filter/policy_name/{policyType}?query={query_string}"
    response     = vmanage.client.apiCall(vmanage.GET, endpoint)
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
    endpoint     = f"https://{vmanage.host}:{vmanage.port}/dataservice/statistics/sul/connections/page?query={query_string}&scrollId={scrollId}&count={count}"
    response     = vmanage.client.apiCall(vmanage.GET, endpoint)
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
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/statistics/sul/connections/page?scrollId={scrollId}&count={count}"
    response = vmanage.client.apiCall(vmanage.POST, endpoint, statsquerystring)
    return response
def getStatQueryFields(vmanage):
    """
    Get query fields
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/statistics/sul/connections/query/fields"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response
