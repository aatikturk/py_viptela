from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class CustomApp(object):
    """
    Configuration - Policy Custom Application Builder API
    
    Implements GET POST DEL PUT methods for PolicyCustomApplicationBuilder endpoints

    """

    def __init__(self, session, host, port):
        self.host = host
        self.port = port
        self.client = HttpMethods.HttpClient(session=session)
    
    
    def MapTrafficProfiles(self, apppayload):
        """
        Set SLA class for policy cloud discovered applications
        
        Parameters:
        apppayload:	App payload
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/policy/clouddiscoveredapp"
        response = self.client.apiCall(HttpMethods.POST, endpoint, apppayload)
        return response


    def getCustomApps(self):
        """
        Get all policy custom applications
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/policy/customapp"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def create(self, apppayload):
        """
        Create a policy custom applications
        
        Parameters:
        apppayload:	App payload
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/policy/customapp"
        response = self.client.apiCall(HttpMethods.POST, endpoint, apppayload)
        return response


    def getById(self, id):
        """
        Get a policy custom applications
        
        Parameters:
        id	 (string):	Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/policy/customapp/{id}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def edit(self, apppayload, id):
        """
        Edit a policy custom applications
        
        Parameters:
        apppayload:	App payload
		id	 (string):	Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/policy/customapp/{id}"
        response = self.client.apiCall(HttpMethods.PUT, endpoint, apppayload)
        return response


    def delete(self, id):
        """
        Delete a policy custom applications
        
        Parameters:
        id	 (string):	Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/policy/customapp/{id}"
        response = self.client.apiCall(HttpMethods.DELETE, endpoint)
        return response


