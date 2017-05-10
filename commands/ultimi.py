# -*- coding: utf-8 -*-
# This command returns last 10 items added

import database.items
import utils.inventory

pass_args = True

def run(bot, update, args):
	dbitems = database.items.DbItems()
	count = 10
	if len(args) == 1 and args[0].isdigit():
		count = int(args[0])
	inv = dbitems.get_last(count)
	messages = inv.get_messages(head='Gli ultimi oggetti inseriti nel catalogo:')
	for msg in messages:
		update.message.reply_text(msg)
