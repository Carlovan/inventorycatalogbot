# This module is just a fancy way to get settings from file and/or environment variables

import os

token = os.getenv('TOKEN')
database_url = os.getenv('DATABASE_URL')
webhook = os.getenv('WEBHOOK', None)
bot = None
changelog = 'Benvenuto nel catalogo!'
try:
	with open('changelog.txt', 'r') as cf:
		changelog += '\n' + cf.read()
except:
	pass
