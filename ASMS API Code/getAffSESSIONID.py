#! /Library/Frameworks/Python.framework/Versions/3.8/bin/python3
import requests, json, pprint
requests.packages.urllib3.disable_warnings() 

def doAffLogin():
    headers = {'Content-type': 'application/json'}
    data = { 'username' : 'admin', 'password' : 'algosec', 'domain' : 0 }
    aFfRequestData = requests.post('https://192.168.0.237/FireFlow/api/authentication/authenticate', headers=headers, data=json.dumps(data), verify=False)
    contentDictionary = convertBytesToDictionary(aFfRequestData)
    sessionId, faSessionId, phpSessionId = extractSessionData(contentDictionary)
    #pp = pprint.PrettyPrinter(indent=4)
    #pp.pprint(contentDictionary)
    return(sessionId)

def convertBytesToDictionary(requestData):
    contentBytes = requestData.content.decode('UTF-8')
    contentDictionary = json.loads(contentBytes)
    return(contentDictionary)

def extractSessionData(contentDictionary):
    sessionId = contentDictionary['data']['sessionId']
    faSessionId = contentDictionary['data']['faSessionId']
    phpSessionId = contentDictionary['data']['phpSessionId']
    return(sessionId, faSessionId, phpSessionId)

sessionId = doAffLogin()
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(sessionId)
exit(731)
