# -*- coding: utf-8 -*-
# This package contains handlers for text messages

import importlib
from telegram.ext import MessageHandler, RegexHandler
from telegram.ext.filters import Filters

msg_list = [('inventario','@.*, possiedi( \(pg \d+/\d+\))?:\n.*'),
            ('mostra', '@.*, mostri orgogliosamente di possedere \d+x (?P<item>.*)'),
            ('esporta', Filters.document)]

handlers = []
for c in msg_list:
	m = importlib.import_module('.'+c[0], __name__)
	groups = m.run.__code__.co_argcount == 3 # If the run function takes 3 arguments, groupdict from the regex is required
	if type(c[1]) is str:
		handlers.append(RegexHandler(c[1], m.run, pass_groupdict=groups))
	else:
		handlers.append(MessageHandler(c[1], m.run))
