# -*- coding: utf-8 -*-
# Admin command to delete an item

import database.items
import utils

def run(bot, update, args):
	if utils.is_from_admin(update):
		if not all(map(str.isdigit, args)):
			update.message.reply_text('Specifica gli id degli item da eliminare')
		else:
			for itemid in args:
				itemid = int(itemid)
				database.items.delete(itemid)
			update.message.reply_text('Fatto.')
