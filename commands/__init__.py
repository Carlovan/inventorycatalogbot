# -*- coding: utf-8 -*-
# This package contains handlers for commands

import importlib
from telegram.ext import CommandHandler

cmd_list = ['adadd', 'addelete', 'adinit', 'adinventario', 'adnewchangelog', 'adsetadmin', 'adupdate', 'broadcast', 'conta', 'containv', 'help', 'helpcomandi', 'helpcontribuisci', 'inventario', 'start', 'ultimi', 'confronta', 'confrontainv', 'fine', 'annulla']


def reply_exception_wrapper(handler):
	def new_handler(bot, update, *args, **kwargs):
		try:
			return handler(bot, update, *args, **kwargs)
		except Exception as ex:
			update.message.reply_text('ERRORE: {}'.format(str(ex)))
	return new_handler


handlers = []
for c in cmd_list:
	m = importlib.import_module('.'+c, __name__)
	args = m.pass_args
	handlers.append(CommandHandler(c, reply_exception_wrapper(m.run), pass_args=args))
