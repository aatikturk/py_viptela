from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class MSLA(object):
    """
    MSLA API
    
    Implements GET POST DEL PUT methods for MSLA endpoints

    """

    def __init__(self, session, host, port):
        self.host = host
        self.port = port
        self.client = HttpMethods.HttpClient(session=session)
    
    
    def editDeviceWithLicense(self, license):
        """
        Update device subscription
        
        Parameters:
        license:	Subscription and license
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/msla/assignLicense"
        response = self.client.apiCall(HttpMethods.PUT, endpoint, license)
        return response


    def createDeviceWithLicense(self, license):
        """
        Create device subscription
        
        Parameters:
        license:	Subscription and license
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/msla/assignLicense"
        response = self.client.apiCall(HttpMethods.POST, endpoint, license)
        return response


    def getMSLADevices(self):
        """
        Retrieve devices subscription
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/msla/devices"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getDeviceDistributionOverview(self):
        """
        Get device distribution 
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/msla/devices/assignmentdistribution"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getLicenseandDeviceOverview(self):
        """
        Get license device overview 
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/msla/devices/licenseanddeviceoverviewtable"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getLicenseDistributionOverview(self):
        """
        Get license distribution 
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/msla/devices/licensedistribution"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getSubscriptionOverview(self):
        """
        Get subscription overview 
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/msla/devices/subscriptiondistribution"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getSubscriptions(self, payload):
        """
        Retrieve MSLA subscription/licenses
        
        Parameters:
        payload:	Request Payload
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/msla/licenses/subscription"
        response = self.client.apiCall(HttpMethods.POST, endpoint, payload)
        return response


    def syncLicenses(self, synclicense):
        """
        Retrieve MSLA subscription/licenses
        
        Parameters:
        synclicense:	Sync license
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/msla/licenses/sync"
        response = self.client.apiCall(HttpMethods.POST, endpoint, synclicense)
        return response


    def getlicensedDeviceCount(self):
        """
        get license and device count
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/msla/monitoring/licensedDeviceCount"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getLicensedDistributionDetails(self):
        """
        get license and device count
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/msla/monitoring/licensedDistributionDetails"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getpackagingDistributionDetails(self):
        """
        get packaging distribution details
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/msla/monitoring/packagingDistributionDetails"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getSubscriptions(self):
        """
        Retrieve subscriptions
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/msla/subscriptions"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getAllTemplate(self):
        """
        Retrieve all MSLA template
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/msla/template"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getSubscriptions(self, payload):
        """
        Retrieve MSLA subscription/licenses
        
        Parameters:
        payload:	Request Payload
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/msla/template/licenses"
        response = self.client.apiCall(HttpMethods.POST, endpoint, payload)
        return response


    def getSubscriptions(self, payload):
        """
        Retrieve MSLA subscription/licenses
        
        Parameters:
        payload:	Request Payload
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/msla/va/License"
        response = self.client.apiCall(HttpMethods.POST, endpoint, payload)
        return response


