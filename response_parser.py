import json

class Parser(object):
    def __init__(self) -> None:
        pass

    def parseResponse(self, response):
        try:
            raw_data = json.loads(response)
        except:
            raw_data = {'error':"could not parse response"}
        if 'data' in raw_data:
            parsed_data = raw_data['data']
        else:
            parsed_data = raw_data
        return parsed_data