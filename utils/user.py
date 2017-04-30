# -*- coding: utf-8 -*-
# This module contains class and functions to work with users

import telegram.user
import utils.states

class User:
	def __init__(self, userid, username, admin, state):
		assert(type(userid) is int)
		assert(type(username) is str)
		assert(type(admin) is bool)
		assert(type(state) is utils.states.UserState)
		self.userid = userid
		self.username = username
		self.admin = admin
		self.state = state
	@staticmethod
	def from_telegram(tuser):
		assert(type(tuser) is telegram.user.User)
		return User(tuser.id, tuser.username, False, utils.states.UserState.NONE)
	def __str__(self):
		return '{} [{}] [{}]{}'.format(self.username, self.userid, self.state.name, ' [admin]' if self.admin else '')
	def __repr__(self):
		return str(self)
