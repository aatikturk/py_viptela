def getHealthSummary(vmanage, type, limit, query):
    """
    Get application-aware routing statistics summary from device
    
    Parameters:
    type	 (string):	Type
	limit	 (integer):	Query result size
	query	 (string):	Query filter
    
    Returns
    response    (dict)
    
    
    """
    query_string = vmanage.builder.generateQuery(query)
    endpoint     = f"https://{vmanage.host}:{vmanage.port}/dataservice/statistics/approute/transport/summary/{type}?limit={limit}&query={query_string}"
    response     = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response
def getHealth(vmanage, type, query, limit):
    """
    Get application-aware routing statistics from device
    
    Parameters:
    type	 (string):	Type
	query    (string):  Query filter
	limit	 (string):	Query result size
    
    Returns
    response    (dict)
    
    
    """
    query_string = vmanage.builder.generateQuery(query)
    endpoint     = f"https://{vmanage.host}:{vmanage.port}/dataservice/statistics/approute/transport/{type}?query={query_string}&limit={limit}"
    response     = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response
