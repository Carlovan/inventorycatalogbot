# -*- coding: utf-8 -*-
# This package contains handlers for text messages

import importlib
from telegram.ext import MessageHandler, RegexHandler
from telegram.ext.filters import Filters
import re

msg_list = [('inventario','@.*, possiedi( \(pg \d+/\d+\))?:\n.*'),
            ('mostra', '@.*, mostri orgogliosamente di possedere \d+x (?P<item>.*)'),
            ('esporta', Filters.document),
			('users_stats', 'Avventuriero @.+(\n.*)*.*Oggetti unici:(?P<items>.+(\n.*)*)')]

handlers = []
for c in msg_list:
	m = importlib.import_module('.'+c[0], __name__)
	groups = m.pass_args
	if type(c[1]) is str:
		handlers.append(RegexHandler(c[1], m.run, pass_groupdict=groups))
	else:
		handlers.append(MessageHandler(c[1], m.run))
