import globalVars
import requests
import json

def bootVM(token_id):
    url2 = globalVars.computeURL.format(globalVars.tenant_id) #Replaces {0} from config file with the appropriate tenant id

    body = {"server": 
                {"name": "server-test",
                 "imageRef": "eec1fa2e-a8ba-4725-ab6c-2c65acb958fc",
                 "flavorRef": "1"}}

    my_headers = {"X-Auth-Token": token_id}

    json_body = json.dumps(body)

    r = requests.post(url2, json_body, headers=my_headers)
    print r
