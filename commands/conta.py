# -*- coding: utf-8 -*-
import database.items
from utils.filters import ItemFilter

pass_args = True

def run(bot, update, args):
	filt = ItemFilter.from_list(args)
	count = database.items.count(filt)
	update.message.reply_text('Ci sono {} oggetti che corrispondono alla tua ricerca.'.format(count))
