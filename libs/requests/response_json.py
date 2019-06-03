#!/usr/bin/python3

import requests

login='mkhuthir'

response = requests.get('https://api.github.com/users/'+login)

data = response.json()

print('name:\t\t',data['name'])
print('location:\t',data['location'])
print('bio:\t\t',data['bio'])


