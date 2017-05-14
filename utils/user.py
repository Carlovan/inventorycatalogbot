# -*- coding: utf-8 -*-
# This module contains class and functions to work with users

import telegram.user
import telegram.ext
import utils.states
import database.users
from utils.filters import UserFilter
import settings

class User:
	def __init__(self, userid, username, admin, state, changelog, other):
		assert(type(userid) is int)
		assert(type(username) is str)
		assert(type(admin) is bool)
		assert(type(state) is utils.states.UserState)
		assert(type(changelog) is bool)
		assert(type(other) is str or other is None)
		self.userid = userid
		self.username = username
		self.admin = admin
		self.state = state
		self.changelog = changelog
		self.other = other
	@staticmethod
	def from_telegram(tuser):
		assert(type(tuser) is telegram.user.User)
		return User(tuser.id, tuser.username, False, utils.states.UserState.NONE, False, None)
	def __str__(self):
		return '{} [{}] [{}]{}'.format(self.username, self.userid, self.state.name, ' [admin]' if self.admin else '')
	def __repr__(self):
		return str(self)

def check_handler_run(bot, update):
	# This handler adds or update the user in the db when any message is received
	dbusers = database.users.DbUsers()
	user = dbusers.get_single(UserFilter(userid=update.message.from_user.id))
	if user == None:
		new_user = User.from_telegram(update.message.from_user)
		dbusers.add_new(new_user)
	else:
		user.username = update.message.from_user.username
		dbusers.update(user)
check_handler = telegram.ext.RegexHandler('.*', check_handler_run)

def changelog_handler_run(bot, update):
	dbusers = database.users.DbUsers()
	user = dbusers.get_single(UserFilter(userid=update.message.from_user.id))
	if user.changelog == False:
		user.changelog = True
		dbusers.update(user)
		update.message.reply_text(settings.changelog, parse_mode='HTML')
changelog_handler = telegram.ext.RegexHandler('.*', changelog_handler_run)
