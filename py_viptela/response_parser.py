import json

ERROR_CODES = {
    400: "Bad Request",
    403: "Forbidden",
    500: "Internal Server Error",
    800: "Emtpy Response",
    801: "Invalid Json Data",
    802: "Empty Data field in Response"
}

def parse_response(response):
    status_code = response.status_code
    if status_code == 200:
        if response.text != '':
            # check for invalid Json data
            try:
                raw_data = json.loads(response.text)
            except json.JSONDecodeError:
                return {"failed":True, "code": 801, "error":ERROR_CODES[801], "msg":response.text}
            else:
                if type(raw_data) == list:
                    return {"failed":False, "code": status_code, "error":"", "msg":raw_data} 
                elif raw_data.get("data"):
                    return {"failed":False, "code": status_code, "error":"", "msg":raw_data} 
                else:
                    return {"failed":True, "code": 802, "error":ERROR_CODES[802], "msg":response.text}
        else:
            # if response is an empty string, return it
            return {"failed":True, "code": 800, "error":ERROR_CODES[800], "msg":response.text}
    else:
        return {"failed":True, "code":status_code, "error":ERROR_CODES[status_code], "msg":response.text}