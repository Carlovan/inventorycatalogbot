# -*- coding: utf-8 -*-

import database.users
from utils.filters import UserFilter
from utils.states import UserState
from telegram.ext.dispatcher import run_async
import logging
logger = logging.getLogger(__name__)

pass_args = True

@run_async
def run(bot, update, args):
	dbusers = database.users.DbUsers()
	user = dbusers.get_single(UserFilter(userid=update.message.from_user.id))
	if user.state == UserState.NONE:
		logger.info('User {} -> ({})'.format(update.message.from_user.username, ' '.join(args)))
		user.other = ' '.join(args)
		user.state = UserState.CONFRONTA
		dbusers.update(user)
		update.message.reply_text('Ora mandami il tuo inventario. Quando hai finito usa /fine. Per cancellare /annulla.')
	elif user.state == UserState.CONFRONTA:
		user.other = ' '.join(args)
		dbusers.update(user)
		update.message.reply_text('Filtro aggiornato')
