from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

def activateContainerOnRemoteHost(vmanage, containerName, url, hostIp, checksum):
    """
    Activate container on remote host
    
    Parameters:
    containerName	 (string):	Container name
	url	 (string):	Container image URL
	hostIp	 (string):	Container host IP
	checksum	 (string):	Container image checksum
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/container-manager/activate/{containerName}?url={url}&hostIp={hostIp}&checksum={checksum}"
    response = vmanage.client.apiCall(HttpMethods.POST, endpoint)
    return response
def deActivateContainer(vmanage, containerName, hostIp):
    """
    Deactivate container on remote host
    
    Parameters:
    containerName	 (string):	Container name
	hostIp	 (string):	Container host IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/container-manager/deactivate/{containerName}?hostIp={hostIp}"
    response = vmanage.client.apiCall(HttpMethods.POST, endpoint)
    return response
def doesValidImageExist(vmanage, containerName):
    """
    Get container image checksum
    
    Parameters:
    containerName	 (string):	Container name
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/container-manager/doesValidImageExist/{containerName}"
    response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
    return response
def getContainerInspectData(vmanage, containerName, hostIp):
    """
    Get container inspect data
    
    Parameters:
    containerName	 (string):	Container name
	hostIp	 (string):	Container host IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/container-manager/inspect/{containerName}?hostIp={hostIp}"
    response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
    return response
def getContainerSettings(vmanage, containerName, hostIp):
    """
    Get container settings
    
    Parameters:
    containerName	 (string):	Container name
	hostIp	 (string):	Container host IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/container-manager/settings/{containerName}?hostIp={hostIp}"
    response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
    return response
def getChecksum(vmanage):
    """
    Get container image checksum
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/sdavc/checksum"
    response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
    return response
def getCustomApp(vmanage):
    """
    Displays the user-defined applications
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/sdavc/customapps"
    response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
    return response
def activateContainer(vmanage, containertaskconfig, taskId):
    """
    Activate container
    
    Parameters:
    containertaskconfig:	Container task config
	taskId	 (string):	Task Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/sdavc/task/{taskId}"
    response = vmanage.client.apiCall(HttpMethods.POST, endpoint, containertaskconfig)
    return response
def testLoadBalancer(vmanage):
    """
    Test SD_AVC load balancer
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/sdavc/test"
    response = vmanage.client.apiCall(HttpMethods.POST, endpoint)
    return response
