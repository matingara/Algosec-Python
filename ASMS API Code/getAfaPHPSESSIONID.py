#! /Library/Frameworks/Python.framework/Versions/3.8/bin/python3
import requests, json, pprint
requests.packages.urllib3.disable_warnings() 

def doAfaLogin():
    headers = {'Content-type': 'application/json'}
    data = { 'username' : 'admin', 'password' : 'algosec', 'domain' : 0 }
    aFaRequestData = requests.post('https://192.168.0.237/fa/server/connection/login', headers=headers, data=json.dumps(data), verify=False)
    contentDictionary = convertBytesToDictionary(aFaRequestData)
    phpSessionId = contentDictionary['SessionID']
    return(phpSessionId)

def convertBytesToDictionary(requestData):
    contentBytes = requestData.content.decode('UTF-8')
    contentDictionary = json.loads(contentBytes)
    return(contentDictionary)

phpSessionId = doAfaLogin()
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(phpSessionId)