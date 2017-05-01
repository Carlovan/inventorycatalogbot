# -*- coding: utf-8 -*-

import database.users
import database.confronta_items
from utils.filters import UserFilter, ItemFilter
from utils.states import UserState

def run(bot, update):
	user = database.users.get_single(UserFilter(userid=update.message.from_user.id))
	if user.state == UserState.CONFRONTA:
		uinv = database.confronta_items.get(user)
		query = user.other.split(' ')
		filt = ItemFilter.from_list(query)
		dbinv = database.items.get_multiple(filt)
		diff = dbinv - uinv
		diff.items.sort()

		user.state = UserState.NONE
		user.other = None
		database.confronta_items.clear(user)
		database.users.update(user)

		update.message.reply_text('Your query was {}'.format(query))
		messages = diff.get_messages(head='Ti mancano {} oggetti:'.format(len(diff.items)))
		for m in messages:
			update.message.reply_text(m)
