# -*- coding: utf-8 -*-

import database.items
import database.users
import database.user_items
from utils.filters import UserFilter, ItemFilter
from utils.states import UserState, ItemState
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
	elif user.state == UserState.CONFRONTAINV_A:
		user.state = UserState.CONFRONTAINV_B
		dbusers.update(user)
		update.message.reply_text('Ora mandami il secondo inventario da confrontare.')
	elif user.state == UserState.CONFRONTAINV_B:
		try:
			dbuseritems = database.user_items.DbUserItems()
			filt = ItemFilter.from_list(user.other.split(' '))
			all_items = dbuseritems.get(user).filter_items(filt)
			dbuseritems.clear(user)
			user.state = UserState.NONE
			user.other = None
			dbusers.update(user)
			a_items = all_items.filter_items(lambda x: x.state == ItemState.CONFRONTAINV_A)
			b_items = all_items.filter_items(lambda x: x.state == ItemState.CONFRONTAINV_B)
			ab_items = a_items - b_items
			ba_items = b_items - a_items
			ab_items.items.sort()
			ba_items.items.sort()
			for x in ab_items.get_messages('Oggetti presenti solo nel primo ({}):'.format(len(ab_items.items))):
				update.message.reply_text(x)
			for x in ba_items.get_messages('Oggetti presenti solo nel secondo ({}):'.format(len(ba_items.items))):
				update.message.reply_text(x)
		except Exception as ex:
			print(ex, flush=True)
	elif user.state in [UserState.CONFRONTA_ADDING, UserState.CONTAINV_ADDING, UserState.CONFRONTAINV_A_ADDING, UserState.CONFRONTAINV_B_ADDING]:
		update.message.reply_text('Aspetta il messaggio di conferma!')
