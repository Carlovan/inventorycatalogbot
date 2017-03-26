# -*- coding: utf-8  -*-
# A bunch of useful functions

import database
from .filters import UserFilter

def is_fromIB(update):
	# Gets a bot update and checks if it's from @InventoryBot
	message = update.message
	valid = message.forward_from is not None and message.forward_from.username == 'InventoryBot'
	if not valid:
		update.message.reply_text('Devi inoltrare il messaggio da @InventoryBot!')
		return False
	return True

def is_from_admin(update):
	# Gets a bot update and checks if it's from an admin
	filt = UserFilter(userid=update.message.from_user.id)
	user = database.get_user(filt)
	return user.admin
