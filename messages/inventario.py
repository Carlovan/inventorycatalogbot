# -*- coding: utf-8 -*-
# Handles an inventory message

import utils
import utils.inventory as inventory
import database.items

def run(bot, update):
	if utils.is_fromIB(update):
		items = inventory.parse(update.message.text)
		items = list(filter(lambda x: database.items.get_single(x.name) is None, items))
		database.items.add(items)
		update.message.reply_text(f'Hai aggiunto {len(items)} oggetti.')
