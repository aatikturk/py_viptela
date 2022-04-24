from query_builder import Builder
import HttpMethods

class Manage(object):
    """
    Tenant Management API
    
    Implements GET POST DEL PUT methods for TenantManagement endpoints

    """

    def __init__(self, session, host, port):
        self.host = host
        self.port = port
        self.client = HttpMethods.HttpClient(session=session)
    
    
    def getAllTenants(self, deviceId):
        """
        Lists all the tenants on the vManage<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.
        
        Parameters:
        deviceId	 (string):	List all tenants associated with a vSmart
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/tenant?deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def createTenant(self, tenantmodel):
        """
        Create a new tenant in Multi-Tenant vManage<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.
        
        Parameters:
        tenantmodel:	Tenant model
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/tenant"
        response = self.client.apiCall(HttpMethods.POST, endpoint, tenantmodel)
        return response


    def createTenantAsync(self, tenantmodel):
        """
        Create a new tenant in Multi-Tenant vManage asynchronously<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.
        
        Parameters:
        tenantmodel:	Tenant model
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/tenant/async"
        response = self.client.apiCall(HttpMethods.POST, endpoint, tenantmodel)
        return response


    def createTenantAsyncBulk(self, tenantmodel):
        """
        Create multiple tenants on vManage asynchronously<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.
        
        Parameters:
        tenantmodel:	Tenant model
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/tenant/bulk/async"
        response = self.client.apiCall(HttpMethods.POST, endpoint, tenantmodel)
        return response


    def deleteTenantAsyncBulk(self, tenantmodel):
        """
        Delete multiple tenants on vManage asynchronously<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.
        
        Parameters:
        tenantmodel:	Tenant model
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/tenant/bulk/async"
        response = self.client.apiCall(HttpMethods.DELETE, endpoint, tenantmodel)
        return response


    def getTenantvSmartMapping(self):
        """
        Retrieve mapping of tenants to vSmarts<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/tenant/vsmart"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def tenantvSmartMtMigrate(self):
        """
        Migrate tenants from single tenant vSmarts to multi-tenant capable vSmarts<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/tenant/vsmart-mt/migrate"
        response = self.client.apiCall(HttpMethods.POST, endpoint)
        return response


    def getTenantHostingCapacityOnvSmarts(self):
        """
        Lists all the vsmarts on the vManage and its tenant hosting capacity<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/tenant/vsmart/capacity"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getTenant(self, tenantId):
        """
        Get a tenant by Id<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.
        
        Parameters:
        tenantId	 (string):	Tenant Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/tenant/{tenantId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def updateTenant(self, tenantmodel, tenantId):
        """
        Update a tenant in Multi-Tenant vManage<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.
        
        Parameters:
        tenantmodel:	Tenant model
		tenantId	 (string):	Tenant Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/tenant/{tenantId}"
        response = self.client.apiCall(HttpMethods.PUT, endpoint, tenantmodel)
        return response


    def deleteTenant(self, tenantmodel, tenantId):
        """
        Delete a tenant by Id<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.
        
        Parameters:
        tenantmodel:	Tenant model
		tenantId	 (string):	Tenant Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/tenant/{tenantId}/delete"
        response = self.client.apiCall(HttpMethods.POST, endpoint, tenantmodel)
        return response


    def switchTenant(self, tenantId):
        """
        Switch to a specific tenant<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.
        
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
        Get VSessionId for a specific tenant<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.
        
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
        List all tenant status<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/tenantstatus"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def forceStatusCollection(self):
        """
        Force tenant status collection<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/tenantstatus/force"
        response = self.client.apiCall(HttpMethods.POST, endpoint)
        return response


