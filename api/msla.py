from query_builder import Builder
import HttpMethods

class MSLA(object):
    """
    MSLA API
    
    Implements GET POST DEL PUT methods for MSLA endpoints

    """

    def __init__(self, session, host, port):
        self.host = host
        self.port = port
        self.client = HttpMethods.HttpClient(session=session)
    
    
    def editDeviceWithLicense(self, subscriptionandlicense):
        """
        Update device subscription
        
        Parameters:
        subscriptionandlicense:	Subscription and license
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/msla/assignLicense"
        response = self.client.apiCall(HttpMethods.PUT, endpoint, subscriptionandlicense)
        return response


    def createDeviceWithLicense(self, subscriptionandlicense):
        """
        Create device subscription
        
        Parameters:
        subscriptionandlicense:	Subscription and license
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/msla/assignLicense"
        response = self.client.apiCall(HttpMethods.POST, endpoint, subscriptionandlicense)
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


    def getSubscriptions(self, bodyParameter):
        """
        Retrieve MSLA subscription/licenses
        
        Parameters:
        bodyParameter:	Description
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/msla/licenses/subscription"
        response = self.client.apiCall(HttpMethods.POST, endpoint, bodyParameter)
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


    def getSubscriptions(self, bodyParameter):
        """
        Retrieve MSLA subscription/licenses
        
        Parameters:
        bodyParameter:	Description
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/msla/template/licenses"
        response = self.client.apiCall(HttpMethods.POST, endpoint, bodyParameter)
        return response


    def getSubscriptions(self, bodyParameter):
        """
        Retrieve MSLA subscription/licenses
        
        Parameters:
        bodyParameter:	Description
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/msla/va/License"
        response = self.client.apiCall(HttpMethods.POST, endpoint, bodyParameter)
        return response


