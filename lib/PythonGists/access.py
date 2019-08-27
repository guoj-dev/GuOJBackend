GITHUB_API = 'https://api.github.com'


import requests
import getpass
import json
try:
    from .generateRandomNote import noteGen
except:
    from generateRandomNote import noteGen

def main(username,password):
    username = username
    password = password
    note=noteGen()
    url =GITHUB_API+ '/authorizations'
    payload = {"scopes":["gist"]}
    if note:
        payload['note'] = note
    res = requests.post(
        url,
        auth = (username, password),
        data = json.dumps(payload),
        )
    j = json.loads(res.text)
    if res.status_code >= 400:
        msg = j.get('message', 'UNDEFINED ERROR (no error description from server)')
        print(j)
        print ('ERROR: %s' % msg)
        return None
        
    token = j['token']

    return token

if __name__ == '__main__':
    username=input('username: ')
    password=getpass.getpass('password: ')
    main(username,password)