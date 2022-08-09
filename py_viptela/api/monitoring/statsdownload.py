def fetchList(vmanage, processType):
    """
    fetchList Description
    
    Parameters:
    Parameter Description
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/statistics/download/{processType}/fetchvManageList"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
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
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
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
    response = vmanage.client.apiCall(vmanage.POST, endpoint, bodyParameter)
    return response
