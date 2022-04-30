from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class Vedge(object):
    """
    Configuration - vEdge Template Policy API
    
    Implements GET POST DEL PUT methods for vEdgeTemplatePolicy endpoints

    """

    def __init__(self, session, host, port):
        self.host = host
        self.port = port
        self.client = HttpMethods.HttpClient(session=session)
    
    
    def generatePolicyTemplateList(self):
        """
        Get policy details
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/policy/vedge"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def createVEdgeTemplate(self, templatepolicy):
        """
        Create template
        
        Parameters:
        templatepolicy:	Template policy
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/policy/vedge"
        response = self.client.apiCall(HttpMethods.POST, endpoint, templatepolicy)
        return response


    def getVEdgeTemplate(self, policyId):
        """
        Get template
        
        Parameters:
        policyId	 (string):	Policy Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/policy/vedge/definition/{policyId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getVEdgePolicyDeviceList(self):
        """
        Get device list
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/policy/vedge/devices"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getDeviceListByPolicy(self, policyId):
        """
        Get device list by policy
        
        Parameters:
        policyId	 (string):	Policy Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/policy/vedge/devices/{policyId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def editVEdgeTemplate(self, templatepolicy, policyId):
        """
        Edit template
        
        Parameters:
        templatepolicy:	Template policy
		policyId	 (string):	Policy Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/policy/vedge/{policyId}"
        response = self.client.apiCall(HttpMethods.PUT, endpoint, templatepolicy)
        return response


    def deleteVEdgeTemplate(self, policyId):
        """
        Delete template
        
        Parameters:
        policyId	 (string):	Policy Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/policy/vedge/{policyId}"
        response = self.client.apiCall(HttpMethods.DELETE, endpoint)
        return response


    def changePolicyResourceGroup(self, policyId, resourceGroupName):
        """
        Change policy resource group
        
        Parameters:
        policyId	 (string):	Policy Id
		resourceGroupName	 (string):	Resrouce group name
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/policy/vedge/{resourceGroupName}/{policyId}"
        response = self.client.apiCall(HttpMethods.POST, endpoint)
        return response


