# -*- coding: utf-8 -*-
# Handles a /mostra forwarded message

import utils.inventory
import utils.user
from telegram.ext.dispatcher import run_async

pass_args = True

@run_async
def run(bot, update, groupdict):
	if utils.is_from_ib(update):
		user = utils.user.User.from_telegram(update.message.from_user)
		inv = utils.inventory.Inventory([utils.item.Item.from_string(groupdict['item'])], user)
		msg = utils.inventory.received(inv)
		update.message.reply_text(msg)
