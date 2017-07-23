# This module is just a fancy way to get settings from file and/or environment variables

import json

with open('settings.json', 'r') as sf:
	_data = json.loads(sf.read())

token = _data.get('token')
database_url = _data.get('database_url')
webhook = _data.get('webhook', None)
bot = None
changelog = 'Benvenuto nel catalogo!'
try:
	with open('changelog.txt', 'r') as cf:
		changelog += '\n' + cf.read()
except:
	pass
