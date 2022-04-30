from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class Vsmart(object):
    """
    Configuration - vSmart Template Policy API
    
    Implements GET POST DEL PUT methods for vSmartTemplatePolicy endpoints

    """

    def __init__(self, session, host, port):
        self.host = host
        self.port = port
        self.client = HttpMethods.HttpClient(session=session)
    
    
    def getVSmartPolicyTemplateList(self):
        """
        Get all template vsmart policy list
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/policy/vsmart"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def createVSmartTemplate(self, templatepolicy):
        """
        Create template for given policy
        
        Parameters:
        templatepolicy:	Template policy
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/policy/vsmart"
        response = self.client.apiCall(HttpMethods.POST, endpoint, templatepolicy)
        return response


    def activatePolicyForCloudServices(self, templatepolicy, policyId):
        """
        Activate vsmart policy for a given policy id
        
        Parameters:
        templatepolicy:	Template policy
		policyId	 (string):	Policy Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/policy/vsmart/activate/central/{policyId}"
        response = self.client.apiCall(HttpMethods.POST, endpoint, templatepolicy)
        return response


    def activatePolicy(self, templatepolicy, policyId):
        """
        Activate vsmart policy for a given policy id
        
        Parameters:
        templatepolicy:	Template policy
		policyId	 (string):	Policy Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/policy/vsmart/activate/{policyId}"
        response = self.client.apiCall(HttpMethods.POST, endpoint, templatepolicy)
        return response


    def editTemplateWithoutLockChecks(self, templatepolicy, policyId):
        """
        Edit template for given policy id to allow for multiple component edits
        
        Parameters:
        templatepolicy:	Template policy
		policyId	 (string):	Policy Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/policy/vsmart/central/{policyId}"
        response = self.client.apiCall(HttpMethods.PUT, endpoint, templatepolicy)
        return response


    def checkVSmartConnectivityStatus(self):
        """
        Check VSmart Connectivity Status
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/policy/vsmart/connectivity/status"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def deActivatePolicy(self, policyId):
        """
        Deactivate vsmart policy for a given policy id
        
        Parameters:
        policyId	 (string):	Policy Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/policy/vsmart/deactivate/{policyId}"
        response = self.client.apiCall(HttpMethods.POST, endpoint)
        return response


    def getTemplateByPolicyId(self, policyId):
        """
        Get template policy definition by policy id
        
        Parameters:
        policyId	 (string):	Policy Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/policy/vsmart/definition/{policyId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def QosmosNbarMigrationWarning(self):
        """
        Qosmos Nbar migration
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/policy/vsmart/qosmos_nbar_migration_warning"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def editVSmartTemplate(self, templatepolicy, policyId):
        """
        Edit template for given policy id
        
        Parameters:
        templatepolicy:	Template policy
		policyId	 (string):	Policy Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/policy/vsmart/{policyId}"
        response = self.client.apiCall(HttpMethods.PUT, endpoint, templatepolicy)
        return response


    def deleteVSmartTemplate(self, policyId):
        """
        Delete template for a given policy id
        
        Parameters:
        policyId	 (string):	Policy Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/policy/vsmart/{policyId}"
        response = self.client.apiCall(HttpMethods.DELETE, endpoint)
        return response


