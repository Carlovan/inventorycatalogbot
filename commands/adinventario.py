# -*- coding: utf-8 -*-
# Admin command: like /inventario but shows item ids

import database.items
from utils.filters import ItemFilter
from utils.inventory import get_messages
import utils

def run(bot, update, args):
	if utils.is_from_admin(update):
		filt = ItemFilter.from_list(args)
		items = database.items.get_multiple(filt)
		items.sort()
		messages = get_messages(items, head='Ci sono {} oggetti che corrispondono alla tua ricerca:'.format(len(items)), show_id=True)
		for msg in messages:
			update.message.reply_text(msg)
