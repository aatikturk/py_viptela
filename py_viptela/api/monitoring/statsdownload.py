from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class Downloader(object):
    """
    Monitoring - Stats Download API
    
    Implements GET POST DEL PUT methods for StatsDownload endpoints

    """

    def __init__(vmanage, session, host, port):
        vmanage.client = HttpMethods.HttpClient(session=session)
        vmanage.host = host
        vmanage.port = port
    
    
    def fetchList(vmanage, processType):
        """
        fetchList Description
        
        Parameters:
        Parameter Description
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/statistics/download/{processType}/fetchvManageList"
        response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def download(vmanage, processType, fileType, queue, deviceIp, token, fileName):
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
        
        endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/statistics/download/{processType}/file/{fileType}/{queue}/{deviceIp}/{token}/{fileName}"
        response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def downloadList(vmanage, bodyParameter, processType):
        """
        Downloading list of stats file
        
        Parameters:
        bodyParameter:	Description
		processType	 (string):	Possible types are: remoteprocessing, dr
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/statistics/download/{processType}/filelist"
        response = vmanage.client.apiCall(HttpMethods.POST, endpoint, bodyParameter)
        return response


