# -*- coding: utf-8 -*-
# Handles an inventory message

import utils.inventory

def run(bot, update):
	if utils.is_fromIB(update):
		items = utils.inventory.parse(update.message.text)
		count = utils.inventory.add(items)
		update.message.reply_text(f'Hai aggiunto {count} oggetti.')
