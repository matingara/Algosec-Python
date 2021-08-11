#! /Library/Frameworks/Python.framework/Versions/3.8/bin/python3
import requests, json

r = requests.get('https://192.168.0.237/FireFlow/api/templates/', verify=False)
session = requests.Session()

print('r.text', r.text)
print('r: ', r)
print('STATUS CODE: ', r.status_code)
print('HEADERS: ', r.headers)
print('CONTENT: ', r.content)
print('C1: ', session.cookies, 'C2: ', r.cookies)