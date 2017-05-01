# -*- coding: utf-8 -*-

import database.users
import utils
from utils.filters import UserFilter

def run(bot, update, args):
	if utils.is_from_admin(update):
		if len(args) != 2:
			update.message.reply_text('Usage: /adsetadmin username bool')
		else:
			username = args[0]
			value = args[1]
			user = database.users.get_single(UserFilter(username=username))
			if user is None:
				update.message.reply_text('Utente {} non trovato!'.format(username))
			else:
				user.admin = value.lower() in ['t', 'true', '1']
				database.users.update(user)
				update.message.reply_text('Fatto.')
