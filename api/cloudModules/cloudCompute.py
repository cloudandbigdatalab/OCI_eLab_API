import api.configuration.globalVars as globalVars
import requests
import json

def bootVM(token_id, name, imageid):
    #Replaces {0} from config file with the appropriate tenant id
    url2 = globalVars.computeURL.format(globalVars.tenant_id) 

    with open('cfgb64.sh', 'r') as configfile:
        config_b64 = configfile.read()

    print config_b64

    body = {"server": 
                {"name": name,
                 "imageRef": imageid,
                 "flavorRef": "1",
                 "networks":[{"uuid":"ed850e35-090c-4a5a-bea9-8b83dce481f7"}],
                 "user_data":config_b64
                 }
            }

    my_headers = {"X-Auth-Token": token_id}

    json_body = json.dumps(body)

    r = requests.post(url2, json_body, headers=my_headers)
    print json.dumps(r.json(), indent=4)
    return r.json()['server']['id']

def deleteVM(token_id, server_id):
    url = globalVars.computeURL.format(globalVars.tenant_id) + '/' + server_id

    my_headers = {"X-Auth-Token": token_id}

    r = requests.delete(url, headers=my_headers)
    print r

def queryVM(token_id, server_id):
    url = globalVars.computeURL.format(globalVars.tenant_id) + '/' + server_id

    my_headers = {"X-Auth-Token": token_id}

    r = requests.get(url, headers=my_headers)
    
    print json.dumps(r.json(), indent=4)

    if(r.json()['server']['addresses']['internal'][0]['version'] == 6):
        print r.json()['server']['addresses']['internal'][1]['addr']
    else:
        print r.json()['server']['addresses']['internal'][0]['addr']

    return r

def rebuildVM(token_id, server_id, image_id, name):
    url = globalVars.computeURL.format(globalVars.tenant_id) + '/' + server_id + '/action'

    body = {"rebuild":
                {"imageRef" : image_id,
                 "name" : name}}

    my_headers = {"X-Auth-Token": token_id}
    json_body = json.dumps(body)

    r = requests.post(url, json_body, headers=my_headers)
    return r
