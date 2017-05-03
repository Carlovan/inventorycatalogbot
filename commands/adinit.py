# -*- coding: utf-8 -*-
# Initializes the database

import utils
import database

pass_args = False

def run(bot, update):
	db = database.Database()
	db.build()
	update.message.reply_text('Fatto.')
