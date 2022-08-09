from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class Network(object):
    """
    Real-Time Monitoring - Cellular EIOLTE Network Service API
    
    Implements GET POST DEL PUT methods for CellularEIOLTENetworkService endpoints

    """

    def __init__(vmanage, session, host, port):
        vmanage.host = host
        vmanage.port = port
        vmanage.client = HttpMethods.HttpClient(session=session)
    
    
    def getNetworkInfo(vmanage, deviceId):
        """
        Get cellular network  info from device
        
        Parameters:
        deviceId	 (string):	Device Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/cellularEiolte/network?deviceId={deviceId}"
        response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
        return response


