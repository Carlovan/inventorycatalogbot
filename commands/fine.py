# -*- coding: utf-8 -*-

import database.items
import database.users
import database.user_items
from utils.filters import UserFilter, ItemFilter
from utils.states import UserState
import utils.item

pass_args = False

def run(bot, update):
	dbusers = database.users.DbUsers()
	user = dbusers.get_single(UserFilter(userid=update.message.from_user.id))
	if user.state == UserState.CONFRONTA:
		dbuseritems = database.user_items.DbUserItems()
		dbitems = database.items.DbItems()
		uinv = dbuseritems.get(user)
		query = user.other.split(' ')
		filt = ItemFilter.from_list(query)
		dbinv = dbitems.get_multiple(filt)
		diff = dbinv - uinv
		diff.items.sort()

		user.state = UserState.NONE
		user.other = None
		dbuseritems.clear(user)
		dbusers.update(user)

		messages = diff.get_messages(head='Ti mancano {} oggetti:'.format(len(diff.items)))
		for m in messages:
			update.message.reply_text(m)
	elif user.state == UserState.CONTAINV:
		dbuseritems = database.user_items.DbUserItems()
		dbitems = database.items.DbItems()
		uinv = dbuseritems.get(user)
		text = 'Hai in totale {} oggetti di cui:'.format(len(uinv.items))
		for rar in utils.item._rarities:
			filt = ItemFilter(rarity=[rar])
			ucount = len(uinv.filter_items(filt).items)
			dbcount = dbitems.count(filt)
			text += '\n- {}/{} di rarità {}'.format(ucount, dbcount, rar)

		user.state = UserState.NONE
		dbuseritems.clear(user)
		dbusers.update(user)
		update.message.reply_text(text)
	elif user.state in [UserState.CONFRONTA_ADDING, UserState.CONTAINV_ADDING]:
		update.message.reply_text('Aspetta il messaggio di conferma!')
