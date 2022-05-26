#! /Library/Frameworks/Python.framework/Versions/3.8/bin/python3
import requests, json, pprint
requests.packages.urllib3.disable_warnings() 

def doAfaLogin(asmsName):
    headers = {
        'Content-type': 'application/json'
        }
    data = {
        'username' : 'admin',
        'password' : 'algosec',
        'domain' : 0
        }
    URL = 'https://' + asmsName + '/fa/server/connection/login'
    requestData = requests.post(url=URL , headers=headers, data=json.dumps(data), verify=False)
    contentBytes = requestData.content.decode('UTF-8')
    contentDictionaries = json.loads(contentBytes)
    phpSessionId = contentDictionaries['SessionID']
    return(phpSessionId)

def getAllDeviceDetails(phpSessionId):
    aFaCookie = 'PHPSESSID=' + phpSessionId
    headers = {
        'Content-type': 'application/json',
        'Cookie': aFaCookie
        }
    URL = 'https://' + asmsName + '/afa/api/v1/devices'
    requestData = requests.get(url=URL, headers=headers, verify=False)
    contentBytes = requestData.content.decode('UTF-8')
    contentDictionaries = json.loads(contentBytes)
    return(contentDictionaries)

def getAllRulesOnFirewall(entity):
    headers = {
        'accept': '*/*',
    }
    params = (
        ('entity', entity),
        ('entityType', 'FIREWALL'),
    )
    cookies = {
        'PHPSESSID': phpSessionId
    }
    requestData = requests.get('https://192.168.0.237/afa/api/v1/rules', headers=headers, params=params, cookies=cookies, verify=False)
    contentBytes = requestData.content.decode('UTF-8')
    contentDictionaries = json.loads(contentBytes)
#    pp = pprint.PrettyPrinter(indent=4)
#    pp.pprint(contentDictionaries)
    return(contentDictionaries)

asmsName = input('Enter name of the ASMS system [192.168.0.237]: ')
if not asmsName:
    asmsName = '192.168.0.237'
phpSessionId = doAfaLogin(asmsName)
contentDictionaries = getAllDeviceDetails(phpSessionId)
firewallList = []
for dictionary in contentDictionaries:
    print(dictionary['brand'], 'firewall exists with name', dictionary['name'], 'and display name', dictionary['display_name'])
    firewallList.append(dictionary['display_name'])

print('firewallList', firewallList)
for firewall in firewallList:
    ruleList = getAllRulesOnFirewall(firewall)
    print('The firewall device', firewall, 'has', len(ruleList[0]['rules']), 'rules configured')

print('Done processing firewalls')

exit(731)
