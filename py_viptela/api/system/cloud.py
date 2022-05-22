from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class Cloud(object):
    """
    System - Cloud Service API
    
    Implements GET POST DEL PUT methods for CloudService endpoints

    """

    def __init__(self, session, host, port):
        self.host = host
        self.port = port
        self.client = HttpMethods.HttpClient(session=session)
    
    
    def getAccessTokenforDevice(self):
        """
        getAccessTokenforDevice Description
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/cloudservices/accesstoken"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getAzureToken(self, bodyParameter):
        """
        Get Azure token
        
        Parameters:
        bodyParameter:	Description
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/cloudservices/authtoken"
        response = self.client.apiCall(HttpMethods.POST, endpoint, bodyParameter)
        return response


    def connect(self):
        """
        Telemetry Opt In
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/cloudservices/connect"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getCloudCreds(self):
        """
        Get cloud service credentials
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/cloudservices/credentials"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def addCloudCreds(self, bodyParameter):
        """
        Get cloud service settings
        
        Parameters:
        bodyParameter:	Description
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/cloudservices/credentials"
        response = self.client.apiCall(HttpMethods.POST, endpoint, bodyParameter)
        return response


    def getDeviceCode(self):
        """
        Get Azure device code
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/cloudservices/devicecode"
        response = self.client.apiCall(HttpMethods.POST, endpoint)
        return response


    def isStaging(self):
        """
        Check if testbed or production
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/cloudservices/staging"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getTelemetryState(self):
        """
        Get Telemetry state
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/cloudservices/telemetry"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def optIn(self, bodyParameter):
        """
        Telemetry Opt In
        
        Parameters:
        bodyParameter:	Description
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/cloudservices/telemetry/optin"
        response = self.client.apiCall(HttpMethods.PUT, endpoint, bodyParameter)
        return response


    def optOut(self, bodyParameter):
        """
        Telemetry Opt Out
        
        Parameters:
        bodyParameter:	Description
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/cloudservices/telemetry/optout"
        response = self.client.apiCall(HttpMethods.DELETE, endpoint, bodyParameter)
        return response


    def getCloudSettings(self):
        """
        Get cloud service settings
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/dca/cloudservices"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getOTP(self):
        """
        Get cloud service OTP value
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/dca/cloudservices/otp"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def updatetOTP(self, cloudserviceotpvalue):
        """
        Update cloud service OTP value
        
        Parameters:
        cloudserviceotpvalue:	Cloud service OTP value
        
        Returns
        response    (dict)
        
        
        """
        
        self.client.session.headers['Content-Type'] = "application/octet-stream"
        endpoint = f"https://{self.host}:{self.port}/dataservice/dca/cloudservices/otp"
        response = self.client.apiCall(HttpMethods.PUT, endpoint, cloudserviceotpvalue)
        return response


    def listEntityOwnerInfo(self):
        """
        List all entity ownership info
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/entityownership/list"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def entityOwnerInfo(self):
        """
        Entity ownership info grouped by buckets
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/entityownership/tree"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


