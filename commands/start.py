# -*- coding: utf-8 -*-

import utils.help

def run(bot, update):
	text = utils.help.main_text
	text += '\n Puoi leggere nuovamente questo messaggio con /help .'
	update.message.reply_text(text)
