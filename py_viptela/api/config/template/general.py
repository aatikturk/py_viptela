from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class General(object):
    """
    Configuration - General Template API
    
    Implements GET POST DEL PUT methods for GeneralTemplate endpoints

    """

    def __init__(self, session, host, port):
        self.host = host
        self.port = port
        self.client = HttpMethods.HttpClient(session=session)
    
    
    def getFeatureTemplateList(self, summary, offset, limit):
        """
        Get feature template list
        NOTE: In a multitenant vManage system, this API is only available in the Provider view.
        
        Parameters:
        summary	 (boolean):	Flag to include template definition
		offset	 (integer):	Pagination offset
		limit	 (integer):	Pagination limit on templateId
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/feature?summary={summary}&offset={offset}&limit={limit}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def createFeatureTemplate(self, featuretemplate):
        """
        Create feature template
        
        Parameters:
        featuretemplate:	Feature template
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/feature"
        response = self.client.apiCall(HttpMethods.POST, endpoint, featuretemplate)
        return response


    def cloneTemplate(self, id, name, desc):
        """
        Clone a feature template
        NOTE: In a multitenant vManage system, this API is only available in the Provider view.
        
        Parameters:
        id	 (string):	Template Id to clone from
		name	 (string):	Name for the cloned template
		desc	 (string):	Description for the cloned template
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/feature/clone?id={id}&name={name}&desc={desc}"
        response = self.client.apiCall(HttpMethods.POST, endpoint)
        return response


    def getNetworkInterface(self, deviceModel):
        """
        Get default network interface
        NOTE: In a multitenant vManage system, this API is only available in the Provider view.
        
        Parameters:
        deviceModel	 (string):	Device model
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/feature/default/networkinterface?deviceModel={deviceModel}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getDefaultNetworks(self, deviceModel):
        """
        Get default networks
        NOTE: In a multitenant vManage system, this API is only available in the Provider view.
        
        Parameters:
        deviceModel	 (string):	Device model
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/feature/default/networks?deviceModel={deviceModel}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getTemplateDefinition(self, templateId):
        """
        Get the configured template definition for given template Id
        NOTE: In a multitenant vManage system, this API is only available in the Provider view.
        
        Parameters:
        templateId	 (string):	Template Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/feature/definition/{templateId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getDeviceTemplatesAttachedToFeature(self, templateId):
        """
        Get all device templates for this feature template
        NOTE: In a multitenant vManage system, this API is only available in the Provider view.
        
        Parameters:
        templateId	 (string):	Feature template Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/feature/devicetemplates/{templateId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def listLITemplate(self):
        """
        Get LI feature template
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/feature/li"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def createLITemplate(self, litemplate):
        """
        Create LI feature template
        NOTE: In a multitenant vManage system, this API is only available in the Provider view.
        
        Parameters:
        litemplate:	LI template
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/feature/li"
        response = self.client.apiCall(HttpMethods.POST, endpoint, litemplate)
        return response


    def editLITemplate(self, litemplate, templateId):
        """
        Update LI feature template
        NOTE: In a multitenant vManage system, this API is only available in the Provider view.
        
        Parameters:
        litemplate:	LI template
		templateId	 (string):	Template Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/feature/li/{templateId}"
        response = self.client.apiCall(HttpMethods.PUT, endpoint, litemplate)
        return response


    def getMasterTemplateDefinition(self, type_name):
        """
        Generate template type definition by device type
        NOTE: In a multitenant vManage system, this API is only available in the Provider view.
        
        Parameters:
        type_name	 (string):	Device type
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/feature/master/{type_name}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getTemplateForMigration(self):
        """
        Generate a list of templates which require migration
        NOTE: In a multitenant vManage system, this API is only available in the Provider view.
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/feature/migration"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getGeneralTemplate(self, templateId):
        """
        Get template object definition for given template Id
        NOTE: In a multitenant vManage system, this API is only available in the Provider view.
        
        Parameters:
        templateId	 (string):	Template Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/feature/object/{templateId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def changeTemplateResourceGroup(self, templateId, resourceGroupName):
        """
        Change template resource group
        
        Parameters:
        templateId	 (string):	Template Id
		resourceGroupName	 (string):	Resrouce group name
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/feature/resource-group/{resourceGroupName}/{templateId}"
        response = self.client.apiCall(HttpMethods.POST, endpoint)
        return response


    def getTemplateTypes(self, type):
        """
        Generate template types
        NOTE: In a multitenant vManage system, this API is only available in the Provider view.
        
        Parameters:
        type	 (string):	Device type
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/feature/types?type={type}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getTemplateTypeDefinition(self, type_name, version):
        """
        Generate template type definition
        NOTE: In a multitenant vManage system, this API is only available in the Provider view.
        
        Parameters:
        type_name	 (string):	Device type
		version	 (string):	Version
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/feature/types/definition/{type_name}/{version}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getTemplateByDeviceType(self, deviceType):
        """
        Generate template based on device
        NOTE: In a multitenant vManage system, this API is only available in the Provider view.
        
        Parameters:
        deviceType	 (string):	Device type
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/feature/{deviceType}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def editFeatureTemplate(self, template, templateId):
        """
        Update feature template
        NOTE: In a multitenant vManage system, this API is only available in the Provider view.
        
        Parameters:
        template:	Template
		templateId	 (string):	Template Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/feature/{templateId}"
        response = self.client.apiCall(HttpMethods.PUT, endpoint, template)
        return response


    def deleteGeneralTemplate(self, templateId):
        """
        Delete feature template
        
        Parameters:
        templateId	 (string):	Template Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/feature/{templateId}"
        response = self.client.apiCall(HttpMethods.DELETE, endpoint)
        return response


    def getEncryptedString(self, type6encryption):
        """
        Get Type 6 Encryptedd String for a given value
        
        Parameters:
        type6encryption:	Type6 Encryption
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/security/encryptText/encrypt"
        response = self.client.apiCall(HttpMethods.POST, endpoint, type6encryption)
        return response


