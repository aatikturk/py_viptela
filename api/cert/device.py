from query_builder import Builder
import HttpMethods

class Device(object):
    """
    Certificate Management - Device API
    
    Implements GET POST DEL PUT methods for Device endpoints

    """

    def __init__(self, session, host, port):
        self.host = host
        self.port = port
        self.client = HttpMethods.HttpClient(session=session)
    
    
    def getCertDetails(self, parsecert):
        """
        Get cert details
        
        Parameters:
        parsecert:	parse cert
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/certificate/certdetails"
        response = self.client.apiCall(HttpMethods.POST, endpoint, parsecert)
        return response


    def getCSRViewRightMenus(self):
        """
        Get CSR detail view
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/certificate/csr/details"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getDeviceViewRightMenus(self):
        """
        Get device detail view
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/certificate/device/details"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getDevicesList(self):
        """
        Get vEdge list
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/certificate/device/list"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def forceSyncRootCert(self, singedcertificate):
        """
        Force sync root certificate<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider and Provider-As-Tenant view.
        
        Parameters:
        singedcertificate:	Singed certificate
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/certificate/forcesync/rootCert"
        response = self.client.apiCall(HttpMethods.POST, endpoint, singedcertificate)
        return response


    def generateCSR(self, csrrequestfordevice):
        """
        Generate CSR<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider and Provider-As-Tenant view.
        
        Parameters:
        csrrequestfordevice:	CSR request for device
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/certificate/generate/csr"
        response = self.client.apiCall(HttpMethods.POST, endpoint, csrrequestfordevice)
        return response


    def generateEnterpriseCSR(self, csrrequestfordevice):
        """
        Generate CSR<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider and Provider-As-Tenant view.
        
        Parameters:
        csrrequestfordevice:	CSR request for device
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/certificate/generate/enterprise/csr/vedge"
        response = self.client.apiCall(HttpMethods.POST, endpoint, csrrequestfordevice)
        return response


    def generateEnterpriseCSR(self, csrrequestfordevice):
        """
        Generate CSR<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider and Provider-As-Tenant view.
        
        Parameters:
        csrrequestfordevice:	CSR request for device
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/certificate/generate/wanedge/csr"
        response = self.client.apiCall(HttpMethods.POST, endpoint, csrrequestfordevice)
        return response


    def installCertificate(self, singedcertificate):
        """
        Install singed certificate<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider and Provider-As-Tenant view.
        
        Parameters:
        singedcertificate:	Singed certificate
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/certificate/install/signedCert"
        response = self.client.apiCall(HttpMethods.POST, endpoint, singedcertificate)
        return response


    def updateJks(self, updatejks):
        """
        update JKS<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider and Provider-As-Tenant view.
        
        Parameters:
        updatejks:	Update JKS
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/certificate/jks"
        response = self.client.apiCall(HttpMethods.PUT, endpoint, updatejks)
        return response


    def getListStatus(self):
        """
        get certificate
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/certificate/list/status"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getCertificateData(self):
        """
        Get certificate chain
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/certificate/record"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def resetRSA(self, csrrequestforvedge):
        """
        Register CSR<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider and Provider-As-Tenant view.
        
        Parameters:
        csrrequestforvedge:	CSR request for vEdge
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/certificate/reset/rsa"
        response = self.client.apiCall(HttpMethods.POST, endpoint, csrrequestforvedge)
        return response


    def decommissionEnterpriseCSRForVedge(self, revokingcsrforhardwarevedge):
        """
        Revoking enterprise CSR for hardware vEdge<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider and Provider-As-Tenant view.
        
        Parameters:
        revokingcsrforhardwarevedge:	Revoking CSR for hardware vEdge
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/certificate/revoke/enterprise/certificate"
        response = self.client.apiCall(HttpMethods.POST, endpoint, revokingcsrforhardwarevedge)
        return response


    def getRootCertChains(self, action):
        """
        Get root cert chain
        
        Parameters:
        action	 (string):	Action
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/certificate/rootcertchains?action={action}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def saveRootCertChain(self, saverootcertchain):
        """
        Save root cert chain<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider and Provider-As-Tenant view.
        
        Parameters:
        saverootcertchain:	Save root cert chain
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/certificate/rootcertchains"
        response = self.client.apiCall(HttpMethods.PUT, endpoint, saverootcertchain)
        return response


    def getRootCertificate(self):
        """
        Get device root certificate detail view
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/certificate/rootcertificate"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def saveVEdgeList(self, vedgedevicelist):
        """
        Save vEdge device list
        
        Parameters:
        vedgedevicelist:	vEdge device list
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/certificate/save/vedge/list"
        response = self.client.apiCall(HttpMethods.POST, endpoint, vedgedevicelist)
        return response


    def getCertificateDetail(self):
        """
        Get certificate detail
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/certificate/stats/detail"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getCertificateStats(self):
        """
        Get certificate expiration status
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/certificate/stats/summary"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def syncvBond(self):
        """
        sync vManage UUID to all vBond
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/certificate/syncvbond"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getcEdgeList(self):
        """
        Get cEdge list with tokengenerated list
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/certificate/tokengeneratedlist"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getInstalledCert(self):
        """
        Get Installed Certificate<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider and Provider-As-Tenant view.
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/certificate/vedge"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getvEdgeCSR(self):
        """
        Get vEdge CSR Certificate<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider and Provider-As-Tenant view.
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/certificate/vedge/csr"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getvEdgeList(self, model, state):
        """
        Get vEdge list
        
        Parameters:
        model	 (string):	Device model
		state	 (array):	Device state
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/certificate/vedge/list?model={model}&state={state}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def setvEdgeList(self, vedgedevicelist):
        """
        Save vEdge list
        
        Parameters:
        vedgedevicelist:	vEdge device list
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/certificate/vedge/list"
        response = self.client.apiCall(HttpMethods.POST, endpoint, vedgedevicelist)
        return response


    def getView(self):
        """
        Get certificate UI view
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/certificate/view"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getvSmartList(self):
        """
        Get vSmart list<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider and Provider-As-Tenant view.
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/certificate/vsmart/list"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def setvSmartList(self):
        """
        Save vSmart list
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/certificate/vsmart/list"
        response = self.client.apiCall(HttpMethods.POST, endpoint)
        return response


    def deleteConfiguration(self, uuid, replaceController, deviceId):
        """
        Invalidate device<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider and Provider-As-Tenant view.
        
        Parameters:
        uuid	 (string):	Device uuid
		replaceController	 (boolean):	Replace a vSmart in Multi-tenant setup with a new vSmart
		deviceId	 (string):	uuid of new vSmart
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/certificate/{uuid}?replaceController={replaceController}&deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.DELETE, endpoint)
        return response


