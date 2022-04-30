from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class FeatureCert(object):
    """
    Configuration - Feature Certificate API
    
    Implements GET POST DEL PUT methods for Feature Certificate endpoints

    """

    def __init__(self, session, host, port):
        self.client = HttpMethods.HttpClient(session=session)
        self.host = host
        self.port = port
    
    
    def getDeviceCert(self, deviceId):
        """
        Get feature cert from cEdge device        
        NOTE: In a multitenant vManage system, this API is only available in the Provider and Provider-As-Tenant view.
        
        Parameters:
        deviceId	 (string):	Device Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/featurecertificate/certificate?deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def install(self, certRequest):
        """
        Upload feature cert for cEdge device        
        NOTE: In a multitenant vManage system, this API is only available in the Provider and Provider-As-Tenant view.
        
        Parameters:
        certRequest:	Install feature cert request for cEdge
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/featurecertificate/certificate"
        response = self.client.apiCall(HttpMethods.PUT, endpoint, certRequest)
        return response


    def getDeviceCsr(self, deviceId):
        """
        Get CSR from cEdge device        
        NOTE: In a multitenant vManage system, this API is only available in the Provider and Provider-As-Tenant view.
        
        Parameters:
        deviceId	 (string):	Device Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/featurecertificate/devicecsr?deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def genDeviceCsr(self, csrRequest):
        """
        Create CSR for cEdge device        
        NOTE: In a multitenant vManage system, this API is only available in the Provider and Provider-As-Tenant view.
        
        Parameters:
        csrRequest:	CSR request for cEdge
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/featurecertificate/devicecsr"
        response = self.client.apiCall(HttpMethods.PUT, endpoint, csrRequest)
        return response


    def revoke(self, revokeReq):
        """
        Revoke feature cert from cEdge device        
        NOTE: In a multitenant vManage system, this API is only available in the Provider and Provider-As-Tenant view.
        
        Parameters:
        revokeReq:	Revoking feature cert request for cEdge
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/featurecertificate/revoke"
        response = self.client.apiCall(HttpMethods.PUT, endpoint, revokeReq)
        return response


    def getFeatureCaState(self):
        """
        Get Feature CA state        
        NOTE: In a multitenant vManage system, this API is only available in the Provider and Provider-As-Tenant view.
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/featurecertificate/syslogconfig"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


