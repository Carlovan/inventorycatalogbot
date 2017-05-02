# -*- coding: utf-8 -*-
# This commands sends a message to all the registered users

import utils
import telegram
import database.users

pass_args = True

def run(bot, update, args):
	if utils.is_from_admin(update):
		text = ' '.join(args)
		users = database.users.get_all()
		for user in users:
			try: # Necessary if the user blocked the bot
				bot.send_message(chat_id=user.userid, text=text, parse_mode='HTML')
			except telegram.TelegramError:
				pass
