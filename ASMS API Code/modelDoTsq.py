#! /Library/Frameworks/Python.framework/Versions/3.8/bin/python3
import requests, json, pprint
requests.packages.urllib3.disable_warnings() 

def doAfaLogin():
    headers = {'Content-type': 'application/json'}
    data = { 'username' : 'c839024', 'password' : 'Idreamalgosec1i#', 'domain' : 0 }
    aFaRequestData = requests.post('https://lxapp6420.dc.corp.telstra.com/fa/server/connection/login', headers=headers, data=json.dumps(data), verify=False)
    contentDictionary = convertBytesToDictionary(aFaRequestData)
    phpSessionId = contentDictionary['SessionID']
    return(phpSessionId)

def convertBytesToDictionary(requestData):
    contentBytes = requestData.content.decode('UTF-8')
    contentDictionary = json.loads(contentBytes)
    return(contentDictionary)

def doTrafficSimulationQuery(phpSessionId):
    aFaCookie = 'PHPSESSID=' + phpSessionId
    headers = {'Content-type': 'application/json', 'Cookie': aFaCookie}
    data = {'queryInput': [{'application': ['any'],'destination': ['172.16.1.30'],\
            'service': ['tcp/7171'],'source': ['172.16.0.30'],'user': ['any']}],\
            'queryTarget': 'ALL_FIREWALLS','includeDevicesPaths' : 'true', 'includeRulesZones' : 'true'}
    trafficSimulationQueryRequestData = requests.post('https://lxapp6420.dc.corp.telstra.com/afa/api/v1/query', headers=headers, data=json.dumps(data), verify=False)
    contentDictionary = convertBytesToDictionary(trafficSimulationQueryRequestData)
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(contentDictionary)
    return(contentDictionary)

def getRuleData(contentDictionary, phpSessionId):
    ruleName = contentDictionary['queryResult'][0]['queryItem'][0]['rules'][0]['ruleName']
    rule_id = contentDictionary['queryResult'][0]['queryItem'][0]['rules'][0]['rule_id']
    deviceName = contentDictionary['queryResult'][0]['queryItem'][0]['deviceName']
    print(type(deviceName))
    aFaCookie = 'PHPSESSID=' + phpSessionId
    headers = {'Content-type': 'application/json', 'Cookie': aFaCookie}
    data = {'columnId': 'Application', 'deviceId': deviceName, 'rule_id': rule_id }
    getRuleDocumentationRequestData = requests.get('https://lxapp6420.dc.corp.telstra.com/afa/api/v1/rule/ruleDocumentation', headers=headers, data=json.dumps(data), verify=False)
    contentDictionary = convertBytesToDictionary(getRuleDocumentationRequestData)
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(contentDictionary)
    return()

phpSessionId = doAfaLogin()
contentDictionary = doTrafficSimulationQuery(phpSessionId)
getRuleData(contentDictionary, phpSessionId)

exit(731)