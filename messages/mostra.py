# -*- coding: utf-8 -*-
# Handles a /mostra forwarded message

import utils.inventory

def run(bot, update, groupdict):
	if utils.is_from_ib(update):
		items = [utils.item.Item.from_string(groupdict['item'])]
		count = utils.inventory.add(items)
		update.message.reply_text(f'Hai aggiunto {count} oggetti.')
