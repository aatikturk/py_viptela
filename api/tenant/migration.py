from query_builder import Builder
import HttpMethods

class Migration(object):
    """
    Tenant Migration API
    
    Implements GET POST DEL PUT methods for TenantMigration endpoints

    """

    def __init__(self, session, host, port):
        self.host = host
        self.port = port
        self.client = HttpMethods.HttpClient(session=session)
    
    
    def downloadTenantData(self, path):
        """
        Download tenant data
        
        Parameters:
        path	 (string):	File path
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/tenantmigration/download/{path}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def exportTenantData(self, bodyParameter):
        """
        Export tenant data
        
        Parameters:
        bodyParameter:	Description
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/tenantmigration/export"
        response = self.client.apiCall(HttpMethods.POST, endpoint, bodyParameter)
        return response


    def importTenantData(self):
        """
        Import tenant data
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/tenantmigration/import"
        response = self.client.apiCall(HttpMethods.POST, endpoint)
        return response


    def getMigrationToken(self, migrationId):
        """
        Get migration token
        
        Parameters:
        migrationId	 (string):	Migration Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/tenantmigration/migrationToken?migrationId={migrationId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def reTriggerNetworkMigration(self):
        """
        Re-trigger network migration
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/tenantmigration/networkMigration"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def migrateNetwork(self, networkMigration):
        """
        Migrate network
        
        Parameters:
        networkMigration:	Network migration
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/tenantmigration/networkMigration"
        response = self.client.apiCall(HttpMethods.POST, endpoint, networkMigration)
        return response


