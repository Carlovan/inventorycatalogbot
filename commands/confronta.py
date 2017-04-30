# -*- coding: utf-8 -*-

import database.users
from utils.filters import UserFilter
from utils.states import UserState

def run(bot, update):
	user = database.users.get_single(UserFilter(userid=update.message.from_user.id))
	if user.state == UserState.NONE:
		user.state = UserState.CONFRONTA
		database.users.update(user)
		update.message.reply_text('Ora mandami il tuo inventario. Quando hai finito usa /done. Per cancellare /cancel.')
