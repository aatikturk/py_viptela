from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class DialPeer(object):
    """
    Configuration - Policy DialPeer Definition Builder API
    
    Implements GET POST DEL PUT methods for PolicyDialPeerDefinitionBuilder endpoints

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
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/policy/definition/dialpeer"
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
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/policy/definition/dialpeer"
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
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/policy/definition/dialpeer/bulk"
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
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/policy/definition/dialpeer/multiple/{id}"
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
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/policy/definition/dialpeer/preview"
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
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/policy/definition/dialpeer/preview/{id}"
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
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/policy/definition/dialpeer/{id}"
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
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/policy/definition/dialpeer/{id}"
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
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/policy/definition/dialpeer/{id}"
        response = self.client.apiCall(HttpMethods.DELETE, endpoint)
        return response


    def getDefinitionsSRST(self):
        """
        Get policy definitions
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/policy/definition/srstphoneprofile"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def createSRST(self, policydefinition):
        """
        Create policy definition
        
        Parameters:
        policydefinition:	Policy definition
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/policy/definition/srstphoneprofile"
        response = self.client.apiCall(HttpMethods.POST, endpoint, policydefinition)
        return response


    def saveInBulkSRST(self, policydefinition):
        """
        Create/Edit policy definitions in bulk
        
        Parameters:
        policydefinition:	Policy definition
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/policy/definition/srstphoneprofile/bulk"
        response = self.client.apiCall(HttpMethods.PUT, endpoint, policydefinition)
        return response


    def editMultipleSRST(self, policydefinition, id):
        """
        Edit multiple policy definitions
        
        Parameters:
        policydefinition:	Policy definition
		id	 (string):	Policy Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/policy/definition/srstphoneprofile/multiple/{id}"
        response = self.client.apiCall(HttpMethods.PUT, endpoint, policydefinition)
        return response


    def previewSRST(self, policydefinition):
        """
        Preview policy definition
        
        Parameters:
        policydefinition:	Policy definition
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/policy/definition/srstphoneprofile/preview"
        response = self.client.apiCall(HttpMethods.POST, endpoint, policydefinition)
        return response


    def previewByIdSRST(self, id):
        """
        Preview policy definition
        
        Parameters:
        id	 (string):	Policy Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/policy/definition/srstphoneprofile/preview/{id}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getSRST(self, id):
        """
        Get a specific policy definitions
        
        Parameters:
        id	 (string):	Policy Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/policy/definition/srstphoneprofile/{id}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def editSRST(self, policydefinition, id):
        """
        Edit a policy definitions
        
        Parameters:
        policydefinition:	Policy definition
		id	 (string):	Policy Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/policy/definition/srstphoneprofile/{id}"
        response = self.client.apiCall(HttpMethods.PUT, endpoint, policydefinition)
        return response


    def deleteSRST(self, id):
        """
        Delete policy definition
        
        Parameters:
        id	 (string):	Policy Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/policy/definition/srstphoneprofile/{id}"
        response = self.client.apiCall(HttpMethods.DELETE, endpoint)
        return response


