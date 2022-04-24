from query_builder import Builder
import HttpMethods

class DNAC(object):
    """
    Partner - DNAC SDA API API
    
    Implements GET POST DEL PUT methods for DNACSDAAPI endpoints

    """

    def __init__(self, session, host, port):
        self.host = host
        self.port = port
        self.client = HttpMethods.HttpClient(session=session)
    
    
    def createSDAConfig(self, devicesdaconfiguration, partnerId):
        """
        Create SDA enabled device
        
        Parameters:
        devicesdaconfiguration:	Device SDA configuration
		partnerId	 (string):	Partner Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/partner/dnac/sda/config/{partnerId}"
        response = self.client.apiCall(HttpMethods.POST, endpoint, devicesdaconfiguration)
        return response


    def getSDAEnabledDevices(self, partnerId):
        """
        Get SDA enabled devices
        
        Parameters:
        partnerId	 (string):	Partner Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/partner/dnac/sda/device/{partnerId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getDeviceDetails(self, partnerId, uuid):
        """
        Get SDA enabled devices detail
        
        Parameters:
        partnerId	 (string):	Partner Id
		uuid	 (string):	Device uuid
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/partner/dnac/sda/device/{partnerId}/{uuid}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def createSDAConfigFromNetconf(self, devicesdaconfiguration, partnerId):
        """
        Create SDA enabled device from Netconf
        
        Parameters:
        devicesdaconfiguration:	Device SDA configuration
		partnerId	 (string):	Partner Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/partner/dnac/sda/netconfconfig/{partnerId}"
        response = self.client.apiCall(HttpMethods.POST, endpoint, devicesdaconfiguration)
        return response


    def getSitesForPartner(self, partnerId):
        """
        Get SDA enabled devices
        
        Parameters:
        partnerId	 (string):	Partner Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/partner/dnac/sda/site/{partnerId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getOverlayVPNList(self):
        """
        Get Overlay VPN list
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/partner/dnac/sda/vpn"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


