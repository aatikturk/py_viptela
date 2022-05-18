from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class DPI(object):
    """
    Real-Time Monitoring - DPI API
    
    Implements GET POST DEL PUT methods for DPI endpoints

    """

    def __init__(self, session, host, port):
        self.host = host
        self.port = port
        self.client = HttpMethods.HttpClient(session=session)
    
    
    def getDPIDeviceFieldJSON(self, isDeviceDashBoard):
        """
        Get DPI query field from device
        
        Parameters:
        isDeviceDashBoard	 (boolean):	Flag whether is device dashboard request
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/dpi/application/fields?isDeviceDashBoard={isDeviceDashBoard}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def createDPICollectorList(self, vpnId, application, family, deviceId):
        """
        Get DPI applications from device (Real Time)
        
        Parameters:
        vpnId	 (string):	VPN Id
		application	 (string):	Application
		family	 (string):	Family
		deviceId	 (string):	Device Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/dpi/applications?vpn-id={vpnId}&application={application}&family={family}&deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getCommonAppList(self):
        """
        Get DPI common application list from device
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/dpi/common/applications"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getDPIFieldJSON(self):
        """
        Get DPI field from device
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/dpi/device/fields"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getDPIDeviceDetailsFieldJSON(self):
        """
        Get DPI detailed field from device
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/dpi/devicedetails/fields"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getDPIFlowsList(self, vpnId, ip, application, family, deviceId):
        """
        Get DPI flow list from device (Real Time)
        
        Parameters:
        vpnId	            (string):	VPN Id
		ip	                (string):	Source IP
		application	        (string):	Application
		family	            (string):	Family
		deviceId	        (string):	Device Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/dpi/flows?vpn-id={vpnId}&src-ip={ip}&application={application}&family={family}&deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getQosmosAppList(self):
        """
        Get DPI QoSMos application list from device
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/dpi/qosmos/applications"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getDPISummaryRealTime(self, deviceId):
        """
        Get DPI summary from device (Real Time)
        
        Parameters:
        deviceId	 (string):	Device Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/dpi/summary?deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getDPIStatistics(self, application, family, deviceId):
        """
        Get supported applications from device (Real Time)
        
        Parameters:
        application	 (string):	Application
		family	 (string):	Family
		deviceId	 (string):	Device Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/dpi/supported-applications?application={application}&family={family}&deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


