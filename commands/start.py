# -*- coding: utf-8 -*-

import utils.help
import utils.user, database.users
from utils.filters import UserFilter

def run(bot, update):
	text = utils.help.main_text
	text += '\n Puoi leggere nuovamente questo messaggio con /help .'
	user = database.users.get_single(UserFilter(userid=update.message.from_user.id))
	if user == None:
		database.users.add_new(utils.user.User.from_telegram(update.message.from_user))
	else:
		user.username = update.message.from_user.username
		database.users.update(user)
	update.message.reply_text(text, parse_mode='HTML')
