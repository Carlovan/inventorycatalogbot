# -*- coding: utf-8 -*-

import database.users
import database.user_items
from utils.states import UserState
from utils.filters import UserFilter

pass_args = False

def run(bot, update):
	dbusers = database.users.DbUsers()
	user = dbusers.get_single(UserFilter(userid=update.message.from_user.id))
	if user.state == UserState.CONFRONTA:
		dbuseritems = database.user_items.DbUserItems()
		user.state = UserState.NONE
		user.other = None
		dbuseritems.clear(user)
		dbusers.update(user)
		update.message.reply_text('Comando <code>confronta</code> annullato.', parse_mode='HTML')
	elif user.state == UserState.CONTAINV:
		dbuseritems = database.user_items.DbUserItems()
		user.state = UserState.NONE
		dbuseritems.clear(user)
		dbusers.update(user)
		update.message.reply_text('Comando <code>containv</code> annullato.', parse_mode='HTML')
	elif user.state in [UserState.CONFRONTA_ADDING, UserState.CONTAINV_ADDING]:
		update.message.reply_text('Aspetta il messaggio di conferma!')
