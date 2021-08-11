#! /Library/Frameworks/Python.framework/Versions/3.8/bin/python3
import requests, json

#headers = {'Content-type': 'application/json', 'accept': 'application/json;charset=UTF-8'}
headers = {'Content-type': 'application/json'}
#headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
# "accept: application/json;charset=UTF-8" -H "Content-Type: application/json"

data = { 'username' : 'admin', 'password' : 'algosec', 'domain': '' }
djd = json.dumps(data)
print(djd)
r = requests.post('https://192.168.0.237/FireFlow/api/authentication/authenticate/', headers=headers, data=json.dumps(data), verify=False)
#r = requests.post('https://192.168.0.237/FireFlow/api/authentication/authenticate/', headers=headers, data={ 'username' : 'admin', 'password' : 'algosec', 'domain': 0 }, verify=False)
session = requests.Session()
#token = json.loads(r.text)['session']
#token = json.loads(r.text)
print('r.text', r.text)
print('r: ', r)
print('STATUS CODE: ', r.status_code)
print('HEADERS: ', r.headers)
print('CONTENT: ', r.content)
print('C1: ', session.cookies, 'C2: ', r.cookies)
print('response.json is next')
r.json
