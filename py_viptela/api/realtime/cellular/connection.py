from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class Connection(object):
    """
    Real-Time Monitoring - Cellular EIOLTE Connection Service API
    
    Implements GET POST DEL PUT methods for CellularEIOLTEConnectionService endpoints

    """

    def __init__(vmanage, session, host, port):
        vmanage.host = host
        vmanage.port = port
        vmanage.client = HttpMethods.HttpClient(session=session)
    
    
    def getConnInfo(vmanage, deviceId):
        """
        Get cellular connection info from device
        
        Parameters:
        deviceId	 (string):	Device Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/cellularEiolte/connections?deviceId={deviceId}"
        response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getRadioInfo(vmanage, deviceId):
        """
        Get cellular radio info from device
        
        Parameters:
        deviceId	 (string):	Device Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/cellularEiolte/radio?deviceId={deviceId}"
        response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
        return response


