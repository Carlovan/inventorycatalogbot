# Handles the stats message for a user.
# Useful to add [U]s from that

from telegram.ext.dispatcher import run_async
import utils.inventory
import utils.user

pass_args = True

@run_async
def run(bot, update, groupdict):
	print('ok')
	if utils.is_from_ib(update):
		user = utils.user.User.from_telegram(update.message.from_user)
		inv = utils.inventory.Inventory.parse(groupdict['items'], user)
		msg = utils.inventory.received(inv)
		update.message.reply_text(msg)
