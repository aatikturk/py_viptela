from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class CFM(object):
    """
    Real-Time Monitoring - CFM API
    
    Implements GET POST DEL PUT methods for CFM endpoints

    """

    def __init__(self, session, host, port):
        self.host = host
        self.port = port
        self.client = HttpMethods.HttpClient(session=session)
    
    
    def getMpDatabase(self, deviceId):
        """
        Get mp database from device
        
        Parameters:
        deviceId	 (string):	Device IP
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/cfm/mp/database?deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getMpLocalMep(self, domain, service, mepId, deviceId):
        """
        Get mp local mep from device
        
        Parameters:
        domain	 (string):	Domain Name
		service	 (string):	Service Name
		mepId	 (number):	MEP ID
		deviceId	 (string):	Device IP
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/cfm/mp/local/mep?domain={domain}&service={service}&mepId={mepId}&deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getMpLocalMip(self, level, port, svcInst, deviceId):
        """
        Get mp local mip from device
        
        Parameters:
        level	 (number):	Level
		port	 (string):	Port
		svcInst	 (number):	Service Instance
		deviceId	 (string):	Device IP
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/cfm/mp/local/mip?level={level}&port={port}&svcInst={svcInst}&deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getMpRemoteMep(self, domain, service, locMepId, remMepId, deviceId):
        """
        Get mp remote mep from device
        
        Parameters:
        domain	 (string):	Domain Name
		service	 (string):	Service Name
		locMepId	 (number):	Local MEP ID
		remMepId	 (number):	Remote MEP ID
		deviceId	 (string):	Device IP
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/cfm/mp/remotemep?domain={domain}&service={service}&locMepId={locMepId}&remMepId={remMepId}&deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


