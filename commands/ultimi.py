# -*- coding: utf-8 -*-
# This command returns last 10 items added

import database.items
import utils.inventory
from utils.filters import ItemFilter

pass_args = True

def run(bot, update, args):
	dbitems = database.items.DbItems()
	count = 10
	if len(args) >= 1 and args[0].isdigit():
		count = int(args[0])
		args = args[1:]
	filt = ItemFilter.from_list(args)
	inv = dbitems.get_last(count, filt)
	messages = inv.get_messages(head='Gli ultimi oggetti inseriti nel catalogo che corrispodono alla tua ricerca:')
	for msg in messages:
		update.message.reply_text(msg)
