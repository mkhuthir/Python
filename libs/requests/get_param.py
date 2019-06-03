#!/usr/bin/python3

import requests

payload = {
	   'key1': 'value1',
	   'key2': 'value2'
	  }

r = requests.get('https://httpbin.org/get', params=payload)

print('\nURL:', r.url)
print('\nENCODING: ', r.encoding)
print('\nSTATUS_CODE: ', r.status_code)
print('\nHEADERS: ', r.headers)
print('\nTEXT: ', r.text)
print('\nCONTENT: ', r.content)
print('\nJSON: ', r.json)
