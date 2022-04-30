from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class Interface(object):
    """
    Real-Time Monitoring - Interface API
    
    Implements GET POST DEL PUT methods for Interface endpoints

    """

    def __init__(self, session, host, port):
        self.host = host
        self.port = port
        self.client = HttpMethods.HttpClient(session=session)
    
    
    def getInterface(self, vpnId, ifname, af, deviceId):
        """
        Get device interfaces
        
        Parameters:
        vpnId	        (string):	VPN Id
		ifname	        (string):	IF Name
		af  	        (string):	AF Type
		deviceId	    (string):	Device Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/interface?vpn-id={vpnId}&ifname={ifname}&af-type={af}&deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getARPStats(self, vpnId, ifname, af, deviceId):
        """
        Get interface ARP statistics
        
        Parameters:
        vpnId	        (string):	VPN Id
		ifname	        (string):	IF Name
		af  	        (string):	AF Type
		deviceId	    (string):	Device Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/interface/arp_stats?vpn-id={vpnId}&ifname={ifname}&af-type={af}&deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getErrorStats(self, vpnId, ifname, af, deviceId):
        """
        Get interface error stats
        
        Parameters:
        vpnId	        (string):	VPN Id
		ifname	        (string):	IF Name
		af  	        (string):	AF Type
		deviceId	    (string):	Device Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/interface/error_stats?vpn-id={vpnId}&ifname={ifname}&af-type={af}&deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getV6Stats(self, vpnId, ifname, af, deviceId):
        """
        Get interface IPv6 stats
        
        Parameters:
        vpnId	        (string):	VPN Id
		ifname	        (string):	IF Name
		af  	        (string):	AF Type
		deviceId	    (string):	Device Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/interface/ipv6Stats?vpn-id={vpnId}&ifname={ifname}&af-type={af}&deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getPktSizes(self, vpnId, ifname, af, deviceId):
        """
        Get interface packet size
        
        Parameters:
        vpnId	        (string):	VPN Id
		ifname	        (string):	IF Name
		af  	        (string):	AF Type
		deviceId	    (string):	Device Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/interface/pkt_size?vpn-id={vpnId}&ifname={ifname}&af-type={af}&deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getPortStats(self, vpnId, ifname, af, deviceId):
        """
        Get interface port stats
        
        Parameters:
        vpnId	        (string):	VPN Id
		ifname	        (string):	IF Name
		af  	        (string):	AF Type
		deviceId	    (string):	Device Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/interface/port_stats?vpn-id={vpnId}&ifname={ifname}&af-type={af}&deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getQosStats(self, vpnId, ifname, af, deviceId):
        """
        Get interface QOS stats
        
        Parameters:
        vpnId	        (string):	VPN Id
		ifname	        (string):	IF Name
		af  	        (string):	AF Type
		deviceId	    (string):	Device Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/interface/qosStats?vpn-id={vpnId}&ifname={ifname}&af-type={af}&deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getQueueStats(self, vpnId, ifname, af, deviceId):
        """
        Get interface queue stats
        
        Parameters:
        vpnId	        (string):	VPN Id
		ifname	        (string):	IF Name
		af  	        (string):	AF Type
		deviceId	    (string):	Device Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/interface/queue_stats?vpn-id={vpnId}&ifname={ifname}&af-type={af}&deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getDeviceSerialInterface(self, vpnId, ifname, af, deviceId):
        """
        Get serial interface
        
        Parameters:
        vpnId	        (string):	VPN Id
		ifname	        (string):	IF Name
		af  	        (string):	AF Type
		deviceId	    (string):	Device Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/interface/serial?vpn-id={vpnId}&ifname={ifname}&af-type={af}&deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getStats(self, vpnId, ifname, af, deviceId):
        """
        Get interface stats
        
        Parameters:
        vpnId	        (string):	VPN Id
		ifname	        (string):	IF Name
		af  	        (string):	AF Type
		deviceId	    (string):	Device Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/interface/stats?vpn-id={vpnId}&ifname={ifname}&af-type={af}&deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getSyncedInterface(self, vpnId, ifname, af, deviceId):
        """
        Get device interfaces synchronously
        
        Parameters:
        vpnId	        (string):	VPN Id
		ifname	        (string):	IF Name
		af  	        (string):	AF Type
		deviceId	    (string):	Device Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/interface/synced?vpn-id={vpnId}&ifname={ifname}&af-type={af}&deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def trustsec(self, deviceId):
        """
        Get policy filter memory usage from device
        
        Parameters:
        deviceId	 (string):	Device Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/interface/trustsec?deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getInterfaceVPN(self, deviceId):
        """
        Get device interfaces per VPN
        
        Parameters:
        deviceId	 (string):	Device Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/interface/vpn?deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


