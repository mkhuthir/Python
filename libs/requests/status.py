#!/usr/bin/python3

import requests
from requests.exceptions import HTTPError

urls = [
		'https://api.github.com',
		'https://api.github.com/invalid',
		'https://dog.ceo/api/breeds/image/random'
       ]

for url in urls:
	try:
		print("\ntrying: ",url)
		response = requests.get(url)
		# If the response was successful, no Exception will be raised
		response.raise_for_status()

	except HTTPError as http_err:
		# if HTTP error occurred
		print(f'HTTP error occurred: {http_err}')

	except Exception as err:
		# if any error other than above occurred
        print(f'Other error occurred: {err}')

	else:
		# if no error occurred
		print('Success!')
	
	

print("\nDone.\n")
