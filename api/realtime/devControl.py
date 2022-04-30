from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class Control(object):
    """
    Real-Time Monitoring - Device Control API
    
    Implements GET POST DEL PUT methods for DeviceControl endpoints

    """

    def __init__(self, session, host, port):
        self.host = host
        self.port = port
        self.client = HttpMethods.HttpClient(session=session)
    
    
    def getAffinityConfig(self, deviceId):
        """
        Get affinity config from device (Real Time)
        
        Parameters:
        deviceId	 (string):	Device IP
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/control/affinity/config?deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getAffinityStatus(self, deviceId):
        """
        Get affinity status from device (Real Time)
        
        Parameters:
        deviceId	 (string):	Device IP
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/control/affinity/status?deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def createRealTimeConnectionList(self, peerType, sysIp, deviceId):
        """
        Get connections list from device (Real Time)
        
        Parameters:
        peerType	    (string):	Peer type
		sysIp	        (string):	Peer system IP
		deviceId	    (string):	Device IP
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/control/connections?peerType={peerType}&sysIp={sysIp}&deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def createConnectionHistoryListRealTime(self, peerType, sysIp, deviceId):
        """
        Get connections history list from device (Real Time)
        
        Parameters:
        peerType	 (string):	Peer type
		sysIp	 (string):	Peer system IP
		deviceId	 (string):	Device IP
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/control/connectionshistory?peerType={peerType}&sysIp={sysIp}&deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getTotalCountForDeviceStates(self, isCached):
        """
        Get number of vedges and vsmart device in different control states
        
        Parameters:
        isCached	 (boolean):	Device State cached
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/control/count?isCached={isCached}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def createLinkList(self, state):
        """
        Get connections list
        
        Parameters:
        state	 (string):	Device State
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/control/links?state={state}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def createLocalPropertiesListListRealTIme(self, deviceId):
        """
        Get local properties list (Real Time)
        
        Parameters:
        deviceId	 (string):	Device IP
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/control/localproperties?deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def networkSummary(self, state):
        """
        Get list of unreachable devices
        
        Parameters:
        state	 (string):	Device State
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/control/networksummary?state={state}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getConnectionStatistics(self, deviceId):
        """
        Get connection statistics from device (Real Time)
        
        Parameters:
        deviceId	 (string):	Device IP
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/control/statistics?deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getLocalDeviceStatus(self):
        """
        Get local device status
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/control/status"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def createConnectionsSummary(self, deviceId):
        """
        Get connections summary from device (Real Time)
        
        Parameters:
        deviceId	 (string):	Device IP
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/control/summary?deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getDeviceControlStatusSummary(self, deviceId):
        """
        Get device control status summary
        
        Parameters:
        deviceId	 (string):	Device Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/control/summary/device?deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def createSyncedConnectionList(self, peerType, sysIp, deviceId):
        """
        Get connections list from vManage
        
        Parameters:
        peerType	 (string):	Peer type
		sysIp	 (string):	Peer system IP
		deviceId	 (string):	Device IP
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/control/synced/connections?peerType={peerType}&sysIp={sysIp}&deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def createLocalPropertiesSyncedList(self, deviceId):
        """
        Get local properties list
        
        Parameters:
        deviceId	 (string):	Device Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/control/synced/localproperties?deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def createWanInterfaceSyncedList(self, deviceId):
        """
        Get WAN interface list
        
        Parameters:
        deviceId	 (string):	Device Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/control/synced/waninterface?deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def createValidDevicesListRealTime(self, deviceId):
        """
        Get valid device list (Real Time)
        
        Parameters:
        deviceId	 (string):	Device Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/control/validdevices?deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getValidVManageIdRealTime(self, deviceId):
        """
        Get valid vManage from device (Real Time)
        
        Parameters:
        deviceId	 (string):	Device Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/control/validvmanageid?deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def createValidVSmartsListRealTime(self, deviceId):
        """
        Get valid vSmart list from device (Real Time)
        
        Parameters:
        deviceId	 (string):	Device IP
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/control/validvsmarts?deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def createWanInterfaceListList(self, deviceId):
        """
        Get WAN interface list (Real Time)
        
        Parameters:
        deviceId	 (string):	Device IP
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/control/waninterface?deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getPortHopColor(self, deviceId):
        """
        Get port hop colors
        
        Parameters:
        deviceId	 (string):	Device IP
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/control/waninterface/color?deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


