from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class FXO(object):
    """
    Configuration - Policy FXO Port Definition Builder API
    
    Implements GET POST DEL PUT methods for PolicyFXOPortDefinitionBuilder endpoints

    """

    def __init__(self, session, host, port):
        self.host = host
        self.port = port
        self.client = HttpMethods.HttpClient(session=session)
    
    
    def getDefinitions(self):
        """
        Get policy definitions
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/policy/definition/fxoport"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def create(self, policydefinition):
        """
        Create policy definition
        
        Parameters:
        policydefinition:	Policy definition
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/policy/definition/fxoport"
        response = self.client.apiCall(HttpMethods.POST, endpoint, policydefinition)
        return response


    def saveInBulk(self, policydefinition):
        """
        Create/Edit policy definitions in bulk
        
        Parameters:
        policydefinition:	Policy definition
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/policy/definition/fxoport/bulk"
        response = self.client.apiCall(HttpMethods.PUT, endpoint, policydefinition)
        return response


    def editMultiple(self, policydefinition, id):
        """
        Edit multiple policy definitions
        
        Parameters:
        policydefinition:	Policy definition
		id	 (string):	Policy Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/policy/definition/fxoport/multiple/{id}"
        response = self.client.apiCall(HttpMethods.PUT, endpoint, policydefinition)
        return response


    def preview(self, policydefinition):
        """
        Preview policy definition
        
        Parameters:
        policydefinition:	Policy definition
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/policy/definition/fxoport/preview"
        response = self.client.apiCall(HttpMethods.POST, endpoint, policydefinition)
        return response


    def previewById(self, id):
        """
        Preview policy definition
        
        Parameters:
        id	 (string):	Policy Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/policy/definition/fxoport/preview/{id}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def get(self, id):
        """
        Get a specific policy definitions
        
        Parameters:
        id	 (string):	Policy Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/policy/definition/fxoport/{id}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def edit(self, policydefinition, id):
        """
        Edit a policy definitions
        
        Parameters:
        policydefinition:	Policy definition
		id	 (string):	Policy Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/policy/definition/fxoport/{id}"
        response = self.client.apiCall(HttpMethods.PUT, endpoint, policydefinition)
        return response


    def delete(self, id):
        """
        Delete policy definition
        
        Parameters:
        id	 (string):	Policy Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/policy/definition/fxoport/{id}"
        response = self.client.apiCall(HttpMethods.DELETE, endpoint)
        return response


