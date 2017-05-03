# -*- coding: utf-8 -*-

import utils.help
import utils.user, database.users
from utils.filters import UserFilter

pass_args = False

def run(bot, update):
	dbusers = database.users.DbUsers()
	#text = utils.help.main_text
	#text += '\n Puoi leggere nuovamente questo messaggio con /help .'
	text = '''Changelog felice!
Il bot e' stato completamente riscritto anche se da fuori non sembrerebbe. Il codice lo trovate <a href="https://github.com/Carlovan/inventorycatalogbot">qui</a>.
Ora sono supportati anche i comandi /inv2 e /esporta di @InventoryBot.
Il comando /confronta dovrebbe funzionare molto meglio rispetto a prima.
Ho anche cambiato server quindi non dovrete piu aspettare i soliti 10 secondi ogni volta che gli scrivete :)

Per info generali /help. Per info sui comandi (consigliata la lettura) /helpcomandi.
Per segnalazioni @Carlovan.'''
	user = dbusers.get_single(UserFilter(userid=update.message.from_user.id))
	if user == None:
		dbusers.add_new(utils.user.User.from_telegram(update.message.from_user))
	else:
		user.username = update.message.from_user.username
		dbusers.update(user)
	update.message.reply_text(text, parse_mode='HTML')
