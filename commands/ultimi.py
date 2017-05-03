# -*- coding: utf-8 -*-
# This command returns last 10 items added

import database.items
import utils.inventory

pass_args = False

def run(bot, update):
	dbitems = database.items.DbItems()
	inv = dbitems.get_last(10)
	messages = inv.get_messages(head='Gli ultimi oggetti inseriti nel catalogo:')
	for msg in messages:
		update.message.reply_text(msg)
