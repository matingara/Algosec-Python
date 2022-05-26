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

def doTrafficSimulationQuery(phpSessionId):
    aFaCookie = 'PHPSESSID=' + phpSessionId
    headers = {'Content-type': 'application/json', 'Cookie': aFaCookie}
    data = {'queryInput': [{'application': ['any'],'destination': ['172.16.102.30'],\
            'service': ['tcp/7171'],'source': ['172.16.1.30'],'user': ['any']}],\
            'queryTarget': 'ALL_FIREWALLS','includeDevicesPaths' : 'true', 'includeRulesZones' : 'true'}
    trafficSimulationQueryRequestData = requests.post('https://192.168.0.237/afa/api/v1/query', headers=headers, data=json.dumps(data), verify=False)
    contentDictionary = convertBytesToDictionary(trafficSimulationQueryRequestData)
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(contentDictionary)
    return(contentDictionary)

def getRuleDataForTSQ(contentDictionary, phpSessionId):
    rule_id = contentDictionary['queryResult'][0]['queryItem'][0]['rules'][0]['rule_id']
    deviceName = contentDictionary['queryResult'][0]['queryItem'][0]['deviceName']
    cookies = {
        'PHPSESSID': phpSessionId
    }
    headers = {
        'accept': '*/*',
    }
    params = (
        ('columnId', 'DESCRIPTION'),
        ('deviceId', deviceName),
        ('ruleId', rule_id)
    )
    getRulesData = requests.get('https://192.168.0.237/afa/api/v1/rule/ruleDocumentation', headers=headers, params=params, cookies=cookies, verify=False)
    contentDictionary = convertBytesToDictionary(getRulesData)
    print('PART ONE CONTENT DICTIONARY')
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(contentDictionary)
    return()

def getAllRulesOnFirewall(contentDictionary, phpSessionId):
    print('STARTING PART TWO')
    cookies = {
        'PHPSESSID': phpSessionId
    }
    headers = {
        'accept': '*/*',
    }
    params = (
        ('entity', '192.168.0.224'),
        ('entityType', 'FIREWALL'),
    )
    getRulesData = requests.get('https://192.168.0.237/afa/api/v1/rules', headers=headers, params=params, cookies=cookies, verify=False)
    contentDictionary = convertBytesToDictionary(getRulesData)
    print('PART TWO CONTENT DICTIONARY')
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(contentDictionary)
    return()

#def getRuleData(contentDictionary, phpSessionId):
#    ruleName = contentDictionary['queryResult'][0]['queryItem'][0]['rules'][0]['ruleName']
#    rule_id = contentDictionary['queryResult'][0]['queryItem'][0]['rules'][0]['rule_id']
#    deviceName = contentDictionary['queryResult'][0]['queryItem'][0]['deviceName']
#    print(type(deviceName), deviceName)
#    aFaCookie = 'PHPSESSID=' + phpSessionId
#    headers = {'Content-type': 'application/json', 'Cookie': aFaCookie}
#    data = {'columnId': 'DESCRIPTION', 'deviceId': deviceName, 'ruleId': rule_id }
#    data = {'deviceId': deviceName, 'rule_id': rule_id }
#    print('headers', headers)
#    print('data', data)
#    getRuleDocumentationRequestData = requests.get('https://192.168.0.237/afa/api/v1/rule/ruleDocumentation', headers=headers, data=json.dumps(data), verify=False)
#    contentDictionary = convertBytesToDictionary(getRuleDocumentationRequestData)
#    pp = pprint.PrettyPrinter(indent=4)
#    pp.pprint(contentDictionary)
#    return()

phpSessionId = doAfaLogin()
contentDictionary = doTrafficSimulationQuery(phpSessionId)
getRuleDataForTSQ(contentDictionary, phpSessionId)

exit(731)