from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class Device(object):
    """
    Configuration - Device Template API
    
    Implements GET POST DEL PUT methods for DeviceTemplate endpoints

    """

    def __init__(self, session, host, port):
        self.host = host
        self.port = port
        self.client = HttpMethods.HttpClient(session=session)
    
    
    def pushMasterBootstrap(self, bootstrapTemplate):
        """
        Attach bootstrap template to device
        NOTE: In a multitenant vManage system, this API is only available in the Provider view.
        
        Parameters:
        bootstrapTemplate:	Device template
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/device/config/attachBootStrap"
        response = self.client.apiCall(HttpMethods.POST, endpoint, bootstrapTemplate)
        return response


    def pushCLITemplate(self, devicetemplate):
        """
        Attach CLI device template
        NOTE: In a multitenant vManage system, this API is only available in the Provider view.
        
        Parameters:
        devicetemplate:	Device template
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/device/config/attachcli"
        response = self.client.apiCall(HttpMethods.POST, endpoint, devicetemplate)
        return response


    def editCloudxConfig(self, cloudxconfig):
        """
        Edit already enabled gateways, clients, dias
        NOTE: In a multitenant vManage system, this API is only available in the Provider view.
        
        Parameters:
        cloudxconfig:	CloudX config
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/device/config/attachcloudx"
        response = self.client.apiCall(HttpMethods.PUT, endpoint, cloudxconfig)
        return response


    def pushCloudxConfig(self, cloudxconfig):
        """
        Enable gateways, clients, dias
        
        Parameters:
        cloudxconfig:	CloudX config
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/device/config/attachcloudx"
        response = self.client.apiCall(HttpMethods.POST, endpoint, cloudxconfig)
        return response


    def getAttachedDeviceList(self, masterTemplateId):
        """
        Get attached device list by master template Id
        NOTE: In a multitenant vManage system, this API is only available in the Provider view.
        
        Parameters:
        masterTemplateId	 (string):	Template Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/device/config/attached/{masterTemplateId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getAttachedConfigToDevice(self, deviceId):
        """
        Get attached config to device
        NOTE: In a multitenant vManage system, this API is only available in the Provider view.
        
        Parameters:
        deviceId	 (string):	Device Model ID
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/device/config/attachedconfig?deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def pushMasterTemplate(self, devicetemplate):
        """
        Attach feature device template
        NOTE: In a multitenant vManage system, this API is only available in the Provider view.
        
        Parameters:
        devicetemplate:	Device template
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/device/config/attachfeature"
        response = self.client.apiCall(HttpMethods.POST, endpoint, devicetemplate)
        return response


    def attachDeviceTemplate(self, devicetemplate):
        """
        Attach device template
        NOTE: In a multitenant vManage system, this API is only available in the Provider view.
        
        Parameters:
        devicetemplate:	Device template
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/device/config/attachment"
        response = self.client.apiCall(HttpMethods.POST, endpoint, devicetemplate)
        return response


    def getDeviceListByMasterTemplateId(self, masterTemplateId):
        """
        Get possible device list by master template Id
        NOTE: In a multitenant vManage system, this API is only available in the Provider view.
        
        Parameters:
        masterTemplateId	 (string):	Template Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/device/config/available/{masterTemplateId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getDeviceConfigurationPreview(self, devicetemplate):
        """
        Get device configuration
        NOTE: In a multitenant vManage system, this API is only available in the Provider view.
        
        Parameters:
        devicetemplate:	Device template
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/device/config/config"
        response = self.client.apiCall(HttpMethods.POST, endpoint, devicetemplate)
        return response


    def detachDeviceTemplate(self, devicetemplate):
        """
        Detach device template
        NOTE: In a multitenant vManage system, this API is only available in the Provider view.
        
        Parameters:
        devicetemplate:	Device template
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/device/config/detach"
        response = self.client.apiCall(HttpMethods.POST, endpoint, devicetemplate)
        return response


    def detachSites(self, cloudxconfig):
        """
        Disable enabled gateways, clients, dias
        NOTE: In a multitenant vManage system, this API is only available in the Provider view.
        
        Parameters:
        cloudxconfig:	CloudX config
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/device/config/detachcloudx"
        response = self.client.apiCall(HttpMethods.POST, endpoint, cloudxconfig)
        return response


    def getDevicesWithDuplicateIP(self, devicelist):
        """
        Detects duplicate system IP from a list of devices
        NOTE: In a multitenant vManage system, this API is only available in the Provider view.
        
        Parameters:
        devicelist:	Device list
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/device/config/duplicateip"
        response = self.client.apiCall(HttpMethods.POST, endpoint, devicelist)
        return response


    def createInputWithoutDevice(self, devicetemplate):
        """
        Export the device template to CSV format for given template id
        NOTE: In a multitenant vManage system, this API is only available in the Provider view.
        
        Parameters:
        devicetemplate:	Device template
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/device/config/exportcsv"
        response = self.client.apiCall(HttpMethods.POST, endpoint, devicetemplate)
        return response


    def createDeviceInput(self, templatedeviceinput):
        """
        Create device input
        NOTE: In a multitenant vManage system, this API is only available in the Provider view.
        
        Parameters:
        templatedeviceinput:	Template device input
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/device/config/input"
        response = self.client.apiCall(HttpMethods.POST, endpoint, templatedeviceinput)
        return response


    def processInputCommaSepFile(self, devicetemplate):
        """
        Process input comma separated file
        NOTE: In a multitenant vManage system, this API is only available in the Provider view.
        
        Parameters:
        devicetemplate:	Device template
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/device/config/process/input/file"
        response = self.client.apiCall(HttpMethods.POST, endpoint, devicetemplate)
        return response


    def getQuickConnectVariables(self, devicelist):
        """
        Get connection variables to be configured
        
        Parameters:
        devicelist:	Device List
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/device/config/quickconnectvariable"
        response = self.client.apiCall(HttpMethods.POST, endpoint, devicelist)
        return response


    def checkVbond(self):
        """
        Check if vBond is configured
        NOTE: In a multitenant vManage system, this API is only available in the Provider view.
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/device/config/vbond"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def validateTemplate(self, payload):
        """
        Validate full template"

        NOTE: In a multitenant vManage system, this API is only available in the Provider view.
        
        Parameters:
        payload:	Description
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/device/config/verify"
        response = self.client.apiCall(HttpMethods.POST, endpoint, payload)
        return response


