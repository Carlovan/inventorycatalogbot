# -*- coding: utf-8 -*-

import utils.help

def run(bot, update):
	text = utils.help.commands_text
	update.message.reply_text(text)
