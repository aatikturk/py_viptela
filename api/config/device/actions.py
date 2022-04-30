from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class DeviceActions(object):
    """
    Configuration - Device Actions API
    
    Implements GET POST DEL PUT methods for DeviceActions endpoints

    """

    def __init__(self, session, host, port):
        self.host = host
        self.port = port
        self.client = HttpMethods.HttpClient(session=session)
    
    
    def generateChangePartitionInfo(self, deviceId):
        """
        Get change partition information
        
        Parameters:
        deviceId	 (array):	Device Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/action/changepartition?deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def processChangePartition(self, payload):
        """
        Process change partition operation
        
        Parameters:
        payload:	Device change partition request payload
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/action/changepartition"
        response = self.client.apiCall(HttpMethods.POST, endpoint, payload)
        return response


    def generateDeactivateInfo(self, deviceId):
        """
        Get deactivate partition information
        
        Parameters:
        deviceId	 (array):	Device Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/action/deactivate?deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def processDeactivateSmu(self, request):
        """
        Process deactivate operation for smu image
        
        Parameters:
        request:	Device smu image deactivate request
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/action/deactivate"
        response = self.client.apiCall(HttpMethods.POST, endpoint, request)
        return response


    def processDefaultPartition(self, request):
        """
        Process marking default partition operation
        
        Parameters:
        request:	Marking default partition request
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/action/defaultpartition"
        response = self.client.apiCall(HttpMethods.POST, endpoint, request)
        return response


    def createFilterVPNList(self):
        """
        Get filter VPN list
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/action/filter/vpn"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def generateInstallInfo(self, deviceId):
        """
        Generate install info
        
        Parameters:
        deviceId	 (array):	Device Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/action/install?deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def processInstall(self, payload):
        """
        Process an installation operation
        
        Parameters:
        payload:	Installation payload
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/action/install"
        response = self.client.apiCall(HttpMethods.POST, endpoint, payload)
        return response


    def generateDeviceList(self, deviceType, groupId):
        """
        Get list of installed devices
        
        Parameters:
        Parameter Description
		Parameter Description
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/action/install/devices/{deviceType}?groupId={groupId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def generateDeviceActionList(self):
        """
        Get device action list
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/action/list"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def processLxcActivate(self, payload):
        """
        Process an activation operation
        
        Parameters:
        payload:	Activation request payload
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/action/lxcactivate"
        response = self.client.apiCall(HttpMethods.POST, endpoint, payload)
        return response


    def processLxcDelete(self, payload):
        """
        Process a delete operation
        
        Parameters:
        payload:	Delete request payload
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/action/lxcdelete"
        response = self.client.apiCall(HttpMethods.POST, endpoint, payload)
        return response


    def processLxcInstall(self, payload):
        """
        Process an installation operation
        
        Parameters:
        payload:	Installation request payload
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/action/lxcinstall"
        response = self.client.apiCall(HttpMethods.POST, endpoint, payload)
        return response


    def processLxcReload(self, payload):
        """
        Process a reload operation
        
        Parameters:
        payload:	Reload request payload
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/action/lxcreload"
        response = self.client.apiCall(HttpMethods.POST, endpoint, payload)
        return response


    def processLxcReset(self, payload):
        """
        Process a reset operation
        
        Parameters:
        payload:	Reset request payload
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/action/lxcreset"
        response = self.client.apiCall(HttpMethods.POST, endpoint, payload)
        return response


    def processLxcUpgrade(self, payload):
        """
        Process an upgrade operation
        
        Parameters:
        payload:	Upgrade request payload
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/action/lxcupgrade"
        response = self.client.apiCall(HttpMethods.POST, endpoint, payload)
        return response


    def generateRebootInfo(self, deviceId):
        """
        Get device reboot information
        
        Parameters:
        deviceId	 (array):	Device Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/action/reboot?deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def processReboot(self, payload):
        """
        Process a reboot operation
        
        Parameters:
        payload:	Device reboot request payload
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/action/reboot"
        response = self.client.apiCall(HttpMethods.POST, endpoint, payload)
        return response


    def generateRebootDeviceList(self, deviceType, deviceId):
        """
        Get list of rebooted devices
        
        Parameters:
        Parameter Description
		Parameter Description
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/action/reboot/devices/{deviceType}?deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def generateRediscoverInfo(self):
        """
        Get rediscover operation information
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/action/rediscover"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def reDiscoverDevices(self, payload):
        """
        Rediscover device
        
        Parameters:
        payload:	Rediscover device request payload
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/action/rediscover"
        response = self.client.apiCall(HttpMethods.POST, endpoint, payload)
        return response


    def reDiscoverAllDevice(self, payload):
        """
        Rediscover all devices
        
        Parameters:
        payload:	Rediscover device request payload
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/action/rediscoverall"
        response = self.client.apiCall(HttpMethods.POST, endpoint, payload)
        return response


    def generateRemovePartitionInfo(self, deviceId):
        """
        Get remove partition information
        
        Parameters:
        deviceId	 (string):	Device Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/action/removepartition?deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def processRemovePartition(self, payload):
        """
        Process remove partition operation
        
        Parameters:
        payload:	Device remove partition request payload
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/action/removepartition"
        response = self.client.apiCall(HttpMethods.POST, endpoint, payload)
        return response


    def processDeleteAmpApiKey(self, uuid):
        """
        Process amp api key deletion operation
        
        Parameters:
        uuid	 (string):	Uuid
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/action/security/amp/apikey/{uuid}"
        response = self.client.apiCall(HttpMethods.DELETE, endpoint)
        return response


    def processAmpApiReKey(self, payload):
        """
        Process amp api re-key operation
        
        Parameters:
        ampapire-keyrequestpayload:	AMP API re-key request payload
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/action/security/amp/rekey"
        response = self.client.apiCall(HttpMethods.POST, endpoint, payload)
        return response


    def testApiKey(self, uuid):
        """
        Get API key from device
        
        Parameters:
        uuid	 (string):	Device uuid
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/action/security/apikey/{uuid}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def generateSecurityDevicesList(self, policyType, groupId):
        """
        Get list of devices by security policy type
        
        Parameters:
        policyType	 (string):	Policy type
		Parameter Description
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/action/security/devices/{policyType}?groupId={groupId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def triggerPendingTasksMonitoring(self):
        """
        Triggers global monitoring thread
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/action/startmonitor"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def testIoxConfig(self, deviceIP):
        """
        testIoxConfig
        
        Parameters:
        Parameter Description
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/action/test/ioxconfig/{deviceIP}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def createUniqueVPNList(self, deviceips):
        """
        Create unique VPN list
        
        Parameters:
        deviceips:	Device IPs
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/action/uniquevpnlist"
        response = self.client.apiCall(HttpMethods.POST, endpoint, deviceips)
        return response


    def processVnfInstall(self, payload):
        """
        Process an installation operation
        
        Parameters:
        payload:	Installation request payload
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/action/vnfinstall"
        response = self.client.apiCall(HttpMethods.POST, endpoint, payload)
        return response


    def createVPNList(self):
        """
        Create VPN list
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/action/vpn"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getZTPUpgradeConfig(self):
        """
        Get ZTP upgrade configuration
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/action/ztp/upgrade"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def processZTPUpgradeConfig(self, ztpConfig):
        """
        Process ZTP upgrade configuration
        
        Parameters:
        ztpConfig:	ZTP upgrade config
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/action/ztp/upgrade"
        response = self.client.apiCall(HttpMethods.POST, endpoint, ztpConfig)
        return response


    def getZTPUpgradeConfigSetting(self):
        """
        Get ZTP upgrade configuration setting
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/action/ztp/upgrade/setting"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def processZTPUpgradeConfigSetting(self, ztpSetting):
        """
        Process ZTP upgrade configuration setting
        
        Parameters:
        ztpSetting:	ZTP upgrade setting
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/action/ztp/upgrade/setting"
        response = self.client.apiCall(HttpMethods.POST, endpoint, ztpSetting)
        return response


