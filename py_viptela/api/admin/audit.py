


def getStatDataRawAuditLogData(vmanage, inputQuery=None):
    """
    Get stat raw data
    
    Parameters:
    inputQuery	 (string):	Query filter
    
    Returns
    response    (dict)
    
    Sample input query
    
    q = {"size": 10000,
         "query":{
            "condition": "OR",
            "rules":[
            {
                "value":[
                    "6"
                ],
            "field":"entry_time",
            "type":"date",
            "operator":"last_n_weeks"
            }
            ]
            }
        }
    
    """
    query_string = vmanage.builder.generateQuery(inputQuery)
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/auditlog?inputQuery={query_string}"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response

def getRawPropertyData(vmanage, query):
    """
    Get raw property data with post action
    
    Parameters:
    query:	Query filter for getting stat raw data
    
    Returns
    response    (dict)
    
    Sample query filter
    
    q = {"size": 10000,
         "query":{
            "condition": "OR",
            "rules":[
            {
                "value":[
                    "6"
                ],
            "field":"entry_time",
            "type":"date",
            "operator":"last_n_weeks"
            }
            ]
            }
        }
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/auditlog"
    response = vmanage.client.apiCall(vmanage.POST, endpoint, query)
    return response

def getPropertyAggregationData(vmanage, inputQuery):
    """
    Get raw property data aggregated
    
    Parameters:
    inputQuery	 (string):	Query filter
    
    Returns
    response    (dict)
    
    
    """
    query_string = vmanage.builder.generateQuery(query_string)
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/auditlog/aggregation?inputQuery={query_string}"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response

def getPostPropertyAggregationData(vmanage, query):
    """
    Get raw property data aggregated with post action
    
    Parameters:
    query:	Query filter for getting stat raw data
    
    Returns
    response    (dict)
    
    Sample query filter
    q = {"size": 10000,
         "query":{
            "condition": "OR",
            "rules":[
            {
                "value":[
                    "6"
                ],
            "field":"entry_time",
            "type":"date",
            "operator":"last_n_weeks"
            }
            ]
            }
        }
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/auditlog/aggregation"
    response = vmanage.client.apiCall(vmanage.POST, endpoint, query)
    return response

def getCount(vmanage, query):
    """
    Get response count of a query
    
    Parameters:
    query	 (string):	Query
    
    Returns
    response    (dict)
    
    Sample query filter
    q = {"size": 10000,
         "query":{
            "condition": "OR",
            "rules":[
            {
                "value":[
                    "6"
                ],
            "field":"entry_time",
            "type":"date",
            "operator":"last_n_weeks"
            }
            ]
            }
        }
    
    """
    query_string = vmanage.builder.generateQuery(query_string)
    endpoint     = f"https://{vmanage.host}:{vmanage.port}/dataservice/auditlog/doccount?query={query_string}"
    response     = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response

def getCountPost(vmanage, query):
    """
    Get response count of a query
    
    Parameters:
    query:	Query
    
    Returns
    response    (dict)
    
    Sample query filter
    q = {"size": 10000,
         "query":{
            "condition": "OR",
            "rules":[
            {
                "value":[
                    "6"
                ],
            "field":"entry_time",
            "type":"date",
            "operator":"last_n_weeks"
            }
            ]
            }
        }
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/auditlog/doccount"
    response = vmanage.client.apiCall(vmanage.POST, endpoint, query)
    return response

def getStatDataFields(vmanage):
    """
    Get fields and type
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/auditlog/fields"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response

def getStatBulkRawPropertyData(vmanage, inputQuery, scrollId, count):
    """
    Get raw property data in bulk
    
    Parameters:
    inputQuery	 (string):	Query filter
	scrollId	 (string):	Offset of the query result
	count	 (string):	size of the query result
    
    Returns
    response    (dict)
    
    Sample query filter
    q = {"size": 10000,
         "query":{
            "condition": "OR",
            "rules":[
            {
                "value":[
                    "6"
                ],
            "field":"entry_time",
            "type":"date",
            "operator":"last_n_weeks"
            }
            ]
            }
        }
    """
    query_string = vmanage.builder.generateQuery(inputQuery)
    endpoint     = f"https://{vmanage.host}:{vmanage.port}/dataservice/auditlog/page?inputQuery={query_string}&scrollId={scrollId}&count={count}"
    response     = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response

def getPostStatBulkRawPropertyData(vmanage, query, scrollId, count):
    """
    Get raw property data in bulk with post action
    
    Parameters:
    query:	Query filter for getting stat raw data
	scrollId	 (string):	Offset of the query result
	count	 (string):	Size of the query result
    
    Returns
    response    (dict)
    
    Sample query filter
    q = {"size": 10000,
         "query":{
            "condition": "OR",
            "rules":[
            {
                "value":[
                    "6"
                ],
            "field":"entry_time",
            "type":"date",
            "operator":"last_n_weeks"
            }
            ]
            }
        }
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/auditlog/page?scrollId={scrollId}&count={count}"
    response = vmanage.client.apiCall(vmanage.POST, endpoint, query)
    return response

def getStatQueryFields(vmanage):
    """
    Get query fields
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/auditlog/query/fields"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response

def generateAuditLog(vmanage, query):
    """
    Get audit logs for last 3 hours
    
    Parameters:
    query	 (string):	Query filter
    
    Returns
    response    (dict)
    
    Sample query filter
    q = {"size": 10000,
         "query":{
            "condition": "OR",
            "rules":[
            {
                "value":[
                    "6"
                ],
            "field":"entry_time",
            "type":"date",
            "operator":"last_n_weeks"
            }
            ]
            }
        }
    
    """
    query_string = vmanage.builder.generateQuery(query)
    endpoint     = f"https://{vmanage.host}:{vmanage.port}/dataservice/auditlog/severity?query={query_string}"
    response     = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response

def getAuditSeverityCustomHistogram(vmanage, query):
    """
    Get audit log severity histogram
    
    Parameters:
    query	 (string):	Query filter
    
    Returns
    response    (dict)
    
    Sample query filter
    q = {"size": 10000,
         "query":{
            "condition": "OR",
            "rules":[
            {
                "value":[
                    "6"
                ],
            "field":"entry_time",
            "type":"date",
            "operator":"last_n_weeks"
            }
            ]
            }
        }
    """
    query_string = vmanage.builder.generateQuery(query)
    endpoint     = f"https://{vmanage.host}:{vmanage.port}/dataservice/auditlog/severity/summary?query={query_string}"
    response     = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response


