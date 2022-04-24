from query_builder import Builder
import HttpMethods

class Logging(object):
    """
    Utility - Logging API
    
    Implements GET POST DEL PUT methods for Logging endpoints

    """

    def __init__(self, session, host, port):
        self.host = host
        self.port = port
        self.client = HttpMethods.HttpClient(session=session)
    
    
    def listLogFileDetails(self):
        """
        Lists content of log file. This API accepts content type as text/plain. It is mandatory to provide response content type.  Any other content type would result in empty response.
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/util/logfile/appserver"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def listVManageServerLogLastNLines(self, lines):
        """
        List last N lines of log file. This API accepts content type as text/plain. It is mandatory to provide response content type.  Any other content type would result in empty response.
        
        Parameters:
        lines	 (integer):	Number of lines
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/util/logfile/appserver/lastnlines?lines={lines}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def debugLog(self, bodyParameter):
        """
        Test whether logging works
        
        Parameters:
        bodyParameter:	Description
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/util/logging/debuglog"
        response = self.client.apiCall(HttpMethods.POST, endpoint, bodyParameter)
        return response


    def setLogLevel(self, bodyParameter):
        """
        Set log level for logger
        
        Parameters:
        bodyParameter:	Description
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/util/logging/level"
        response = self.client.apiCall(HttpMethods.POST, endpoint, bodyParameter)
        return response


    def listLoggers(self):
        """
        List loggers
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/util/logging/loggers"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


