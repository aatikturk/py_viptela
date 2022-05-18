from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class Flow(object):
    """
    Monitoring - Cflowd Flows API
    
    Implements GET POST DEL PUT methods for CflowdFlows endpoints

    """

    def __init__(self, session, host, port):
        self.client = HttpMethods.HttpClient(session=session)
        self.host = host
        self.port = port
    
    
    def getCflowdDPIDeviceFieldJSON(self, isDeviceDashBoard):
        """
        Get Cflowd DPI query field JSON
        
        Parameters:
        isDeviceDashBoard	 (boolean):	Flag whether it is device dashboard request
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/cflowd/application/fields?isDeviceDashBoard={isDeviceDashBoard}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getCollectorList(self, deviceId):
        """
        Get cflowd collector list from device
        
        Parameters:
        deviceId	 (string):	Device IP
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/cflowd/collector?deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getDPIFieldJSON(self, isDeviceDashBoard):
        """
        Get CflowdvDPI query field JSON
        
        Parameters:
        isDeviceDashBoard	 (boolean):	Flag whether it is device dashboard request
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/cflowd/device/fields?isDeviceDashBoard={isDeviceDashBoard}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getFlows(self, vpnId, src, dest, deviceId):
        """
        Get list of cflowd flows from device
        
        Parameters:
        vpnId	        (string):	VPN Id
		src	            (string):	Source IP
		dest	        (string):	Destination IP
		deviceId	    (string):	Device IP
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/cflowd/flows?vpn-id={vpnId}&src-ip={src}&dest-ip={dest}&deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getFlowsCount(self, vpnId, src, dest, deviceId):
        """
        Get cflowd flow count from device
        
        Parameters:
        vpnId	        (string):	VPN Id
		src	            (string):	Source IP
		dest	        (string):	Destination IP
		deviceId	    (string):	Device IP
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/cflowd/flows-count?vpn-id={vpnId}&src-ip={src}&dest-ip={dest}&deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getFnFCacheStats(self, deviceId):
        """
        Get FnF cache stats from device
        
        Parameters:
        deviceId	 (string):	Device IP
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/cflowd/fnf/cache-stats?deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getFnFExportClientStats(self, deviceId):
        """
        Get FnF export client stats from device
        
        Parameters:
        deviceId	 (string):	Device IP
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/cflowd/fnf/export-client-stats?deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getFnFExportStats(self, deviceId):
        """
        Get FnF export stats from device
        
        Parameters:
        deviceId	 (string):	Device IP
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/cflowd/fnf/export-stats?deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getFnf(self, deviceId):
        """
        Get FnF from device
        
        Parameters:
        deviceId	 (string):	Device IP
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/cflowd/fnf/flow-monitor?deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getFnFMonitorStats(self, deviceId):
        """
        Get FnF monitor stats from device
        
        Parameters:
        deviceId	 (string):	Device IP
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/cflowd/fnf/monitor-stats?deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getStatistics(self, deviceId):
        """
        Get cflowd statistics from device
        
        Parameters:
        deviceId	 (string):	Device IP
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/cflowd/statistics?deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getTemplate(self, deviceId):
        """
        Get cflowd template from device
        
        Parameters:
        deviceId	 (string):	Device IP
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/cflowd/template?deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


