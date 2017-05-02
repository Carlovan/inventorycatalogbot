# -*- coding: utf-8 -*-
# Admin command to add an item manually

import utils

pass_args = True

def run(bot, update, args):
	if utils.is_from_admin(update):
		item = utils.item.Item.from_string(' '.join(args))
		count = utils.inventory.add(utils.inventory.Inventory([item]))
		res = 'Fatto.' if count > 0 else 'L\'oggetto era gia\' presente'
		update.message.reply_text(res)
