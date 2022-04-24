from query_builder import Builder
import HttpMethods

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


    def updateCertificate(self, uploaddevicecertificate):
        """
        Upload device certificate
        
        Parameters:
        uploaddevicecertificate:	Upload device certificate
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/sslproxy/certificate"
        response = self.client.apiCall(HttpMethods.PUT, endpoint, uploaddevicecertificate)
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


    def uploadCertificiates(self, certificatefile):
        """
        Upload device certificates
        
        Parameters:
        certificatefile:	Certificate file
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/sslproxy/certificates"
        response = self.client.apiCall(HttpMethods.POST, endpoint, certificatefile)
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


    def getAllDeviceCertificates(self, devicelist):
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


    def generateSslProxyCSR(self, csrrequestforedge):
        """
        CSR request SSL proxy for edge
        
        Parameters:
        csrrequestforedge:	CSR request for edge
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/sslproxy/generate/csr/sslproxy"
        response = self.client.apiCall(HttpMethods.POST, endpoint, csrrequestforedge)
        return response


    def generateSSLProxyCSR(self, csrrequest):
        """
        Generate CSR
        
        Parameters:
        csrrequest:	CSR request
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/sslproxy/generate/vmanage/csr"
        response = self.client.apiCall(HttpMethods.POST, endpoint, csrrequest)
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


    def renewCertificate(self, renewdevicecertificaterequest):
        """
        Renew device certificate
        
        Parameters:
        renewdevicecertificaterequest:	Renew device certificate request
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/sslproxy/renew"
        response = self.client.apiCall(HttpMethods.POST, endpoint, renewdevicecertificaterequest)
        return response


    def revokeCertificate(self, revokedevicecertificaterequest):
        """
        Revoke device certificate
        
        Parameters:
        revokedevicecertificaterequest:	Revoke device certificate request
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/sslproxy/revoke"
        response = self.client.apiCall(HttpMethods.POST, endpoint, revokedevicecertificaterequest)
        return response


    def revokeRenewCertificate(self, revokedevicecertificaterequest):
        """
        Revoke and renew device certificate
        
        Parameters:
        revokedevicecertificaterequest:	Revoke device certificate request
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/sslproxy/revokerenew"
        response = self.client.apiCall(HttpMethods.POST, endpoint, revokedevicecertificaterequest)
        return response


    def getCertificateState(self):
        """
        Get certificate state
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/sslproxy/settings/certificate"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getEnterpriseCertificate(self):
        """
        Get enterprise certificate
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/sslproxy/settings/enterprise/certificate"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def setEnterpriseCert(self, configenterprisecertificaterequest):
        """
        Configure enterprise certificate
        
        Parameters:
        configenterprisecertificaterequest:	Config enterprise certificate request
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/sslproxy/settings/enterprise/certificate"
        response = self.client.apiCall(HttpMethods.POST, endpoint, configenterprisecertificaterequest)
        return response


    def getVManageEnterpriseRootCertificate(self):
        """
        Get vManage enterprise root certificate
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/sslproxy/settings/enterprise/rootca"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def setEnterpriseRootCaCert(self, setenterpriserootcarequest):
        """
        Set vManage enterprise root certificate
        
        Parameters:
        setenterpriserootcarequest:	Set enterprise root CA request
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/sslproxy/settings/enterprise/rootca"
        response = self.client.apiCall(HttpMethods.POST, endpoint, setenterpriserootcarequest)
        return response


    def getvManageCertificate(self):
        """
        Get vManage intermediate certificate
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/sslproxy/settings/vmanage/certificate"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def setvManageintermediateCert(self, setvmanageintermediatecarequest):
        """
        Set vManage root certificate
        
        Parameters:
        setvmanageintermediatecarequest:	Set vManage intermediate CA request
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/sslproxy/settings/vmanage/certificate"
        response = self.client.apiCall(HttpMethods.POST, endpoint, setvmanageintermediatecarequest)
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


    def setvManageRootCA(self, setvmanagerootcarequest):
        """
        Set vManage root certificate
        
        Parameters:
        setvmanagerootcarequest:	Set vManage root CA request
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/sslproxy/settings/vmanage/rootca"
        response = self.client.apiCall(HttpMethods.POST, endpoint, setvmanagerootcarequest)
        return response


