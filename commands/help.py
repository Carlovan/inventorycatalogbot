# -*- coding: utf-8 -*-

import utils.help

pass_args = False

def run(bot, update):
	text = utils.help.main_text
	update.message.reply_text(text, parse_mode='HTML')
