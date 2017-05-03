# -*- coding: utf-8 -*-

import database.items
import database.users
import database.confronta_items
from utils.filters import UserFilter, ItemFilter
from utils.states import UserState

pass_args = False

def run(bot, update):
	dbusers = database.users.DbUsers()
	user = dbusers.get_single(UserFilter(userid=update.message.from_user.id))
	if user.state == UserState.CONFRONTA:
		dbconfrontaitems = database.confronta_items.DbConfrontaItems()
		dbitems = database.items.DbItems()
		uinv = dbconfrontaitems.get(user)
		query = user.other.split(' ')
		filt = ItemFilter.from_list(query)
		dbinv = dbitems.get_multiple(filt)
		diff = dbinv - uinv
		diff.items.sort()

		user.state = UserState.NONE
		user.other = None
		dbconfrontaitems.clear(user)
		dbusers.update(user)

		messages = diff.get_messages(head='Ti mancano {} oggetti:'.format(len(diff.items)))
		for m in messages:
			update.message.reply_text(m)
	elif user.state == UserState.CONFRONTA_ADDING:
		update.message.reply_text('Aspetta il messaggio di conferma!')
