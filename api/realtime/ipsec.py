from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class IPsec(object):
    """
    Real-Time Monitoring - IPsec API
    
    Implements GET POST DEL PUT methods for IPsec endpoints

    """

    def __init__(self, session, host, port):
        self.host = host
        self.port = port
        self.client = HttpMethods.HttpClient(session=session)
    
    
    def createCryptoIpsecIdentity(self, rTlocAddr, rTlocColor, lTlocColor, deviceId):
        """
        Get Crypto IPSEC identity entry from device
        
        Parameters:
        rTlocAddr	 (string):	Remote TLOC address
		rTlocColor	 (string):	Remote tloc color
		lTlocColor	 (string):	Local tloc color
		deviceId	 (string):	Device IP
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/ipsec/identity?rTlocAddr={rTlocAddr}&rTlocColor={rTlocColor}&lTlocColor={lTlocColor}&deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def createIkeInboundList(self, deviceId):
        """
        Get IPsec IKE inbound connection list from device
        
        Parameters:
        deviceId	 (string):	Device IP
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/ipsec/ike/inbound?deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def createIkeOutboundList(self, deviceId):
        """
        Get IPsec IKE outbound connection list from device
        
        Parameters:
        deviceId	 (string):	Device IP
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/ipsec/ike/outbound?deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def createIkeSessions(self, rTlocAddr, rTlocColor, deviceId):
        """
        Get IPsec IKE sessions from device
        
        Parameters:
        rTlocAddr	 (string):	Remote TLOC address
		rTlocColor	 (string):	Remote tloc color
		deviceId	 (string):	Device IP
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/ipsec/ike/sessions?rTlocAddr={rTlocAddr}&rTlocColor={rTlocColor}&deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def createCryptov1LocalSAList(self, rTlocAddr, rTlocColor, deviceId):
        """
        Get Crypto IKEv1 SA entry from device
        
        Parameters:
        rTlocAddr	 (string):	Remote TLOC address
		rTlocColor	 (string):	Remote tloc color
		deviceId	 (string):	Device IP
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/ipsec/ikev1?rTlocAddr={rTlocAddr}&rTlocColor={rTlocColor}&deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def createCryptov2LocalSAList(self, deviceId):
        """
        Get Crypto IKEv2 SA entry from device
        
        Parameters:
        deviceId	 (string):	Device IP
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/ipsec/ikev2?deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def createInBoundList(self, rTlocAddr, rTlocColor, lTlocColor, deviceId):
        """
        Get IPsec inbound connection list from device (Real Time)
        
        Parameters:
        rTlocAddr	 (string):	Remote TLOC address
		rTlocColor	 (string):	Remote tloc color
		lTlocColor	 (string):	Local tloc color
		deviceId	 (string):	Device IP
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/ipsec/inbound?rTlocAddr={rTlocAddr}&rTlocColor={rTlocColor}&lTlocColor={lTlocColor}&deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def createLocalSAList(self, deviceId):
        """
        Get IPsec local SA list from device
        
        Parameters:
        deviceId	 (string):	Device IP
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/ipsec/localsa?deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def createOutBoundList(self, rTlocAddr, rTlocColor, deviceId):
        """
        Get IPsec outbound connection list from device (Real Time)
        
        Parameters:
        rTlocAddr	 (string):	Remote TLOC address
		rTlocColor	 (string):	Remote tloc color
		deviceId	 (string):	Device IP
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/ipsec/outbound?rTlocAddr={rTlocAddr}&rTlocColor={rTlocColor}&deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def createIPsecPWKInboundConnections(self, rTlocAddr, rTlocColor, lTlocColor, deviceId):
        """
        Get IPSEC pairwise key inbound entry from device
        
        Parameters:
        rTlocAddr	 (string):	Remote TLOC address
		rTlocColor	 (string):	Remote tloc color
		lTlocColor	 (string):	Local tloc color
		deviceId	 (string):	Device IP
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/ipsec/pwk/inbound?rTlocAddr={rTlocAddr}&rTlocColor={rTlocColor}&lTlocColor={lTlocColor}&deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def createIPsecPWKLocalSA(self, rTlocAddr, rTlocColor, lTlocColor, deviceId):
        """
        Get IPSEC pairwise key local SA  entry from device
        
        Parameters:
        rTlocAddr	 (string):	Remote TLOC address
		rTlocColor	 (string):	Remote tloc color
		lTlocColor	 (string):	Local tloc color
		deviceId	 (string):	Device IP
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/ipsec/pwk/localsa?rTlocAddr={rTlocAddr}&rTlocColor={rTlocColor}&lTlocColor={lTlocColor}&deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def createIPsecPWKOutboundConnections(self, rTlocAddr, rTlocColor, lTlocColor, deviceId):
        """
        Get IPSEC pairwise key outbound entry from device
        
        Parameters:
        rTlocAddr	 (string):	Remote TLOC address
		rTlocColor	 (string):	Remote tloc color
		lTlocColor	 (string):	Local tloc color
		deviceId	 (string):	Device IP
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/ipsec/pwk/outbound?rTlocAddr={rTlocAddr}&rTlocColor={rTlocColor}&lTlocColor={lTlocColor}&deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


