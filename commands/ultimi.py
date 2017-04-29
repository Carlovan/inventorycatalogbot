# -*- coding: utf-8 -*-
# This command returns last 10 items added

import database.items
import utils.inventory

def run(bot, update):
	inv = database.items.get_last(10)
	messages = inv.get_messages(head='Gli ultimi oggetti inseriti nel catalogo:')
	for msg in messages:
		update.message.reply_text(msg)
