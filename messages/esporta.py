# -*- coding: utf-8 -*-
# Handles an esporta message

import utils.inventory
import utils.user
import io
import re
from telegram.ext.dispatcher import run_async
import logging
logger = logging.getLogger(__name__)

pass_args = False

@run_async
def run(bot, update):
	if utils.is_from_ib(update):
		user = utils.user.User.from_telegram(update.message.from_user)
		doc = bot.getFile(update.message.document.file_id)
		contentStream = io.BytesIO()
		doc.download(out=contentStream)
		content = contentStream.getvalue().decode('utf-8')
		contentStream.close()
		content = re.sub(r'[^\S\n]+', ' ', content) # Replace any group of consecutive blanks (except newline) with a single whitespace
		content = re.sub(r'^(\d)+x +(.+)$', r'- \2 x\1', content, flags=re.MULTILINE) # makes every lline in the same format as the command /inventario
		inv = utils.inventory.Inventory.parse(content, user)
		msg = utils.inventory.received(inv)
		update.message.reply_text(msg)
