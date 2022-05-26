#! /Library/Frameworks/Python.framework/Versions/3.8/bin/python3
#import requests
#
#params = (
#    ('entity', '192.168.0.224'),
#    ('entityType', 'FIREWALL'),
#)
#
#response = requests.get('https://192.168.0.237/afa/api/v1/rules', params=params, verify=False)
#print('response', response)
import requests

cookies = {
    'PHPSESSID': 'eu6uhughm9tsu39qiqc9ppd9i4',
}

headers = {
    'accept': '*/*',
}

params = (
    ('entity', '192.168.0.224'),
    ('entityType', 'FIREWALL'),
)

response = requests.get('https://192.168.0.237/afa/api/v1/rules', headers=headers, params=params, cookies=cookies, verify=False)
print('response', response)