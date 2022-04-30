from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class Backup(object):
    """
    Tenant Backup Restore API
    
    Implements GET POST DEL PUT methods for Tenant Backup Restore endpoints

    """

    def __init__(self, session, host, port):
        self.host = host
        self.port = port
        self.client = HttpMethods.HttpClient(session=session)
    
    
    def deleteBkp(self, fileName):
        """
        Delete all or a specific backup file stored in vManage
        NOTE: In a multitenant vManage system, this API is only available in the Provider view.
        
        Parameters:
        fileName	 (string):	File name
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/tenantbackup/delete?fileName={fileName}"
        response = self.client.apiCall(HttpMethods.DELETE, endpoint)
        return response


    def downloadBkpFile(self, path):
        """
        Download a Backup File that is already stored in vManage
        NOTE: In a multitenant vManage system, this API is only available in the Provider view.
        
        Parameters:
        path	 (string):	File path
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/tenantbackup/download/{path}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def exportBkp(self):
        """
        Trigger a backup of configuration database and store it in vManage
        NOTE: In a multitenant vManage system, this API is only available in the Provider view.
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/tenantbackup/export"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def importBkp(self):
        """
        Submit a previously backed up file and import the data and apply it to the configuraion database
        NOTE: In a multitenant vManage system, this API is only available in the Provider view.
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/tenantbackup/import"
        response = self.client.apiCall(HttpMethods.POST, endpoint)
        return response


    def listBkp(self):
        """
        List all backup files of a tenant stored in vManage
        NOTE: In a multitenant vManage system, this API is only available in the Provider view.
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/tenantbackup/list"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


