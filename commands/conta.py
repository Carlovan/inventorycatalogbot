# -*- coding: utf-8 -*-
import database.items
from utils.filters import ItemFilter
import utils.item
import logging
logger = logging.getLogger(__name__)

pass_args = True

def run(bot, update, args):
	logger.info('User {} -> ({})'.format(update.message.from_user.username, ' '.join(args)))
	dbitems = database.items.DbItems()
	filt = ItemFilter.from_list(args)
	count = dbitems.count(filt)
	text = 'Ci sono {} oggetti che corrispondono alla tua ricerca'.format(count)
	if len(args) == 0:
		text += '\ndi cui:'
		for rar in utils.item._rarities:
			filt = ItemFilter(rarity=[rar])
			text += '\n- {} oggetti di rarità {}'.format(dbitems.count(filt), rar)
	update.message.reply_text(text)
