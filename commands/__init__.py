# -*- coding: utf-8 -*-
# This package contains handlers for commands

import importlib
from telegram.ext import CommandHandler

cmd_list = ['adadd', 'addelete', 'adinit', 'adinventario', 'adsetadmin', 'adupdate', 'broadcast', 'conta', 'containv', 'help', 'helpcomandi', 'helpcontribuisci', 'inventario', 'start', 'ultimi', 'confronta', 'fine', 'annulla']

handlers = []
for c in cmd_list:
	m = importlib.import_module('.'+c, __name__)
	args = m.pass_args
	handlers.append(CommandHandler(c, m.run, pass_args=args))
