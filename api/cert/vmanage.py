from query_builder import Builder
import HttpMethods

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


    def importCertificate(self, singedcertificate):
        """
        Import a signed web server certificate
        
        Parameters:
        singedcertificate:	Singed certificate
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/setting/configuration/webserver/certificate"
        response = self.client.apiCall(HttpMethods.PUT, endpoint, singedcertificate)
        return response


    def getCSR(self, csrsigningrequest):
        """
        Generate Certificate Signing Request
        
        Parameters:
        csrsigningrequest:	CSR signing request
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/setting/configuration/webserver/certificate"
        response = self.client.apiCall(HttpMethods.POST, endpoint, csrsigningrequest)
        return response


    def DumpCertificate(self, type):
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


    def GetCertificate(self):
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


