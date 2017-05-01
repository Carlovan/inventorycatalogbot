# -*- coding: utf-8 -*-

import utils.help

def run(bot, update):
	text = utils.help.commands_text
	if utils.is_from_admin(update):
		text += '\n' + utils.help.admin_commands_text
	update.message.reply_text(text, parse_mode='HTML')
