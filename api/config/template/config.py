from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class Config(object):
    """
    Configuration - Template Configuration API
    
    Implements GET POST DEL PUT methods for TemplateConfiguration endpoints

    """

    def __init__(self, session, host, port):
        self.host = host
        self.port = port
        self.client = HttpMethods.HttpClient(session=session)
    
    
    def uploadConfig(self, templateconfig, deviceId):
        """
        Upload device config
        
        Parameters:
        templateconfig:	Template config
		deviceId	 (string):	Device Model ID
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/config/attach/{deviceId}"
        response = self.client.apiCall(HttpMethods.PUT, endpoint, templateconfig)
        return response


    def getAttached(self, deviceId, type):
        """
        Get local template attached config for given device
        
        Parameters:
        deviceId	 (string):	Device Model ID
		type	 (string):	Config type
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/config/attached/{deviceId}?type={type}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getCLIModeDevices(self, type):
        """
        Generates a JSON object that contains a list of valid devices in CLI mode
        
        Parameters:
        type	 (string):	Device type
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/config/device/mode/cli?type={type}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def updateToCLI(self, devicelist):
        """
        Given a JSON list of devices not managed by any third member partners, push to devices from a CLI template
        
        Parameters:
        devicelist:	Device list
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/config/device/mode/cli"
        response = self.client.apiCall(HttpMethods.POST, endpoint, devicelist)
        return response


    def getvManageModeDevices(self, type):
        """
        Get list of devices that are allowable for vmanage modes
        
        Parameters:
        type	 (string):	Device type
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/config/device/mode/vmanage?type={type}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getDeviceDiff(self, deviceId):
        """
        Generates a JSON object that contains the diff for a given device
        
        Parameters:
        deviceId	 (string):	Device Model ID
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/config/diff/{deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getCompatibleDevices(self, oldDeviceId):
        """
        Get compatible devices of model, chassis number, certificate serial number with the old device
        
        Parameters:
        oldDeviceId	 (string):	Device Model ID
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/config/rmalist/{oldDeviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def rmaUpdate(self, templateconfig):
        """
        Update new device
        
        Parameters:
        templateconfig:	Template config
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/config/rmaupdate"
        response = self.client.apiCall(HttpMethods.PUT, endpoint, templateconfig)
        return response


    def getRunningConfig(self, deviceId):
        """
        Get device running config
        
        Parameters:
        deviceId	 (string):	Device Model ID
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/config/running/{deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getVpnForDevice(self, deviceId):
        """
        Get list of configured VPN (excluding reserved VPN) for a device
        
        Parameters:
        deviceId	 (string):	Device Model ID
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/template/config/vpn/{deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


