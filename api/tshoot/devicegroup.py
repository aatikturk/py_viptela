from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class DeviceGroup(object):
    """
    Troubleshooting Tools - Device Group API
    
    Implements GET POST DEL PUT methods for Device Group endpoints

    """

    def __init__(self, session, host, port):
        self.host = host
        self.port = port
        self.client = HttpMethods.HttpClient(session=session)
    
    
    def listDeviceGroupList(self):
        """
        Retrieve device group list
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/group"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def listDeviceGroups(self):
        """
        Retrieve device groups
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/group/device"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def listGroupDevices(self, groupId, ssh, vpnId):
        """
        Retrieve devices in group
        
        Parameters:
        groupId	 (string):	Group Id
		ssh	 (boolean):	SSH
		vpnId	 (array):	VPN Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/group/devices?groupId={groupId}&ssh={ssh}&vpnId={vpnId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def listGroupDevicesForMap(self, groupId, vpnId):
        """
        Retrieve group devices for map
        
        Parameters:
        groupId	 (string):	Group Id
		vpnId	 (array):	VPN Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/group/map/devices?groupId={groupId}&vpnId={vpnId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def listGroupLinksForMap(self, groupId):
        """
        Retrieve devices in group for map
        
        Parameters:
        groupId	 (string):	Group Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/group/map/devices/links?groupId={groupId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


