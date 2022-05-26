#! /Library/Frameworks/Python.framework/Versions/3.8/bin/python3
import getAfaPHPSESSIONID
import requests, json, pprint
requests.packages.urllib3.disable_warnings() 

def convertBytesToDictionary(requestData):
    contentBytes = requestData.content.decode('UTF-8')
    contentDictionary = json.loads(contentBytes)
    return(contentDictionary)

def getAllRulesOnFirewall(phpSessionId):
    headers = {
        'accept': '*/*',
    }
    params = (
        ('entity', '192.168.0.224'),
        ('entityType', 'FIREWALL'),
    )
    cookies = {
        'PHPSESSID': phpSessionId
    }
    getRulesData = requests.get('https://192.168.0.237/afa/api/v1/rules', headers=headers, params=params, cookies=cookies, verify=False)
    contentDictionary = convertBytesToDictionary(getRulesData)
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(contentDictionary)
    return()

phpSessionId = getAfaPHPSESSIONID.doAfaLogin()
getAllRulesOnFirewall(phpSessionId)

exit(731)