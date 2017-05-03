# -*- coding: utf-8 -*-

import database.users
import utils
from utils.filters import UserFilter

pass_args = True

def run(bot, update, args):
	if utils.is_from_admin(update):
		if len(args) != 2:
			update.message.reply_text('Usage: /adsetadmin username bool')
		else:
			dbusers = database.users.DbUsers()
			username = args[0]
			value = args[1]
			user = dbusers.get_single(UserFilter(username=username))
			if user is None:
				update.message.reply_text('Utente {} non trovato!'.format(username))
			else:
				user.admin = value.lower() in ['t', 'true', '1']
				dbusers.update(user)
				update.message.reply_text('Fatto.')
