from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class Proxy(object):
    """
    Configuration - Device SSL Proxy Certificate Management API
    
    Implements GET POST DEL PUT methods for DeviceSSLProxyCertificateManagement endpoints

    """

    def __init__(self, session, host, port):
        self.host = host
        self.port = port
        self.client = HttpMethods.HttpClient(session=session)
    
    
    def getSelfSignedCert(self):
        """
        get self signed certificate
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/certificate/vmanage/selfsignedcert"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getProxyCertOfEdge(self, deviceId):
        """
        Get edge proxy certificate
        
        Parameters:
        deviceId	 (string):	Device Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/sslproxy/certificate?deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def updateCert(self, cert):
        """
        Upload device certificate
        
        Parameters:
        cert:	Upload device certificate
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/sslproxy/certificate"
        response = self.client.apiCall(HttpMethods.PUT, endpoint, cert)
        return response


    def addWANEdge(self, certstate, deviceId):
        """
        Add SSL proxy wan edge
        
        Parameters:
        certstate:	Cert state
		deviceId	 (string):	Device Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/sslproxy/certificate/wanedge/{deviceId}"
        response = self.client.apiCall(HttpMethods.POST, endpoint, certstate)
        return response


    def uploadCerts(self, certFile):
        """
        Upload device certificates
        
        Parameters:
        certFile:	Certificate file
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/sslproxy/certificates"
        response = self.client.apiCall(HttpMethods.POST, endpoint, certFile)
        return response


    def getSslProxyCSR(self, deviceId):
        """
        Get SSL proxy CSR
        
        Parameters:
        deviceId	 (string):	Device Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/sslproxy/csr?deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getAllDeviceCerts(self, devicelist):
        """
        Get certificate for all cEdges
        
        Parameters:
        devicelist:	Device list
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/sslproxy/devicecertificates"
        response = self.client.apiCall(HttpMethods.POST, endpoint, devicelist)
        return response


    def getAllDeviceCSR(self, devicelist):
        """
        Get CSR for all cEdges
        
        Parameters:
        devicelist:	Device list
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/sslproxy/devicecsr"
        response = self.client.apiCall(HttpMethods.POST, endpoint, devicelist)
        return response


    def generateSslProxyCSR(self, csrRequest):
        """
        CSR request SSL proxy for edge
        
        Parameters:
        csrRequest:	CSR request for edge
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/sslproxy/generate/csr/sslproxy"
        response = self.client.apiCall(HttpMethods.POST, endpoint, csrRequest)
        return response


    def generateSSLProxyCSR(self, csrRequest):
        """
        Generate CSR
        
        Parameters:
        csrRequest:	CSR request
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/sslproxy/generate/vmanage/csr"
        response = self.client.apiCall(HttpMethods.POST, endpoint, csrRequest)
        return response


    def getSslProxyList(self):
        """
        Get SSL proxy certificate list
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/sslproxy/list"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def renewCert(self, certRequest):
        """
        Renew device certificate
        
        Parameters:
        certRequest:	Renew device certificate request
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/sslproxy/renew"
        response = self.client.apiCall(HttpMethods.POST, endpoint, certRequest)
        return response


    def revokeCert(self, certRequest):
        """
        Revoke device certificate
        
        Parameters:
        certRequest:	Revoke device certificate request
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/sslproxy/revoke"
        response = self.client.apiCall(HttpMethods.POST, endpoint, certRequest)
        return response


    def revokeRenewCert(self, certRequest):
        """
        Revoke and renew device certificate
        
        Parameters:
        certRequest:	Revoke device certificate request
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/sslproxy/revokerenew"
        response = self.client.apiCall(HttpMethods.POST, endpoint, certRequest)
        return response


    def getCertState(self):
        """
        Get certificate state
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/sslproxy/settings/certificate"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getEntCert(self):
        """
        Get enterprise certificate
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/sslproxy/settings/enterprise/certificate"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def setEntCert(self, certRequest):
        """
        Configure enterprise certificate
        
        Parameters:
        certRequest:	Config enterprise certificate request
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/sslproxy/settings/enterprise/certificate"
        response = self.client.apiCall(HttpMethods.POST, endpoint, certRequest)
        return response


    def getVManageEntRootCert(self):
        """
        Get vManage enterprise root certificate
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/sslproxy/settings/enterprise/rootca"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def setEntRootCaCert(self, certRequest):
        """
        Set vManage enterprise root certificate
        
        Parameters:
        setenterpriserootcarequest:	Set enterprise root CA request
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/sslproxy/settings/enterprise/rootca"
        response = self.client.apiCall(HttpMethods.POST, endpoint, certRequest)
        return response


    def getvManageCert(self):
        """
        Get vManage intermediate certificate
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/sslproxy/settings/vmanage/certificate"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def setvManageintermediateCert(self, certRequest):
        """
        Set vManage root certificate
        
        Parameters:
        certRequest:	Set vManage intermediate CA request
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/sslproxy/settings/vmanage/certificate"
        response = self.client.apiCall(HttpMethods.POST, endpoint, certRequest)
        return response


    def getvManageCSR(self):
        """
        Get vManage CSR
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/sslproxy/settings/vmanage/csr"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getvManageRootCA(self):
        """
        Get vManage root certificate
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/sslproxy/settings/vmanage/rootca"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def setvManageRootCA(self, certRequest):
        """
        Set vManage root certificate
        
        Parameters:
        certRequest:	Set vManage root CA request
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/sslproxy/settings/vmanage/rootca"
        response = self.client.apiCall(HttpMethods.POST, endpoint, certRequest)
        return response


