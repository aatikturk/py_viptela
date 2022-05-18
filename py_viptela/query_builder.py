import json
import urllib

class Builder(object):
    
    @staticmethod
    def generateQuery(queryDict):
        return urllib.parse.quote_plus(json.dumps(queryDict))