# -*- coding: utf-8 -*-
import database
from utils.filters import ItemFilter

def run(bot, update, args):
	filters = ItemFilter.from_list(args)
	count = database.count_items(filters)
	update.message.reply_text('Ci sono {} oggetti che corrispondono alla tua ricerca.'.format(count))
