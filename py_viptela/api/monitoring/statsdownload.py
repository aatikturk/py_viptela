from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class Downloader(object):
    """
    Monitoring - Stats Download API
    
    Implements GET POST DEL PUT methods for StatsDownload endpoints

    """

    def __init__(self, session, host, port):
        self.client = HttpMethods.HttpClient(session=session)
        self.host = host
        self.port = port
    
    
    def fetchList(self, processType):
        """
        fetchList Description
        
        Parameters:
        Parameter Description
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/statistics/download/{processType}/fetchvManageList"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def download(self, processType, fileType, queue, deviceIp, token, fileName):
        """
        Downloading stats file
        
        Parameters:
        processType	 (string):	Process type
		fileType	 (string):	File type
		queue	 (string):	Queue name
		deviceIp	 (string):	Device IP
		token	 (string):	Token
		fileName	 (string):	File name
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/statistics/download/{processType}/file/{fileType}/{queue}/{deviceIp}/{token}/{fileName}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def downloadList(self, bodyParameter, processType):
        """
        Downloading list of stats file
        
        Parameters:
        bodyParameter:	Description
		processType	 (string):	Possible types are: remoteprocessing, dr
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/statistics/download/{processType}/filelist"
        response = self.client.apiCall(HttpMethods.POST, endpoint, bodyParameter)
        return response


