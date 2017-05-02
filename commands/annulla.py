# -*- coding: utf-8 -*-

import database.users
import database.confronta_items
from utils.states import UserState
from utils.filters import UserFilter

pass_args = False

def run(bot, update):
	user = database.users.get_single(UserFilter(userid=update.message.from_user.id))
	if user.state == UserState.CONFRONTA:
		user.state = UserState.NONE
		user.other = None
		database.confronta_items.clear(user)
		database.users.update(user)
		update.message.reply_text('Comando <code>confronta</code> annullato.', parse_mode='HTML')
