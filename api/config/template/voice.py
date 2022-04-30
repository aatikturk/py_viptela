from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class Voice(object):
    """
    Configuration - Voice Template Policy API
    
    Implements GET POST DEL PUT methods for VoiceTemplatePolicy endpoints

    """

    def __init__(self, session, host, port):
        self.host = host
        self.port = port
        self.client = HttpMethods.HttpClient(session=session)
    
    
    def generateVoiceTemplateList(self):
        """
        Generate template list
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/policy/voice"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def createVoiceTemplate(self, policytemplate):
        """
        Create Template
        
        Parameters:
        policytemplate:	Policy template
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/policy/voice"
        response = self.client.apiCall(HttpMethods.POST, endpoint, policytemplate)
        return response


    def getTemplateById(self, policyId):
        """
        Get templates by policy Id
        
        Parameters:
        policyId	 (string):	Policy Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/policy/voice/definition/{policyId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getVoicePolicyDeviceList(self):
        """
        Get all device list
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/policy/voice/devices"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getDeviceListByPolicyId(self, policyId):
        """
        Get device list by policy Id
        
        Parameters:
        policyId	 (string):	Policy Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/policy/voice/devices/{policyId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def generateVoicePolicySummary(self):
        """
        Get templates that map a device model
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/policy/voice/summary"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getVoiceTemplatesForDevice(self, deviceModel):
        """
        Get templates that map a device model
        
        Parameters:
        deviceModel:  Device Model
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/policy/voice/{deviceModel}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def editVoiceTemplate(self, policytemplate, policyId):
        """
        Edit Template
        
        Parameters:
        policytemplate:	Policy template
		policyId	 (string):	Policy Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/policy/voice/{policyId}"
        response = self.client.apiCall(HttpMethods.PUT, endpoint, policytemplate)
        return response


    def deleteVoiceTemplate(self, policyId):
        """
        Delete Template
        
        Parameters:
        policyId	 (string):	Policy Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/policy/voice/{policyId}"
        response = self.client.apiCall(HttpMethods.DELETE, endpoint)
        return response


