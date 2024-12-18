import http
import json

def send_sms(mobile:str,templateid:int,parameters:dict,x_api_key:str):
    conn = http.client.HTTPSConnection("api.sms.ir")
    payload = json.dumps({
        "mobile": f'{mobile}',
        "templateId": templateid,
        "parameters": [parameters]
    })

    headers = {
        'Content-Type': 'application/json',
        'Accept': 'text/plain',
        'X-API-KEY': f"{x_api_key}"
    }
    conn.request("POST", "/v1/send/verify", payload, headers)
    res = conn.getresponse()
    data = res.read()
    data.decode("utf-8")