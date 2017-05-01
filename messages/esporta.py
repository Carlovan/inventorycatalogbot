# -*- coding: utf-8 -*-
# Handles an esporta message

import utils.inventory
import utils.user
import os
import time
import re

def run(bot, update):
	if utils.is_from_ib(update):
		user = utils.user.User.from_telegram(update.message.from_user)
		doc = bot.getFile(update.message.document.file_id)
		filename = str(time.time()) + '.txt'
		doc.download(filename)
		with open(filename, 'r') as ff:
			content = ff.read()
		os.remove(filename)
		content = re.sub(r'[^\S\n]+', ' ', content) # Replace any group of consecutive blanks (except newline) with a single whitespace
		content = re.sub(r'^(\d)+x +(.+)$', r'- \2 x\1', content, flags=re.MULTILINE) # makes every lline in the same format as the command /inventario
		inv = utils.inventory.Inventory.parse(content, user)
		count = utils.inventory.received(inv)
		update.message.reply_text(f'Hai aggiunto {count} oggetti.')
