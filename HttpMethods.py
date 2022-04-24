from response_parser import Parser

# CONSTANTS
GET = "GET"
POST = "POST"
PUT = "PUT"
DELETE = "DELETE"

class HttpClient(object):
    
    """
    TODO: methods for this class will be implemented lastResort
    """
    def __init__(self, session):
        self.session = session
        self.parser = Parser()

    def apiCall(self, method, url, body=None):
        if method == 'GET':
            result = self.httpGet(url=url)
        if method == 'POST':
            result = self.httpPost(url=url, body=body)
        if method == 'PUT':
            result = self.httpPut(url=url, body=body)
        if method == 'DELETE':
            result = self.httpDel(url=url, body=body)
        return result

        
    def httpGet(self, url):
        try:
            response = self.session.get(url)
            data = self.parser.parseResponse(response.text)
            return data
        except:
            return {'error': 'bad request'}

    def httpPost(self, url, body=None):
        try:
            response = self.session.post(url, body)
            data = self.parser.parseResponse(response.text)
            return data
        except:
            return {'error': 'bad request'}

    def httpPut(self, url, body=None):
        try:
            response = self.session.put(url, body)
            data = self.parser.parseResponse(response.text)
            return data
        except:
            return {'error': 'bad request'}

    def httpDel(self, url, body=None):
        try:
            response = self.session.delete(url)
            data = self.parser.parseResponse(response.text)
            return data
        except:
            return {'error': 'bad request'}