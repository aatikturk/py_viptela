import json
from json.decoder import JSONDecodeError

class Parser(object):
    @staticmethod
    def parseResponse(response):
        if response.text != '':
            # check for invalid Json data
            try:
                raw_data = json.loads(response.text)
            except JSONDecodeError:
                error = {'error':"Invalid Json Data"}
                return error
            # check raw_data for key "data".
            # if the it doesn't exist, return raw_data
            if 'data' in raw_data:
                parsed_data = raw_data['data']
            else:
                parsed_data = raw_data
            return parsed_data
        else:
            # if response is an empty string, return it
            return response.text
