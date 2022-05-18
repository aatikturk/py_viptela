from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class IP(object):
    """
    Real-Time Monitoring - IP API
    
    Implements GET POST DEL PUT methods for IP endpoints

    """

    def __init__(self, session, host, port):
        self.host = host
        self.port = port
        self.client = HttpMethods.HttpClient(session=session)
    
    
    def getFib(self, vpnId, af, prefix, tloc, color, deviceId):
        """
        Get FIB list from device (Real Time)
        
        Parameters:
        vpnId	 (string):	VPN Id
		af	 (string):	Address family
		prefix	 (string):	IP prefix
		tloc	 (string):	tloc IP
		color	 (string):	tloc color
		deviceId	 (string):	Device Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/ip/fib?vpnId={vpnId}&af={af}&prefix={prefix}&tloc={tloc}&color={color}&deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getIetfRouting(self, instanceName, af, outIf, srcProto, nextHop, deviceId):
        """
        Get ietf routing list from device
        
        Parameters:
        instanceName	 (string):	VPN Id
		af	 (string):	Address family
		outIf	 (string):	Outgoing Interface
		srcProto	 (string):	Source Protocol
		nextHop	 (string):	Next Hop Address
		deviceId	 (string):	Device Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/ip/ipRoutes?instanceName={instanceName}&af={af}&outIf={outIf}&srcProto={srcProto}&nextHop={nextHop}&deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getIPMfibOil(self, deviceId):
        """
        Get IP MFIB OIL list from device (Real Time)
        
        Parameters:
        deviceId	 (string):	Device Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/ip/mfiboil?deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getIPMfibStats(self, deviceId):
        """
        Get IP MFIB statistics list from device (Real Time)
        
        Parameters:
        deviceId	 (string):	Device Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/ip/mfibstats?deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getIPMfibSummary(self, deviceId):
        """
        Get IP MFIB summary list from device (Real Time)
        
        Parameters:
        deviceId	 (string):	Device Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/ip/mfibsummary?deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getNatFilter(self, natVpnId, natIfname, privateSrcAddr, proto, deviceId):
        """
        Get NAT filter list from device
        
        Parameters:
        natVpnId	 (string):	NAT VPN Id
		natIfname	 (string):	NAT interface name
		privateSrcAddr	 (string):	Private source address
		proto	 (string):	Protocol
		deviceId	 (string):	Device Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/ip/nat/filter?natVpnId={natVpnId}&natIfname={natIfname}&privateSrcAddr={privateSrcAddr}&proto={proto}&deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getNatInterface(self, deviceId):
        """
        Get NAT interface list from device (Real Time)
        
        Parameters:
        deviceId	 (string):	Device Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/ip/nat/interface?deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getNatIfStats(self, deviceId):
        """
        Get NAT interface statistics list from device
        
        Parameters:
        deviceId	 (string):	Device Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/ip/nat/interfacestatistics?deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getNatTranslations(self, deviceId):
        """
        Get NAT translation list from device (Real Time)
        
        Parameters:
        deviceId	 (string):	Device Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/ip/nat/translation?deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getNat64Translations(self, deviceId):
        """
        Get NAT64 interface list from device
        
        Parameters:
        deviceId	 (string):	Device Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/ip/nat64/translation?deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getRouteTable(self, vpnId, af, prefix, protocol, deviceId):
        """
        Get route table list from device (Real Time)
        
        Parameters:
        vpnId	 (string):	VPN Id
		af	 (string):	Address family
		prefix	 (string):	IP prefix
		protocol	 (string):	IP protocol
		deviceId	 (string):	Device Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/ip/routetable?vpnId={vpnId}&af={af}&prefix={prefix}&protocol={protocol}&deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


