# -*- coding: utf-8 -*-
# Initializes the database

import utils
import database

def run(bot, update):
	if utils.is_from_admin(update):
		database.build()
		update.message.reply_text('Fatto.')
