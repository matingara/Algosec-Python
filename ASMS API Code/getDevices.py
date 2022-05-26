#! /Library/Frameworks/Python.framework/Versions/3.8/bin/python3
import requests, json, pprint
requests.packages.urllib3.disable_warnings() 

def doAfaLogin():
    headers = {'Content-type': 'application/json'}
    data = { 'username' : 'admin', 'password' : 'algosec', 'domain' : 0 }
    requestData = requests.post('https://192.168.0.237/fa/server/connection/login', headers=headers, data=json.dumps(data), verify=False)
    contentBytes = requestData.content.decode('UTF-8')
    contentDictionaries = json.loads(contentBytes)
    phpSessionId = contentDictionaries['SessionID']
    return(phpSessionId)

def getAllDeviceDetails(phpSessionId):
    aFaCookie = 'PHPSESSID=' + phpSessionId
    headers = {'Content-type': 'application/json', 'Cookie': aFaCookie}
    requestData = requests.get('https://192.168.0.237/afa/api/v1/devices', headers=headers, verify=False)
    contentBytes = requestData.content.decode('UTF-8')
    contentDictionaries = json.loads(contentBytes)
    return(contentDictionaries)

phpSessionId = doAfaLogin()
contentDictionaries = getAllDeviceDetails(phpSessionId)
for dictionary in contentDictionaries:
    print(dictionary['brand'], 'firewall exists with name', dictionary['name'], 'and display name', dictionary['display_name'])

exit(731)
