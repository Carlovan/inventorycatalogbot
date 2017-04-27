# -*- coding: utf-8 -*-

import utils.help
import utils.user, database.users

def run(bot, update):
	text = utils.help.main_text
	text += '\n Puoi leggere nuovamente questo messaggio con /help .'
	user = update.message.from_user
	database.users.add_new(utils.user.User(user.id, user.username, False))
	update.message.reply_text(text)
