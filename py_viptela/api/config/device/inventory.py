def createDevice(vmanage, createdevicerequest):
    """
    Create new device
    NOTE: In a multitenant vManage system, this API is only available in the Provider view.
    
    Parameters:
    createdevicerequest:	Create device request
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/system/device"
    response = vmanage.apiCall("POST", endpoint, createdevicerequest)
    return response

def generateBootstrapConfigForVedge(vmanage, uuid, configtype, inclDefRootCert, version):
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
    
    endpoint = f"dataservice/system/device/bootstrap/device/{uuid}?configtype={configtype}&inclDefRootCert={inclDefRootCert}&version={version}"
    response = vmanage.apiCall("GET", endpoint)
    return response

def generateBootstrapConfigForVedges(vmanage, devicebootstraptypeandid):
    """
    Create bootstrap config for software vEdges
    
    Parameters:
    devicebootstraptypeandid:	Device bootstrap type and id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/system/device/bootstrap/devices"
    response = vmanage.apiCall("POST", endpoint, devicebootstraptypeandid)
    return response

def getBootstrapConfigZip(vmanage, id):
    """
    Download vEdge device config
    
    Parameters:
    id	 (string):	Bootstrap config id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/system/device/bootstrap/download/{id}"
    response = vmanage.apiCall("GET", endpoint)
    return response

def generateGenericBootstrapConfigForVedges(vmanage, wanif):
    """
    Create bootstrap config for software vEdges
    
    Parameters:
    wanif	 (string):	Device WAN interface
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/system/device/bootstrap/generic/devices?wanif={wanif}"
    response = vmanage.apiCall("GET", endpoint)
    return response

def claimDevices(vmanage, claimdevicerequest):
    """
    Claim the selected unclaimed devices
    
    Parameters:
    claimdevicerequest:	Claim device request
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/system/device/claimDevices"
    response = vmanage.apiCall("POST", endpoint, claimdevicerequest)
    return response

def getControllerVEdgeSyncStatus(vmanage):
    """
    Get controllers vEdge sync status
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/system/device/controllers/vedge/status"
    response = vmanage.apiCall("GET", endpoint)
    return response

def decommissionVedgeCloud(vmanage, uuid):
    """
    Decomission vEdge device
    
    Parameters:
    uuid	 (string):	Device uuid
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/system/device/decommission/{uuid}"
    response = vmanage.apiCall("PUT", endpoint)
    return response

def devicesWithoutSubjectSudi(vmanage):
    """
    retrieve devices without subject sudi
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/system/device/devicesWithoutSubjectSudi"
    response = vmanage.apiCall("GET", endpoint)
    return response

def formPost(vmanage):
    """
    Upload file to vEdge
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/system/device/fileupload"
    response = vmanage.apiCall("POST", endpoint)
    return response

def generatePAYG(vmanage, bodyParameter):
    """
    Authenticate vSmart user account
    
    Parameters:
    bodyParameter:	Description
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/system/device/generate-payg"
    response = vmanage.apiCall("POST", endpoint, bodyParameter)
    return response

def setLifeCycle(vmanage, uuid, enable):
    """
    Set device lifecycle needed flag
    
    Parameters:
    uuid	 (string):	Device uuid
	enable	 (boolean):	lifecycle needed flag
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/system/device/lifecycle/management/{uuid}?enable={enable}"
    response = vmanage.apiCall("POST", endpoint)
    return response

def getManagementSystemIPInfo(vmanage):
    """
    Get management system IP mapping
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/system/device/management/systemip"
    response = vmanage.apiCall("GET", endpoint)
    return response

def migrateDevice(vmanage, uuid):
    """
    Migrate device software to vedge/cedge
    
    Parameters:
    uuid	 (string):	Device uuid
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/system/device/migrateDevice/{uuid}"
    response = vmanage.apiCall("PUT", endpoint)
    return response

def resetVedgeCloud(vmanage, uuid):
    """
    Reset vEdge device
    
    Parameters:
    uuid	 (string):	Device uuid
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/system/device/reset/{uuid}"
    response = vmanage.apiCall("PUT", endpoint)
    return response

def getRMACandidates(vmanage, deviceType, uuid):
    """
    Get RMA candidates by device type
    
    Parameters:
    deviceType	 (string):	Device Type
	uuid	 (string):	Excluded currently selected uuid
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/system/device/rma/candidates/{deviceType}?uuid={uuid}"
    response = vmanage.apiCall("GET", endpoint)
    return response

def getRootCertStatusAll(vmanage, state):
    """
    Get controllers vEdge sync status
    
    Parameters:
    state	 (string):	Root certificate state
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/system/device/rootcertchain/status?state={state}"
    response = vmanage.apiCall("GET", endpoint)
    return response

def checkvmanageSignedCert(vmanage):
    """
    Whether vmanage signed certificate created
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/system/device/vmanagesignedcert/iscreated"
    response = vmanage.apiCall("GET", endpoint)
    return response

def validateUser(vmanage, bodyParameter):
    """
    Authenticate vSmart user account
    
    Parameters:
    bodyParameter:	Description
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/system/device/smartaccount/authenticate"
    response = vmanage.apiCall("POST", endpoint, bodyParameter)
    return response

def syncDevices(vmanage, bodyParameter):
    """
    Sync devices from Smart-Account
    
    Parameters:
    bodyParameter:	Description
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/system/device/smartaccount/sync"
    response = vmanage.apiCall("POST", endpoint, bodyParameter)
    return response

def syncRootCertChain(vmanage):
    """
    Sync root certificate
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/system/device/sync/rootcertchain"
    response = vmanage.apiCall("GET", endpoint)
    return response

def getTenantManagementSystemIPs(vmanage):
    """
    Get management system IP
    NOTE: In a multitenant vManage system, this API is only available in the Provider view.
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/system/device/tenant/management/systemip"
    response = vmanage.apiCall("GET", endpoint)
    return response

def getCloudDockDataBasedOnDeviceType(vmanage, deviceCategory):
    """
    Get devices details
    
    Parameters:
    deviceCategory	 (string):	Device category
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/system/device/type/{deviceCategory}"
    response = vmanage.apiCall("GET", endpoint)
    return response

def getCloudDockDefaultConfigBasedOnDeviceType(vmanage, deviceCategory):
    """
    Get devices default config
    
    Parameters:
    deviceCategory	 (string):	Device category
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/system/device/type/{deviceCategory}/defaultConfig"
    response = vmanage.apiCall("GET", endpoint)
    return response

def getAllUnclaimedDevices(vmanage):
    """
    Get list of all unclaimed devices
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/system/device/unclaimedDevices"
    response = vmanage.apiCall("GET", endpoint)
    return response

def invalidateVmanageRootCA(vmanage, uuid):
    """
    Invalidate vManage root CA
    
    Parameters:
    uuid	 (string):	Device uuid
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/system/device/vmanagerootca/{uuid}"
    response = vmanage.apiCall("DELETE", endpoint)
    return response

def getDevicesDetails(vmanage, deviceCategory, model, state, uuid, deviceIP, validity):
    """
    Get devices details. When {deviceCategory = controllers}, it returns vEdge sync status, vBond, vManage and vSmart.
 {deviceCategory = vedges}, it returns all available vEdge routers
    
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
    
    endpoint = f"dataservice/system/device/{deviceCategory}?model={model}&state={state}&uuid={uuid}&deviceIP={deviceIP}&validity={validity}"
    response = vmanage.apiCall("GET", endpoint)
    return response

def editDevice(vmanage, deviceconfig, uuid):
    """
    Edit device
    
    Parameters:
    deviceconfig:	Device config
	uuid	 (string):	Device uuid
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/system/device/{uuid}"
    response = vmanage.apiCall("PUT", endpoint, deviceconfig)
    return response

def deleteDevice(vmanage, uuid):
    """
    Delete vEdges
    
    Parameters:
    uuid	 (string):	Device uuid
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/system/device/{uuid}"
    response = vmanage.apiCall("DELETE", endpoint)
    return response
