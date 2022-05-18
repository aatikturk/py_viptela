from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class Processor(object):
    """
    Monitoring - Stats Processing API
    
    Implements GET POST DEL PUT methods for StatsProcessing endpoints

    """

    def __init__(self, session, host, port):
        self.client = HttpMethods.HttpClient(session=session)
        self.host = host
        self.port = port
    
    
    def getStatisticType(self):
        """
        Get statistics types
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/statistics"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def startStatsCollection(self):
        """
        Start stats collect
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/statistics/collect"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def generateStatsCollectThreadReport(self):
        """
        Get stats collect thread report
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/statistics/collect/thread/status"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def resetStatsCollection(self, processQueue):
        """
        Reset stats collect thread report
        
        Parameters:
        processQueue	 (integer):	Process queue
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/statistics/collection/reset/{processQueue}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def enableStatsDemo(self, enable):
        """
        Enable statistic demo mode
        
        Parameters:
        enable	 (boolean):	Demo mode flag
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/statistics/demomode?enable={enable}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def processStatsData(self):
        """
        Process stats data
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/statistics/process"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getStatsProcessingCounters(self):
        """
        Get statistics processing counters
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/statistics/process/counters"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getStatsProcessReport(self, processQueue):
        """
        Get stats process report
        
        Parameters:
        processQueue	 (integer):	Process queue
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/statistics/process/status?processQueue={processQueue}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getStatsProcessThreadReport(self):
        """
        Get stats process thread report
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/statistics/process/thread/status"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


