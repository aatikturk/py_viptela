from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class Security(object):
    """
    Configuration - Security Template Policy API
    
    Implements GET POST DEL PUT methods for SecurityTemplatePolicy endpoints

    """

    def __init__(self, session, host, port):
        self.host = host
        self.port = port
        self.client = HttpMethods.HttpClient(session=session)
    
    
    def generateSecurityTemplateList(self, mode):
        """
        Generate template list
        
        Parameters:
        mode	 (string):	Mode
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/policy/security?mode={mode}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def createSecurityTemplate(self, policytemplate):
        """
        Create Template
        
        Parameters:
        policytemplate:	Policy template
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/policy/security"
        response = self.client.apiCall(HttpMethods.POST, endpoint, policytemplate)
        return response


    def getSecurityTemplate(self, policyId):
        """
        Get Template
        
        Parameters:
        policyId	 (string):	Policy Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/policy/security/definition/{policyId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getSecurityPolicyDeviceList(self):
        """
        Get device list
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/policy/security/devices"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getDeviceListById(self, policyId):
        """
        Get device list by Id
        
        Parameters:
        policyId	 (string):	Policy Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/policy/security/devices/{policyId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def editTemplateWithLenientLock(self, policytemplate, policyId):
        """
        Edit Template
        
        Parameters:
        policytemplate:	Policy template
		policyId	 (string):	Policy Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/policy/security/staging/{policyId}"
        response = self.client.apiCall(HttpMethods.PUT, endpoint, policytemplate)
        return response


    def generateSecurityPolicySummary(self):
        """
        Generate security policy summary
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/policy/security/summary"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getSecurityTemplatesForDevice(self, deviceModel):
        """
        Get templates that map a device model
        
        Parameters:
        Parameter Description
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/policy/security/{deviceModel}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def editSecurityTemplate(self, policytemplate, policyId):
        """
        Edit Template
        
        Parameters:
        policytemplate:	Policy template
		policyId	 (string):	Policy Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/policy/security/{policyId}"
        response = self.client.apiCall(HttpMethods.PUT, endpoint, policytemplate)
        return response


    def deleteSecurityTemplate(self, policyId):
        """
        Delete Template
        
        Parameters:
        policyId	 (string):	Policy Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/policy/security/{policyId}"
        response = self.client.apiCall(HttpMethods.DELETE, endpoint)
        return response


