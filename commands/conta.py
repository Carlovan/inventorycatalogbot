# -*- coding: utf-8 -*-
import database.items
from utils.filters import ItemFilter

pass_args = True

def run(bot, update, args):
	dbitems = database.items.DbItems()
	filt = ItemFilter.from_list(args)
	count = dbitems.count(filt)
	update.message.reply_text('Ci sono {} oggetti che corrispondono alla tua ricerca.'.format(count))
