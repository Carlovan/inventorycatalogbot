# -*- coding: utf-8 -*-
# Handles an inventory message

import utils
import utils.inventory as inventory
import database

def run(bot, update):
	if utils.is_fromIB(update):
		items = inventory.parse(update.message.text)
		items = list(filter(lambda x: database.get_item(x.name) is None, items))
		database.add_items(items)
		update.message.reply_text(f'Hai aggiunto {len(items)} oggetti.')
