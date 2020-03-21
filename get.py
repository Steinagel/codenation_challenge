import requests
import json


# _test   = "http://127.0.0.1:5500/test.json"

url     = "https://api.codenation.dev/v1/challenge/dev-ps" 
token   = "2318ff2032de236e61faa160f2b982cdc3f109a7"

def request_json(url, filename="answer"):
    '''
    Codenation challenge
    request_json returns True for success, 
     or False if fail
    '''
    response = requests.get(url)
    
    if response.status_code == 200:
        data = json.loads(response.text)
        with open(f'{filename}.json', 'w+') as f:
            json.dump(data, f)
    else:
        return False
        
    return True

# Just to avoid exec script on terminal unintentionally :)
# if __name__=='__main__':
#     if request_json(f'{url}/generate-data?token={token}'):
#         print("success")