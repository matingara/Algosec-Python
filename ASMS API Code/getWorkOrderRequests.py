#! /Library/Frameworks/Python.framework/Versions/3.8/bin/python3
import requests, json, pprint
requests.packages.urllib3.disable_warnings()

def doAffLogin():
    headers = {'Content-type': 'application/json'}
    data = { 'username' : 'admin', 'password' : 'algosec', 'domain' : 0 }
    aFfRequestData = requests.post('https://192.168.0.164/FireFlow/api/authentication/authenticate', headers=headers, data=json.dumps(data), verify=False)
    contentDictionary = convertBytesToDictionary(aFfRequestData)
    sessionId, faSessionId, phpSessionId = extractSessionData(contentDictionary)
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

def getWorkOrderRequests(sessionId, maxWorkOrderNumber):  
    FireFlow_Cookie = 'FireFlow_Session=' + sessionId
    headers = {'Content-type': 'application/json', 'Cookie': FireFlow_Cookie}
    workOrderNumber = 0
    while workOrderNumber < maxWorkOrderNumber:
        workOrderNumber += 1
        workOrderRequestData = requests.get('https://192.168.0.164/FireFlow/api/change-requests/traffic/' + str(workOrderNumber) + '/work-order/implementation/result', headers=headers, verify=False)
        contentDictionary = convertBytesToDictionary(workOrderRequestData)
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(contentDictionary)
    return()

sessionId = doAffLogin()
requestData = getWorkOrderRequests(sessionId, 55)
exit(731)