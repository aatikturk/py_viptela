from query_builder import Builder
import HttpMethods

class Chain(object):
    """
    Colocation - Service Chain API
    
    Implements GET POST DEL PUT methods for ServiceChain endpoints

    """

    def __init__(self, session, host, port):
        self.host = host
        self.port = port
        self.client = HttpMethods.HttpClient(session=session)
    
    
    def attachServiceChain(self, attachservicechainrequest):
        """
        Attach service chain to cluster
        
        Parameters:
        attachservicechainrequest:	Attach service chain request
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/colocation/servicechain/attach"
        response = self.client.apiCall(HttpMethods.POST, endpoint, attachservicechainrequest)
        return response


    def attachServiceChain(self, attachservicechainrequest):
        """
        Attach service chain to cluster
        
        Parameters:
        attachservicechainrequest:	Attach service chain request
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/colocation/servicechain/autoattach"
        response = self.client.apiCall(HttpMethods.POST, endpoint, attachservicechainrequest)
        return response


    def detachServiceChain(self, detachservicechainrequest):
        """
        Detach service chain
        
        Parameters:
        detachservicechainrequest:	Detach service chain request
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/colocation/servicechain/detach"
        response = self.client.apiCall(HttpMethods.PUT, endpoint, detachservicechainrequest)
        return response


    def getEdgeDevices(self):
        """
        Get edge devices
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/colocation/servicechain/edge/devices"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getpnfDevices(self, pnfDeviceType):
        """
        Get PNF edge devices
        
        Parameters:
        pnfDeviceType	 (string):	PNF device type
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/colocation/servicechain/edge/pnfdevices?pnfDeviceType={pnfDeviceType}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


