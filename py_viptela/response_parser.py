import json

class Parser(object):
    @staticmethod
    def parseResponse(response):
        try:
            raw_data = json.loads(response.text)
        except:
            raw_data = {'error':"could not parse response"}
        if 'data' in raw_data:
            parsed_data = raw_data['data']
        else:
            parsed_data = raw_data
        return parsed_data