# -*- coding: utf-8 -*-

import utils.help
import utils.user, database.users
from utils.filters import UserFilter
import settings
import logging
logger = logging.getLogger(__name__)

pass_args = False

def run(bot, update):
	dbusers = database.users.DbUsers()
	#text = utils.help.main_text
	#text += '\n Puoi leggere nuovamente questo messaggio con /help .'
	text = settings.changelog
	user = dbusers.get_single(UserFilter(userid=update.message.from_user.id))
	if user == None:
		new_user = utils.user.User.from_telegram(update.message.from_user)
		dbusers.add_new(new_user)
		logger.info('User {} just started the bot'.format(new_user.username))
	else:
		user.username = update.message.from_user.username
		dbusers.update(user)
	update.message.reply_text(text, parse_mode='HTML')
	
