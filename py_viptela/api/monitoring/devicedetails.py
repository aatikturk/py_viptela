from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class Device(object):
    """
    Monitoring - Device Details API
    
    Implements GET POST DEL PUT methods for DeviceDetails endpoints

    """

    def __init__(vmanage, session, host, port):
        vmanage.client = HttpMethods.HttpClient(session=session)
        vmanage.host = host
        vmanage.port = port
    
    
    def getStateData(vmanage, state_data_type, startId, count):
        """
        Get device state data
        
        Parameters:
        state_data_type	 (string):	State data type
		startId	 (string):	Start Id
		count	 (string):	Count
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/data/device/state/{state_data_type}?startId={startId}&count={count}"
        response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getStateDataFields(vmanage, state_data_type):
        """
        Get device state data fileds
        
        Parameters:
        state_data_type	 (string):	State data type
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/data/device/state/{state_data_type}/fields"
        response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getStateDataWithQuery(vmanage, state_data_type):
        """
        Get device state data fileds
        
        Parameters:
        state_data_type	 (string):	State data type
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/data/device/state/{state_data_type}/query"
        response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def listAllDevices(vmanage):
        """
        List all devices
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device"
        response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def setBlockSync(vmanage, blockSync):
        """
        Set collection manager block set flag
        
        Parameters:
        blockSync	 (string):	Block sync flag
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/blockSync?blockSync={blockSync}"
        response = vmanage.client.apiCall(HttpMethods.POST, endpoint)
        return response


    def getRunning(vmanage, deviceId):
        """
        Get device running configuration
        
        Parameters:
        deviceId	 (array):	Device Id list
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/config?deviceId={deviceId}"
        response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getRunningHtml(vmanage, deviceId):
        """
        Get device running configuration in HTML format
        
        Parameters:
        deviceId	 (array):	Device Id list
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/config/html?deviceId={deviceId}"
        response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getDeviceCounters(vmanage):
        """
        Get device counters
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/counters"
        response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getDeviceOnlyStatus(vmanage):
        """
        Get devices status per type
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/devicestatus"
        response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def enableSDAVCOnDevice(vmanage, deviceIP, enable):
        """
        Enable/Disable SDAVC on device
        
        Parameters:
        deviceIP	 (string):	Device IP
		enable	 (boolean):	Enable/Disable flag
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/enableSDAVC/{deviceIP}/{enable}"
        response = vmanage.client.apiCall(HttpMethods.POST, endpoint)
        return response


    def getHealthDetails(vmanage, deviceId, state):
        """
        Get hardware health details for device
        
        Parameters:
        deviceId	 (string):	Device Id
		state	 (string):	Device state
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/hardwarehealth/detail?deviceId={deviceId}&state={state}"
        response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getHealthSummary(vmanage, isCached, vpnId):
        """
        Get hardware health summary for device
        
        Parameters:
        isCached	 (boolean):	Status cached
		vpnId	 (array):	VPN Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/hardwarehealth/summary?isCached={isCached}&vpnId={vpnId}"
        response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getListAsKeyValue(vmanage):
        """
        Get vEdge inventory as key value (key as systemIp value as hostName)
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/keyvalue"
        response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def listAllModels(vmanage, list):
        """
        Get all device models supported by the vManage
        
        Parameters:
        list	 (string):	List type of device
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/models?list={list}"
        response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getDeviceModels(vmanage, uuid):
        """
        Get device model for the device
        
        Parameters:
        uuid	 (string):	Device uuid
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/models/{uuid}"
        response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def listAllMonitorDetails(vmanage):
        """
        Get all monitoring details of the devices
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/monitor"
        response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getSyncQueues(vmanage):
        """
        Get synchronized queue information, returns information about syncing, queued and stuck devices
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/queues"
        response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def listReachable(vmanage):
        """
        Get list of reachable devices
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/reachable"
        response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getStatsQueues(vmanage):
        """
        Get stats queue information
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/stats"
        response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getAllStatus(vmanage):
        """
        Get devices status for vSmart,vBond,vEdge, and cEdge
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/status"
        response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def listSyncing(vmanage, groupId):
        """
        Get list of currently syncing devices
        
        Parameters:
        groupId	 (string):	Group Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/sync_status?groupId={groupId}"
        response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def syncAllMemDB(vmanage):
        """
        Synchronize memory database for all devices
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/syncall/memorydb"
        response = vmanage.client.apiCall(HttpMethods.POST, endpoint)
        return response


    def getDeviceTlocStatus(vmanage, deviceId, color):
        """
        Get TLOC status list
        
        Parameters:
        deviceId	 (string):	Device Id
		color	 (string):	Status color
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/tloc?deviceId={deviceId}&color={color}"
        response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getTlocUtil(vmanage):
        """
        Get TLOC list
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/tlocutil"
        response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getTlocUtilDetails(vmanage, util):
        """
        Get detailed TLOC list
        
        Parameters:
        util	 (string):	Tloc util
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/tlocutil/detail?util={util}"
        response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def listUnreachable(vmanage, personality):
        """
        Get list of unreachable devices
        
        Parameters:
        personality	 (string):	Device personality
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/unreachable?personality={personality}"
        response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def removeUnreachable(vmanage, deviceIP):
        """
        Delete unreachable device
        
        Parameters:
        deviceIP	 (string):	Device IP
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/unreachable/{deviceIP}"
        response = vmanage.client.apiCall(HttpMethods.DELETE, endpoint)
        return response


    def getVedgeInventory(vmanage, status):
        """
        Get detailed vEdge inventory
        
        Parameters:
        status	 (string):	Device status
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/vedgeinventory/detail?status={status}"
        response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getVedgeInventorySummary(vmanage):
        """
        Get vEdge inventory
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/vedgeinventory/summary"
        response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getVManageSystemIP(vmanage):
        """
        Get vManage system IP
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/vmanage"
        response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
        return response


