# -*- coding: utf-8  -*-

import utils
import utils.item
import database.items

pass_args = True

def run(bot, update, args):
	if utils.is_from_admin(update):
		if len(args) > 2 and args[0].isdigit():
			dbitems = database.items.DbItems()
			itemdb = dbitems.get_single_by_id(int(args[0]))
			if itemdb is None:
				update.message.reply_text('Item with id {} not found'.format(int(args[0])))
				return
			else:
				try:
					itemuser = utils.item.Item.from_string(' '.join(args[1:]))
					itemuser.itemid = itemdb.itemid
					dbitems.update(itemuser)
				except Exception as ex:
					update.message.reply_text('You gave me an invalid item! :(')
					return
		else:
			update.message.reply_text('Usage: <code>/adupdate itemid item-string</code>', parse_mode='HTML')
			return
		update.message.reply_text('Updated')
