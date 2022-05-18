from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class Vmanage(object):
    """
    Certificate Management - vManage API
    
    Implements GET POST DEL PUT methods for vManage endpoints

    """

    def __init__(self, session, host, port):
        self.host = host
        self.port = port
        self.client = HttpMethods.HttpClient(session=session)
    
    
    def showInfo(self):
        """
        Retrieves Certificate Signing Request information
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/setting/configuration/webserver/certificate"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def importCert(self, signedCert):
        """
        Import a signed web server certificate
        
        Parameters:
        signedCert:	Singed certificate
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/setting/configuration/webserver/certificate"
        response = self.client.apiCall(HttpMethods.PUT, endpoint, signedCert)
        return response


    def getCSR(self, csrRequest):
        """
        Generate Certificate Signing Request
        
        Parameters:
        csrRequest:	CSR signing request
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/setting/configuration/webserver/certificate"
        response = self.client.apiCall(HttpMethods.POST, endpoint, csrRequest)
        return response


    def dumpCert(self, type):
        """
        Get certificate with alias name
        
        Parameters:
        type	 (string):	Key alias
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/setting/configuration/webserver/certificate/certificate?type={type}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getCert(self):
        """
        Get certificate for alias server
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/setting/configuration/webserver/certificate/getcertificate"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def rollback(self, type):
        """
        Rollback certificate with alias name
        
        Parameters:
        type	 (string):	Key alias
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/setting/configuration/webserver/certificate/rollback?type={type}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


