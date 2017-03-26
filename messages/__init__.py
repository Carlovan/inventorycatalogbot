# -*- coding: utf-8 -*-
# This package contains handlers for text messages

import importlib
from telegram.ext import RegexHandler

msg_list = [('inventario','@.*, possiedi( \(pg \d+/\d+\))?:\n.*'), ('mostra', '@.*, mostri orgogliosamente di possedere \d+x (?P<item>.*)')]

handlers = []
for c in msg_list:
	m = importlib.import_module('.'+c[0], __name__)
	groups = m.run.__code__.co_argcount == 3 # If the run function takes 3 arguments, groupdict from the regex is required
	handlers.append(RegexHandler(c[1], m.run, pass_groupdict=groups))
