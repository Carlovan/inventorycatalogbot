# -*- coding: utf-8  -*-

import database.users
from utils.filters import UserFilter
from utils.states import UserState
import utils.inventory
from telegram.ext.dispatcher import run_async
import logging
logger = logging.getLogger(__name__)

pass_args = False

@run_async
def run(bot, update):
	dbusers = database.users.DbUsers()
	user = dbusers.get_single(UserFilter(userid=update.message.from_user.id))
	if user.state == UserState.NONE:
		logger.info('User {}'.format(update.message.from_user.username))
		user.state = UserState.CONTAINV
		dbusers.update(user)
		update.message.reply_text('Ora mandami il tuo inventario. Quando hai finito usa /fine. Per annullare /annulla.')
	else:
		update.message.reply_text('È in corso un altro comando, usa /fine o /annulla.')
