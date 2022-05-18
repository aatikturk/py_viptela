from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

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
        Force sync root certificate
        NOTE: In a multitenant vManage system, this API is only available in the Provider and Provider-As-Tenant view.
        
        Parameters:
        singedcertificate:	Singed certificate
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/certificate/forcesync/rootCert"
        response = self.client.apiCall(HttpMethods.POST, endpoint, singedcertificate)
        return response


    def generateCSR(self, csrRequest):
        """
        Generate CSR
        NOTE: In a multitenant vManage system, this API is only available in the Provider and Provider-As-Tenant view.
        
        Parameters:
        csrRequest:	CSR request for device
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/certificate/generate/csr"
        response = self.client.apiCall(HttpMethods.POST, endpoint, csrRequest)
        return response


    def generateEntCSR(self, csrRequest):
        """
        Generate CSR
        NOTE: In a multitenant vManage system, this API is only available in the Provider and Provider-As-Tenant view.
        
        Parameters:
        csrRequest:	CSR request for device
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/certificate/generate/enterprise/csr/vedge"
        response = self.client.apiCall(HttpMethods.POST, endpoint, csrRequest)
        return response


    def generateVedgeEntCSR(self, csrRequest):
        """
        Generate CSR
        NOTE: In a multitenant vManage system, this API is only available in the Provider and Provider-As-Tenant view.
        
        Parameters:
        csrRequest:	CSR request for device
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/certificate/generate/wanedge/csr"
        response = self.client.apiCall(HttpMethods.POST, endpoint, csrRequest)
        return response


    def installCertificate(self, singedCert):
        """
        Install singed certificate
        NOTE: In a multitenant vManage system, this API is only available in the Provider and Provider-As-Tenant view.
        
        Parameters:
        singedCert:	Singed certificate
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/certificate/install/signedCert"
        response = self.client.apiCall(HttpMethods.POST, endpoint, singedCert)
        return response


    def updateJks(self, updatejks):
        """
        update JKS
        NOTE: In a multitenant vManage system, this API is only available in the Provider and Provider-As-Tenant view.
        
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


    def resetRSA(self, csrRequest):
        """
        Register CSR
        NOTE: In a multitenant vManage system, this API is only available in the Provider and Provider-As-Tenant view.
        
        Parameters:
        csrRequest:	CSR request for vEdge
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/certificate/reset/rsa"
        response = self.client.apiCall(HttpMethods.POST, endpoint, csrRequest)
        return response


    def decommissionEnterpriseCSRForVedge(self, revokingcsrforhardwarevedge):
        """
        Revoking enterprise CSR for hardware vEdge
        NOTE: In a multitenant vManage system, this API is only available in the Provider and Provider-As-Tenant view.
        
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


    def saveRootCertChain(self, rootChain):
        """
        Save root cert chain
        NOTE: In a multitenant vManage system, this API is only available in the Provider and Provider-As-Tenant view.
        
        Parameters:
        rootChain:	Save root cert chain
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/certificate/rootcertchains"
        response = self.client.apiCall(HttpMethods.PUT, endpoint, rootChain)
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


    def saveVEdgeList(self, deviceList):
        """
        Save vEdge device list
        
        Parameters:
        deviceList:	vEdge device list
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/certificate/save/vedge/list"
        response = self.client.apiCall(HttpMethods.POST, endpoint, deviceList)
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
        Get Installed Certificate
        NOTE: In a multitenant vManage system, this API is only available in the Provider and Provider-As-Tenant view.
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/certificate/vedge"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getvEdgeCSR(self):
        """
        Get vEdge CSR Certificate
        NOTE: In a multitenant vManage system, this API is only available in the Provider and Provider-As-Tenant view.
        
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


    def setvEdgeList(self, deviceList):
        """
        Save vEdge list
        
        Parameters:
        deviceList:	vEdge device list
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/certificate/vedge/list"
        response = self.client.apiCall(HttpMethods.POST, endpoint, deviceList)
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
        Get vSmart list
        NOTE: In a multitenant vManage system, this API is only available in the Provider and Provider-As-Tenant view.
        
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


    def deleteConfig(self, uuid, replaceController, deviceId):
        """
        Invalidate device
        NOTE: In a multitenant vManage system, this API is only available in the Provider and Provider-As-Tenant view.
        
        Parameters:
        uuid	                (string):	Device uuid
		replaceController	    (boolean):	Replace a vSmart in Multi-tenant setup with a new vSmart
		deviceId	            (string):	uuid of new vSmart
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/certificate/{uuid}?replaceController={replaceController}&deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.DELETE, endpoint)
        return response


