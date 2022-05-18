from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class Migration(object):
    """
    Tenant Migration API
    
    Implements GET POST DEL PUT methods for Tenant Migration endpoints

    """

    def __init__(self, session, host, port):
        self.host = host
        self.port = port
        self.client = HttpMethods.HttpClient(session=session)
    
    
    def downloadData(self, path):
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


    def exportData(self, bodyParameter):
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


    def importData(self):
        """
        Import tenant data
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/tenantmigration/import"
        response = self.client.apiCall(HttpMethods.POST, endpoint)
        return response


    def getToken(self, migrationId):
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


    def reTrigger(self):
        """
        Re-trigger network migration
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/tenantmigration/networkMigration"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def migrate(self, networkMigration):
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


