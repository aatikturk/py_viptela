from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class Inventory(object):
    """
    Configuration - Device Inventory API
    
    Implements GET POST DEL PUT methods for DeviceInventory endpoints

    """

    def __init__(self, session, host, port):
        self.host = host
        self.port = port
        self.client = HttpMethods.HttpClient(session=session)
    
    
    def createDevice(self, createdevicerequest):
        """
        Create new device
        NOTE: In a multitenant vManage system, this API is only available in the Provider view.
        
        Parameters:
        createdevicerequest:	Create device request
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/system/device"
        response = self.client.apiCall(HttpMethods.POST, endpoint, createdevicerequest)
        return response


    def generateBootstrapConfigForVedge(self, uuid, configtype, inclDefRootCert, version):
        """
        Create vEdge device config
        
        Parameters:
        uuid	 (string):	Device uuid
		configtype	 (string):	Device config type
		inclDefRootCert	 (boolean):	Include default root certs flag
		version	 (string):	cloud-init format version
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/system/device/bootstrap/device/{uuid}?configtype={configtype}&inclDefRootCert={inclDefRootCert}&version={version}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def generateBootstrapConfigForVedges(self, devicebootstraptypeandid):
        """
        Create bootstrap config for software vEdges
        
        Parameters:
        devicebootstraptypeandid:	Device bootstrap type and id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/system/device/bootstrap/devices"
        response = self.client.apiCall(HttpMethods.POST, endpoint, devicebootstraptypeandid)
        return response


    def getBootstrapConfigZip(self, id):
        """
        Download vEdge device config
        
        Parameters:
        id	 (string):	Bootstrap config id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/system/device/bootstrap/download/{id}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def generateGenericBootstrapConfigForVedges(self, wanif):
        """
        Create bootstrap config for software vEdges
        
        Parameters:
        wanif	 (string):	Device WAN interface
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/system/device/bootstrap/generic/devices?wanif={wanif}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def claimDevices(self, claimdevicerequest):
        """
        Claim the selected unclaimed devices
        
        Parameters:
        claimdevicerequest:	Claim device request
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/system/device/claimDevices"
        response = self.client.apiCall(HttpMethods.POST, endpoint, claimdevicerequest)
        return response


    def getControllerVEdgeSyncStatus(self):
        """
        Get controllers vEdge sync status
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/system/device/controllers/vedge/status"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def decommissionVedgeCloud(self, uuid):
        """
        Decomission vEdge device
        
        Parameters:
        uuid	 (string):	Device uuid
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/system/device/decommission/{uuid}"
        response = self.client.apiCall(HttpMethods.PUT, endpoint)
        return response


    def devicesWithoutSubjectSudi(self):
        """
        retrieve devices without subject sudi
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/system/device/devicesWithoutSubjectSudi"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def formPost(self):
        """
        Upload file to vEdge
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/system/device/fileupload"
        response = self.client.apiCall(HttpMethods.POST, endpoint)
        return response


    def validateUser(self, bodyParameter):
        """
        Authenticate vSmart user account
        
        Parameters:
        bodyParameter:	Description
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/system/device/generate-payg"
        response = self.client.apiCall(HttpMethods.POST, endpoint, bodyParameter)
        return response


    def setLifeCycle(self, uuid, enable):
        """
        Set device lifecycle needed flag
        
        Parameters:
        uuid	 (string):	Device uuid
		enable	 (boolean):	lifecycle needed flag
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/system/device/lifecycle/management/{uuid}?enable={enable}"
        response = self.client.apiCall(HttpMethods.POST, endpoint)
        return response


    def getManagementSystemIPInfo(self):
        """
        Get management system IP mapping
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/system/device/management/systemip"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def migrateDevice(self, uuid):
        """
        Migrate device software to vedge/cedge
        
        Parameters:
        uuid	 (string):	Device uuid
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/system/device/migrateDevice/{uuid}"
        response = self.client.apiCall(HttpMethods.PUT, endpoint)
        return response


    def resetVedgeCloud(self, uuid):
        """
        Reset vEdge device
        
        Parameters:
        uuid	 (string):	Device uuid
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/system/device/reset/{uuid}"
        response = self.client.apiCall(HttpMethods.PUT, endpoint)
        return response


    def getRMACandidates(self, deviceType, uuid):
        """
        Get RMA candidates by device type
        
        Parameters:
        deviceType	 (string):	Device Type
		uuid	 (string):	Excluded currently selected uuid
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/system/device/rma/candidates/{deviceType}?uuid={uuid}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getRootCertStatusAll(self, state):
        """
        Get controllers vEdge sync status
        
        Parameters:
        state	 (string):	Root certificate state
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/system/device/rootcertchain/status?state={state}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def checkSelfSignedCert(self):
        """
        Whether self signed certificate created
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/system/device/selfsignedcert/iscreated"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def validateUser(self, bodyParameter):
        """
        Authenticate vSmart user account
        
        Parameters:
        bodyParameter:	Description
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/system/device/smartaccount/authenticate"
        response = self.client.apiCall(HttpMethods.POST, endpoint, bodyParameter)
        return response


    def syncDevices(self, bodyParameter):
        """
        Sync devices from Smart-Account
        
        Parameters:
        bodyParameter:	Description
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/system/device/smartaccount/sync"
        response = self.client.apiCall(HttpMethods.POST, endpoint, bodyParameter)
        return response


    def syncRootCertChain(self):
        """
        Sync root certificate
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/system/device/sync/rootcertchain"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getTenantManagementSystemIPs(self):
        """
        Get management system IP
        NOTE: In a multitenant vManage system, this API is only available in the Provider view.
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/system/device/tenant/management/systemip"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getCloudDockDataBasedOnDeviceType(self, deviceCategory):
        """
        Get devices details
        
        Parameters:
        deviceCategory	 (string):	Device category
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/system/device/type/{deviceCategory}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getCloudDockDefaultConfigBasedOnDeviceType(self, deviceCategory):
        """
        Get devices default config
        
        Parameters:
        deviceCategory	 (string):	Device category
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/system/device/type/{deviceCategory}/defaultConfig"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getAllUnclaimedDevices(self):
        """
        Get list of all unclaimed devices
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/system/device/unclaimedDevices"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def invalidateVmanageRootCA(self, uuid):
        """
        Invalidate vManage root CA
        
        Parameters:
        uuid	 (string):	Device uuid
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/system/device/vmanagerootca/{uuid}"
        response = self.client.apiCall(HttpMethods.DELETE, endpoint)
        return response


    def getDevicesDetails(self, deviceCategory, model, state, uuid, deviceIP, validity):
        """
        Get devices details. When {deviceCategory = controllers}, it returns vEdge sync status, vBond, vManage and vSmart.
When {deviceCategory = vedges}, it returns all available vEdge routers
        
        Parameters:
        deviceCategory	 (string):	Device category
		model	 (string):	Device model
		state	 (array):	List of states
		uuid	 (array):	List of device uuid
		deviceIP	 (array):	List of device system IP
		validity	 (array):	List of device validity
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/system/device/{deviceCategory}?model={model}&state={state}&uuid={uuid}&deviceIP={deviceIP}&validity={validity}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def editDevice(self, deviceconfig, uuid):
        """
        Edit device
        
        Parameters:
        deviceconfig:	Device config
		uuid	 (string):	Device uuid
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/system/device/{uuid}"
        response = self.client.apiCall(HttpMethods.PUT, endpoint, deviceconfig)
        return response


    def deleteDevice(self, uuid):
        """
        Delete vEdges
        
        Parameters:
        uuid	 (string):	Device uuid
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/system/device/{uuid}"
        response = self.client.apiCall(HttpMethods.DELETE, endpoint)
        return response


