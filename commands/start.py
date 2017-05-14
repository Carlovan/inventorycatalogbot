# -*- coding: utf-8 -*-

import utils.help
import utils.user, database.users
from utils.filters import UserFilter
import settings
import logging
logger = logging.getLogger(__name__)

pass_args = False

def run(bot, update):
	update.message.reply_text('Ciao benvenuto nel catalogo di @InventoryBot! Ti consiglio caldamente di leggere /help per sapere come funziona :P')
	update.message.reply_text(settings.changelog, parse_mode='HTML')
	logger.info('User {} just started the bot'.format(update.message.from_user.username))
