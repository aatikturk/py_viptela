from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class Master(object):
    """
    Configuration - Template Master API
    
    Implements GET POST DEL PUT methods for TemplateMaster endpoints

    """

    def __init__(self, session, host, port):
        self.host = host
        self.port = port
        self.client = HttpMethods.HttpClient(session=session)
    
    
    def getMasterTemplateList(self, feature):
        """
        Generate template list
        NOTE: In a multitenant vManage system, this API is only available in the Provider view.
        
        Parameters:
        feature	 (string):	Feature
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/device?feature={feature}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def createCLITemplate(self, createtemplaterequest):
        """
        Create CLI template
        NOTE: In a multitenant vManage system, this API is only available in the Provider view.
        
        Parameters:
        createtemplaterequest:	Create template request
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/device/cli"
        response = self.client.apiCall(HttpMethods.POST, endpoint, createtemplaterequest)
        return response


    def createMasterTemplate(self, request):
        """
        Create a device template from feature templates and sub templates
        NOTE: In a multitenant vManage system, this API is only available in the Provider view.
        
        Parameters:
        request:	Create template request
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/device/feature"
        response = self.client.apiCall(HttpMethods.POST, endpoint, request)
        return response


    def isMigrationRequired(self):
        """
        Check if any device templates need migration
        NOTE: In a multitenant vManage system, this API is only available in the Provider view.
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/device/is_migration_required"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getTemplateForMigration(self, hasAAA):
        """
        Generate a list of templates which require migration
        NOTE: In a multitenant vManage system, this API is only available in the Provider view.
        
        Parameters:
        hasAAA	 (boolean):	Return only those uses AAA
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/device/migration?hasAAA={hasAAA}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def migrateTemplates(self, id, prefix, includeAll):
        """
        Migrate the device templates given the template Ids
        
        Parameters:
        id	 (array):	Template Id
		prefix	 (string):	Prefix
		includeAll	 (boolean):	Include all flag
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/device/migration?id={id}&prefix={prefix}&includeAll={includeAll}"
        response = self.client.apiCall(HttpMethods.POST, endpoint)
        return response


    def migrationInfo(self):
        """
        Returns the mapping between old and migrated templates
        NOTE: In a multitenant vManage system, this API is only available in the Provider view.
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/device/migration_info"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getMasterTemplateDefinition(self, templateId):
        """
        Generate template by Id
        NOTE: In a multitenant vManage system, this API is only available in the Provider view.
        
        Parameters:
        templateId	 (string):	Template Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/device/object/{templateId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def changeTemplateResourceGroup(self, templateId, resourceGroupName):
        """
        Change template resource group
        
        Parameters:
        templateId	 (string):	Template Id
		resourceGroupName	 (string):	Resource group name
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/device/resource-group/{resourceGroupName}/{templateId}"
        response = self.client.apiCall(HttpMethods.POST, endpoint)
        return response


    def getOutOfSyncTemplates(self):
        """
        Get template sync status
        NOTE: In a multitenant vManage system, this API is only available in the Provider view.
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/device/syncstatus"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getOutOfSyncDevices(self, templateId):
        """
        Get out of sync devices
        NOTE: In a multitenant vManage system, this API is only available in the Provider view.
        
        Parameters:
        templateId	 (string):	Template Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/device/syncstatus/{templateId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def editMasterTemplate(self, template, templateId):
        """
        Edit template
        NOTE: In a multitenant vManage system, this API is only available in the Provider view.
        
        Parameters:
        template:	Template
		templateId	 (string):	Template Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/device/{templateId}"
        response = self.client.apiCall(HttpMethods.PUT, endpoint, template)
        return response


    def deleteMasterTemplate(self, templateId):
        """
        Delete template
        NOTE: In a multitenant vManage system, this API is only available in the Provider view.
        
        Parameters:
        templateId	 (string):	Template Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/device/{templateId}"
        response = self.client.apiCall(HttpMethods.DELETE, endpoint)
        return response


