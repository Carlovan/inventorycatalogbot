# -*- coding: utf-8 -*-
# Handles an inventory message

import utils.inventory
import utils.user
from telegram.ext.dispatcher import run_async

pass_args = False

@run_async
def run(bot, update):
	if utils.is_from_ib(update):
		user = utils.user.User.from_telegram(update.message.from_user)
		inv = utils.inventory.Inventory.parse(update.message.text, user)
		msg = utils.inventory.received(inv)
		update.message.reply_text(msg)
