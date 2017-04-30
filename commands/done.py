# -*- coding: utf-8 -*-

import database.users
import database.confronta_items
from utils.filters import UserFilter
from utils.states import UserState

def run(bot, update):
	user = database.users.get_single(UserFilter(userid=update.message.from_user.id))
	if user.state == UserState.CONFRONTA:
		user.state = UserState.NONE
		inv = database.confronta_items.get(user)
		database.confronta_items.clear(user)
		database.users.update(user)
		messages = inv.get_messages()
		for m in messages:
			update.message.reply_text(m)
