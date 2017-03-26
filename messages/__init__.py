# -*- coding: utf-8 -*-
# This package contains handlers for text messages

import importlib
from telegram.ext import RegexHandler

msg_list = [('inventario','@.*, possiedi:\n.*')]

handlers = []
for c in msg_list:
	m = importlib.import_module('.'+c[0], __name__)
	handlers.append(RegexHandler(c[1], m.run))
