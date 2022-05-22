from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class Manage(object):
    """
    Tenant Management API
    
    Implements GET POST DEL PUT methods for Tenant Management endpoints

    """

    def __init__(self, session, host, port):
        self.host = host
        self.port = port
        self.client = HttpMethods.HttpClient(session=session)
    
    
    def getAllTenants(self, deviceId):
        """
        Lists all the tenants on the vManage
        NOTE: In a multitenant vManage system, this API is only available in the Provider view.
        
        Parameters:
        deviceId	 (string):	List all tenants associated with a vSmart
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/tenant?deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def createTenant(self, tenantModel):
        """
        Create a new tenant in Multi-Tenant vManage
        NOTE: In a multitenant vManage system, this API is only available in the Provider view.
        
        Parameters:
        tenantModel:	Tenant model
        
        tenantModel Parameter example
        
        param = {
            "password": "12345",
            "tenantIdList": [
            "0f4f1c6e-47da-40c4-8517-9d1e918965d9",
            "6b7b23bf-5dba-4cca-a36c-1c3cc2254d68"
            ]
        }

        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/tenant"
        response = self.client.apiCall(HttpMethods.POST, endpoint, tenantModel)
        return response


    def createTenantAsync(self, tenantModel):
        """
        Create a new tenant in Multi-Tenant vManage asynchronously
        NOTE: In a multitenant vManage system, this API is only available in the Provider view.
        
        Parameters:
        tenantModel:	Tenant model
        
        tenantModel Parameter example
        
        param = {
            "password": "12345",
            "tenantIdList": [
            "0f4f1c6e-47da-40c4-8517-9d1e918965d9",
            "6b7b23bf-5dba-4cca-a36c-1c3cc2254d68"
            ]
        }

        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/tenant/async"
        response = self.client.apiCall(HttpMethods.POST, endpoint, tenantModel)
        return response


    def createTenantAsyncBulk(self, tenantModel):
        """
        Create multiple tenants on vManage asynchronously
        NOTE: In a multitenant vManage system, this API is only available in the Provider view.
        
        Parameters:
        tenantModel:	Tenant model
        
        tenantModel Parameter example
        
        param = {
            "password": "12345",
            "tenantIdList": [
            "0f4f1c6e-47da-40c4-8517-9d1e918965d9",
            "6b7b23bf-5dba-4cca-a36c-1c3cc2254d68"
            ]
        }

        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/tenant/bulk/async"
        response = self.client.apiCall(HttpMethods.POST, endpoint, tenantModel)
        return response


    def deleteTenantAsyncBulk(self, tenantModel):
        """
        Delete multiple tenants on vManage asynchronously
        NOTE: In a multitenant vManage system, this API is only available in the Provider view.
        
        Parameters:
        tenantModel:	Tenant model
        
        tenantModel Parameter example
        
        param = {
            "password": "12345",
            "tenantIdList": [
            "0f4f1c6e-47da-40c4-8517-9d1e918965d9",
            "6b7b23bf-5dba-4cca-a36c-1c3cc2254d68"
            ]
        }

        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/tenant/bulk/async"
        response = self.client.apiCall(HttpMethods.DELETE, endpoint, tenantModel)
        return response


    def getTenantvSmartMapping(self):
        """
        Retrieve mapping of tenants to vSmarts
        NOTE: In a multitenant vManage system, this API is only available in the Provider view.
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/tenant/vsmart"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def tenantvSmartMtMigrate(self):
        """
        Migrate tenants from single tenant vSmarts to multi-tenant capable vSmarts
        NOTE: In a multitenant vManage system, this API is only available in the Provider view.
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/tenant/vsmart-mt/migrate"
        response = self.client.apiCall(HttpMethods.POST, endpoint)
        return response


    def getTenantHostingCapacityOnvSmarts(self):
        """
        Lists all the vsmarts on the vManage and its tenant hosting capacity
        NOTE: In a multitenant vManage system, this API is only available in the Provider view.
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/tenant/vsmart/capacity"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getTenant(self, tenantId):
        """
        Get a tenant by Id
        NOTE: In a multitenant vManage system, this API is only available in the Provider view.
        
        Parameters:
        tenantId	 (string):	Tenant Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/tenant/{tenantId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def updateTenant(self, tenantModel, tenantId):
        """
        Update a tenant in Multi-Tenant vManage
        NOTE: In a multitenant vManage system, this API is only available in the Provider view.
        
        Parameters:
        tenantModel:	Tenant model
		tenantId	 (string):	Tenant Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/tenant/{tenantId}"
        response = self.client.apiCall(HttpMethods.PUT, endpoint, tenantModel)
        return response


    def deleteTenant(self, tenantModel, tenantId):
        """
        Delete a tenant by Id
        NOTE: In a multitenant vManage system, this API is only available in the Provider view.
        
        Parameters:
        tenantModel:	Tenant model
		tenantId	 (string):	Tenant Id
        
        tenantModel Parameter example
        
        param = {
            "password": "12345",
            "tenantIdList": [
            "0f4f1c6e-47da-40c4-8517-9d1e918965d9",
            "6b7b23bf-5dba-4cca-a36c-1c3cc2254d68"
            ]
        }
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/tenant/{tenantId}/delete"
        response = self.client.apiCall(HttpMethods.POST, endpoint, tenantModel)
        return response


    def switchTenant(self, tenantId):
        """
        Switch to a specific tenant
        NOTE: In a multitenant vManage system, this API is only available in the Provider view.
        
        Parameters:
        tenantId	 (string):	Tenant Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/tenant/{tenantId}/switch"
        response = self.client.apiCall(HttpMethods.POST, endpoint)
        return response


    def vSessionId(self, tenantId):
        """
        Get VSessionId for a specific tenant
        NOTE: In a multitenant vManage system, this API is only available in the Provider view.
        
        Parameters:
        tenantId	 (string):	Tenant Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/tenant/{tenantId}/vsessionid"
        response = self.client.apiCall(HttpMethods.POST, endpoint)
        return response


    def getAllTenantStatuses(self):
        """
        List all tenant status
        NOTE: In a multitenant vManage system, this API is only available in the Provider view.
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/tenantstatus"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def forceStatusCollection(self):
        """
        Force tenant status collection
        NOTE: In a multitenant vManage system, this API is only available in the Provider view.
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/tenantstatus/force"
        response = self.client.apiCall(HttpMethods.POST, endpoint)
        return response


