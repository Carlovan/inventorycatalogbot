# -*- coding: utf-8  -*-

import database.users
import utils

pass_args = False

def run(bot, update):
	if utils.is_from_admin(update):
		dbusers = database.users.DbUsers()
		dbusers.set_all_changelog()
		update.message.reply_text('Fatto.')
