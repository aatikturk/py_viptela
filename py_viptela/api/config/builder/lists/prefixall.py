from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class PrefixAll(object):
    """
    Configuration - Policy Prefix for All Types of Lists Builder API
    
    Implements GET POST DEL PUT methods for PolicyPrefixforAllTypesofListsBuilder endpoints

    """

    def __init__(self, session, host, port):
        self.host = host
        self.port = port
        self.client = HttpMethods.HttpClient(session=session)
    
    
    def getListsForAllPrefixes(self):
        """
        Get lists for all prefixes
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/policy/list/ipprefixall"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def create(self, policylist):
        """
        Create policy list
        
        Parameters:
        policylist:	Policy list
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/policy/list/ipprefixall"
        response = self.client.apiCall(HttpMethods.POST, endpoint, policylist)
        return response


    def preview(self, policylist):
        """
        Preview a policy list based on the policy list type
        
        Parameters:
        policylist:	Policy list
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/policy/list/ipprefixall/preview"
        response = self.client.apiCall(HttpMethods.POST, endpoint, policylist)
        return response


    def previewById(self, id):
        """
        Preview a specific policy list entry based on id provided
        
        Parameters:
        id	 (string):	Policy Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/policy/list/ipprefixall/preview/{id}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getListsById(self, id):
        """
        Get a specific policy list based on the id
        
        Parameters:
        id	 (string):	Policy Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/policy/list/ipprefixall/{id}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def edit(self, policylist, id):
        """
        Edit policy list entries for a specific type of policy list
        
        Parameters:
        policylist:	Policy list
		id	 (string):	Policy Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/policy/list/ipprefixall/{id}"
        response = self.client.apiCall(HttpMethods.PUT, endpoint, policylist)
        return response


    def delete(self, id):
        """
        Delete policy list entry for a specific type of policy list
        
        Parameters:
        id	 (string):	Policy Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/policy/list/ipprefixall/{id}"
        response = self.client.apiCall(HttpMethods.DELETE, endpoint)
        return response


