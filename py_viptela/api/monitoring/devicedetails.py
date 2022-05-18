from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class Device(object):
    """
    Monitoring - Device Details API
    
    Implements GET POST DEL PUT methods for DeviceDetails endpoints

    """

    def __init__(self, session, host, port):
        self.client = HttpMethods.HttpClient(session=session)
        self.host = host
        self.port = port
    
    
    def getStateData(self, state_data_type, startId, count):
        """
        Get device state data
        
        Parameters:
        state_data_type	 (string):	State data type
		startId	 (string):	Start Id
		count	 (string):	Count
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/data/device/state/{state_data_type}?startId={startId}&count={count}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getStateDataFields(self, state_data_type):
        """
        Get device state data fileds
        
        Parameters:
        state_data_type	 (string):	State data type
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/data/device/state/{state_data_type}/fields"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getStateDataWithQuery(self, state_data_type):
        """
        Get device state data fileds
        
        Parameters:
        state_data_type	 (string):	State data type
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/data/device/state/{state_data_type}/query"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def listAllDevices(self):
        """
        List all devices
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def setBlockSync(self, blockSync):
        """
        Set collection manager block set flag
        
        Parameters:
        blockSync	 (string):	Block sync flag
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/blockSync?blockSync={blockSync}"
        response = self.client.apiCall(HttpMethods.POST, endpoint)
        return response


    def getRunning(self, deviceId):
        """
        Get device running configuration
        
        Parameters:
        deviceId	 (array):	Device Id list
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/config?deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getRunningHtml(self, deviceId):
        """
        Get device running configuration in HTML format
        
        Parameters:
        deviceId	 (array):	Device Id list
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/config/html?deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getDeviceCounters(self):
        """
        Get device counters
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/counters"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getDeviceOnlyStatus(self):
        """
        Get devices status per type
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/devicestatus"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def enableSDAVCOnDevice(self, deviceIP, enable):
        """
        Enable/Disable SDAVC on device
        
        Parameters:
        deviceIP	 (string):	Device IP
		enable	 (boolean):	Enable/Disable flag
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/enableSDAVC/{deviceIP}/{enable}"
        response = self.client.apiCall(HttpMethods.POST, endpoint)
        return response


    def getHealthDetails(self, deviceId, state):
        """
        Get hardware health details for device
        
        Parameters:
        deviceId	 (string):	Device Id
		state	 (string):	Device state
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/hardwarehealth/detail?deviceId={deviceId}&state={state}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getHealthSummary(self, isCached, vpnId):
        """
        Get hardware health summary for device
        
        Parameters:
        isCached	 (boolean):	Status cached
		vpnId	 (array):	VPN Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/hardwarehealth/summary?isCached={isCached}&vpnId={vpnId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getListAsKeyValue(self):
        """
        Get vEdge inventory as key value (key as systemIp value as hostName)
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/keyvalue"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def listAllModels(self, list):
        """
        Get all device models supported by the vManage
        
        Parameters:
        list	 (string):	List type of device
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/models?list={list}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getDeviceModels(self, uuid):
        """
        Get device model for the device
        
        Parameters:
        uuid	 (string):	Device uuid
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/models/{uuid}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def listAllMonitorDetails(self):
        """
        Get all monitoring details of the devices
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/monitor"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getSyncQueues(self):
        """
        Get synchronized queue information, returns information about syncing, queued and stuck devices
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/queues"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def listReachable(self):
        """
        Get list of reachable devices
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/reachable"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getStatsQueues(self):
        """
        Get stats queue information
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/stats"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getAllStatus(self):
        """
        Get devices status for vSmart,vBond,vEdge, and cEdge
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/status"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def listSyncing(self, groupId):
        """
        Get list of currently syncing devices
        
        Parameters:
        groupId	 (string):	Group Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/sync_status?groupId={groupId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def syncAllMemDB(self):
        """
        Synchronize memory database for all devices
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/syncall/memorydb"
        response = self.client.apiCall(HttpMethods.POST, endpoint)
        return response


    def getDeviceTlocStatus(self, deviceId, color):
        """
        Get TLOC status list
        
        Parameters:
        deviceId	 (string):	Device Id
		color	 (string):	Status color
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/tloc?deviceId={deviceId}&color={color}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getTlocUtil(self):
        """
        Get TLOC list
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/tlocutil"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getTlocUtilDetails(self, util):
        """
        Get detailed TLOC list
        
        Parameters:
        util	 (string):	Tloc util
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/tlocutil/detail?util={util}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def listUnreachable(self, personality):
        """
        Get list of unreachable devices
        
        Parameters:
        personality	 (string):	Device personality
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/unreachable?personality={personality}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def removeUnreachable(self, deviceIP):
        """
        Delete unreachable device
        
        Parameters:
        deviceIP	 (string):	Device IP
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/unreachable/{deviceIP}"
        response = self.client.apiCall(HttpMethods.DELETE, endpoint)
        return response


    def getVedgeInventory(self, status):
        """
        Get detailed vEdge inventory
        
        Parameters:
        status	 (string):	Device status
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/vedgeinventory/detail?status={status}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getVedgeInventorySummary(self):
        """
        Get vEdge inventory
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/vedgeinventory/summary"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getVManageSystemIP(self):
        """
        Get vManage system IP
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/vmanage"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


