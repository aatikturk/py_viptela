from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class Audit(object):
    """
    Administration - Audit Log API
    
    Implements GET POST DEL PUT methods for AuditLog endpoints

    """

    def __init__(self, session, host, port):
        self.host = host
        self.port = port
        self.client = HttpMethods.HttpClient(session=session)
    
    
    def getStatDataRawAuditLogData(self, inputQuery):
        """
        Get stat raw data
        
        Parameters:
        inputQuery	 (string):	Query filter
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/auditlog?inputQuery={inputQuery}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getRawPropertyData(self, query):
        """
        Get raw property data with post action
        
        Parameters:
        query:	Query filter for getting stat raw data
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/auditlog"
        response = self.client.apiCall(HttpMethods.POST, endpoint, query)
        return response


    def getPropertyAggregationData(self, inputQuery):
        """
        Get raw property data aggregated
        
        Parameters:
        inputQuery	 (string):	Query filter
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/auditlog/aggregation?inputQuery={inputQuery}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getPostPropertyAggregationData(self, query):
        """
        Get raw property data aggregated with post action
        
        Parameters:
        query:	Query filter for getting stat raw data
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/auditlog/aggregation"
        response = self.client.apiCall(HttpMethods.POST, endpoint, query)
        return response


    def getCount(self, query):
        """
        Get response count of a query
        
        Parameters:
        query	 (string):	Query
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/auditlog/doccount?query={query}"
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
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/auditlog/doccount"
        response = self.client.apiCall(HttpMethods.POST, endpoint, query)
        return response


    def getStatDataFields(self):
        """
        Get fields and type
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/auditlog/fields"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getStatBulkRawPropertyData(self, inputQuery, scrollId, count):
        """
        Get raw property data in bulk
        
        Parameters:
        inputQuery	 (string):	Query filter
		scrollId	 (string):	Offset of the query result
		count	 (string):	size of the query result
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/auditlog/page?inputQuery={inputQuery}&scrollId={scrollId}&count={count}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getPostStatBulkRawPropertyData(self, query, scrollId, count):
        """
        Get raw property data in bulk with post action
        
        Parameters:
        query:	Query filter for getting stat raw data
		scrollId	 (string):	Offset of the query result
		count	 (string):	Size of the query result
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/auditlog/page?scrollId={scrollId}&count={count}"
        response = self.client.apiCall(HttpMethods.POST, endpoint, query)
        return response


    def getStatQueryFields(self):
        """
        Get query fields
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/auditlog/query/fields"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def generateAuditLog(self, query):
        """
        Get audit logs for last 3 hours
        
        Parameters:
        query	 (string):	Query filter
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/auditlog/severity?query={query}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getAuditSeverityCustomHistogram(self, query):
        """
        Get audit log severity histogram
        
        Parameters:
        query	 (string):	Query filter
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/auditlog/severity/summary?query={query}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


