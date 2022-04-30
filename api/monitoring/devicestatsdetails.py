from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class DeviceStatisticsDetails(object):
    """
    Monitoring - Device Statistics Details API
    
    Implements GET POST DEL PUT methods for DeviceStatisticsDetails endpoints

    """

    def __init__(self, session, host, port):
        self.client = HttpMethods.HttpClient(session=session)
        self.host = host
        self.port = port
    
    
    def getStatisticsType(self):
        """
        Get statistics types
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/data/device/statistics"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getActiveAlarms(self, scrollId, startDate, endDate, count, timeZone):
        """
        Get active alarms
        
        Parameters:
        scrollId	 (string):	SrollId
		startDate	 (string):	Start date
		endDate	 (string):	End date
		count	 (integer):	count
		timeZone	 (string):	Time zone
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/data/device/statistics/alarm/active?scrollId={scrollId}&startDate={startDate}&endDate={endDate}&count={count}&timeZone={timeZone}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getStatsData(self, state_data_type, scrollId, startDate, endDate, count, timeZone):
        """
        Get device statistics data
        
        Parameters:
        state_data_type	 (string):	State data type
		scrollId	 (string):	Scroll Id
		startDate	 (string):	Start date
		endDate	 (string):	End date
		Parameter Description
		timeZone	 (string):	Time zone
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/data/device/statistics/{state_data_type}?scrollId={scrollId}&startDate={startDate}&endDate={endDate}&count={count}&timeZone={timeZone}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getCountWithStateDataType(self, state_data_type, startDate, endDate, timeZone):
        """
        Get response count of a query
        
        Parameters:
        state_data_type	 (string):	State data type
		startDate	 (string):	Start date
		endDate	 (string):	End date
		timeZone	 (string):	Time zone
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/data/device/statistics/{state_data_type}/doccount?startDate={startDate}&endDate={endDate}&timeZone={timeZone}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getFieldsByType(self, state_data_type):
        """
        Get statistics fields and types
        
        Parameters:
        state_data_type	 (string):	State data type
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/data/device/statistics/{state_data_type}/fields"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


