# -*- coding: utf-8 -*-
# Initializes the database

import utils
import database
import settings

pass_args = False

def run(bot, update):
	if update.message.from_user.id == settings.admin:
		db = database.Database()
		db.build()
		update.message.reply_text('Fatto.')
