# -*- coding: utf-8 -*-
# This module contains class and functions to work with users

class User:
	def __init__(self, userid, username, admin):
		assert(type(userid) is int)
		assert(type(username) is str)
		assert(type(admin) is bool)
		self.userid = userid
		self.username = username
		self.admin = admin
	
	def __str__(self):
		return f'{self.username} [{self.userid}]{{}}'.format(' [admin]' if self.admin else '')
