# -*- coding: utf-8 -*-

import database.users
import database.confronta_items
from utils.states import UserState
from utils.filters import UserFilter

pass_args = False

def run(bot, update):
	dbusers = database.users.DbUsers()
	user = dbusers.get_single(UserFilter(userid=update.message.from_user.id))
	if user.state == UserState.CONFRONTA:
		dbconfrontaitems = database.confronta_items.DbConfrontaItems()
		user.state = UserState.NONE
		user.other = None
		dbconfrontaitems.clear(user)
		dbusers.update(user)
		update.message.reply_text('Comando <code>confronta</code> annullato.', parse_mode='HTML')
	elif user.state == UserState.CONFRONTA_ADDING:
		update.message.reply_text('Aspetta il messaggio di conferma!')