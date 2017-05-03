# -*- coding: utf-8 -*-
# Admin command: like /inventario but shows item ids

import database.items
from utils.filters import ItemFilter
import utils

pass_args = True

def run(bot, update, args):
	if utils.is_from_admin(update):
		dbitems = database.items.DbItems()
		filt = ItemFilter.from_list(args)
		inv = dbitems.get_multiple(filt)
		inv.items.sort()
		messages = inv.get_messages(head='Ci sono {} oggetti che corrispondono alla tua ricerca:'.format(len(inv.items)), show_id=True)
		for msg in messages:
			update.message.reply_text(msg)
