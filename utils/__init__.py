# -*- coding: utf-8  -*-
# A bunch of useful functions

import database.users
from .filters import UserFilter
import settings

def is_from_ib(update):
	# Gets a bot update and checks if it's from @InventoryBot
	message = update.message
	valid = message.forward_from is not None and message.forward_from.username == 'InventoryBot'
	if not valid:
		update.message.reply_text('Devi inoltrare il messaggio da @InventoryBot!')
		return False
	return True

def is_from_admin(update):
	# Gets a bot update and checks if it's from an admin
	dbusers = database.users.DbUsers()
	filt = UserFilter(userid=update.message.from_user.id)
	user = dbusers.get_single(filt)
	return user.admin

def send_admin(message):
	# Sends a message with the given text to Carlovan
	dbusers = database.users.DbUsers()
	carlovan = dbusers.get_single(UserFilter(username='Carlovan'))
	settings.bot.send_message(carlovan.userid, text=message, parse_mode='HTML')
