from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class Connectivity(object):
    """
    Troubleshooting Tools - Device Connectivity API
    
    Implements GET POST DEL PUT methods for Device Connectivity endpoints

    """

    def __init__(self, session, host, port):
        self.host = host
        self.port = port
        self.client = HttpMethods.HttpClient(session=session)
    
    
    def invalidateDevice(self, devInfo):
        """
        invalidate the device
        
        Parameters:
        devInfo:	vEdge device info
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/certificate/device/invalidate"
        response = self.client.apiCall(HttpMethods.POST, endpoint, devInfo)
        return response


    def stageDevice(self, devInfo):
        """
        Stop data traffic to device
        
        Parameters:
        devInfo:	vEdge device info
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/certificate/device/stage"
        response = self.client.apiCall(HttpMethods.POST, endpoint, devInfo)
        return response


    def createAdminTech(self, request):
        """
        Generate admin tech logs
        
        Parameters:
        request:	Admin tech generation request
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/tools/admintech"
        response = self.client.apiCall(HttpMethods.POST, endpoint, request)
        return response


    def copyAdminTechOnDevice(self, request):
        """
        copy admin tech logs
        
        Parameters:
        request:	Admin tech copy request
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/tools/admintech/copy"
        response = self.client.apiCall(HttpMethods.POST, endpoint, request)
        return response


    def deleteAdminTechOnDevice(self, request):
        """
        delete admin tech logs
        
        Parameters:
        request:	Admin tech copy request
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/tools/admintech/delete"
        response = self.client.apiCall(HttpMethods.DELETE, endpoint, request)
        return response


    def downloadAdminTechFile(self, filename):
        """
        Download admin tech logs
        
        Parameters:
        filename	 (string):	Admin tech file
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/tools/admintech/download/{filename}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def deleteAdminTechFile(self, requestID):
        """
        Delete admin tech logs
        
        Parameters:
        requestID	 (string):	Request Id of admin tech generation request
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/tools/admintech/{requestID}"
        response = self.client.apiCall(HttpMethods.DELETE, endpoint)
        return response


    def listAdminTechsOnDevice(self, request):
        """
        List admin tech logs
        
        Parameters:
        request:	Admin tech listing request
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/tools/admintechlist"
        response = self.client.apiCall(HttpMethods.POST, endpoint, request)
        return response


    def listAdminTechs(self):
        """
        Get device admin-tech information
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/tools/admintechs"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getInProgressCount(self):
        """
        Get device admin-tech InProgressCount
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/tools/admintechs/inprogress"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def factoryReset(self, payload):
        """
        Device factory reset
        
        Parameters:
        payload:	Device factory reset
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/tools/factoryreset"
        response = self.client.apiCall(HttpMethods.POST, endpoint, payload)
        return response


    def npingDevice(self, npingparameter, deviceIP):
        """
        NPing device
        
        Parameters:
        npingparameter:	NPing parameter
		deviceIP	 (string):	Device IP
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/tools/nping/{deviceIP}"
        response = self.client.apiCall(HttpMethods.POST, endpoint, npingparameter)
        return response


    def pingDevice(self, pingparameter, deviceIP):
        """
        Ping device
        
        Parameters:
        pingparameter:	Ping parameter
		deviceIP	 (string):	Device IP
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/tools/ping/{deviceIP}"
        response = self.client.apiCall(HttpMethods.POST, endpoint, pingparameter)
        return response


    def processPortHopColor(self, deviceporthopcolor, deviceIP):
        """
        Request port hop color
        
        Parameters:
        deviceporthopcolor:	Device port hop color
		deviceIP	 (string):	Device IP
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/tools/porthopcolor/{deviceIP}"
        response = self.client.apiCall(HttpMethods.POST, endpoint, deviceporthopcolor)
        return response


    def processInterfaceReset(self, deviceinterface, deviceIP):
        """
        Reset device interface
        
        Parameters:
        deviceinterface:	Device interface
		deviceIP	 (string):	Device IP
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/tools/reset/interface/{deviceIP}"
        response = self.client.apiCall(HttpMethods.POST, endpoint, deviceinterface)
        return response


    def processResetUser(self, deviceuserreset, deviceIP):
        """
        Request reset user
        
        Parameters:
        deviceuserreset:	Device user reset
		deviceIP	 (string):	Device IP
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/tools/resetuser/{deviceIP}"
        response = self.client.apiCall(HttpMethods.POST, endpoint, deviceuserreset)
        return response


    def servicePath(self, servicepathparameter, deviceIP):
        """
        Service path
        
        Parameters:
        servicepathparameter:	Service path parameter
		deviceIP	 (string):	Device IP
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/tools/servicepath/{deviceIP}"
        response = self.client.apiCall(HttpMethods.POST, endpoint, servicepathparameter)
        return response


    def tracerouteDevice(self, tracerouteparameter, deviceIP):
        """
        Traceroute
        
        Parameters:
        tracerouteparameter:	Traceroute parameter
		deviceIP	 (string):	Device IP
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/tools/traceroute/{deviceIP}"
        response = self.client.apiCall(HttpMethods.POST, endpoint, tracerouteparameter)
        return response


    def tunnelPath(self, tunnelpathparameter, deviceIP):
        """
        TunnelPath
        
        Parameters:
        tunnelpathparameter:	TunnelPath parameter
		deviceIP	 (string):	Device IP
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/tools/tunnelpath/{deviceIP}"
        response = self.client.apiCall(HttpMethods.POST, endpoint, tunnelpathparameter)
        return response


    def getControlConnections(self, uuid):
        """
        Troubleshoot control connections
        
        Parameters:
        uuid	 (string):	Device uuid
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/troubleshooting/control/{uuid}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getDeviceConfiguration(self, uuid):
        """
        Debug device bring up
        
        Parameters:
        uuid	 (string):	Device uuid
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/troubleshooting/devicebringup?uuid={uuid}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


