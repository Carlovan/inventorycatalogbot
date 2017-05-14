# -*- coding: utf-8 -*-

from database import Database
import utils.user
import utils.filters
import utils.states

def _from_db_format(user):
	return utils.user.User(user['id'], user['username'], user['admin'], utils.states.UserState(user['state']), user['changelog'], user['other'])

class DbUsers(Database):
	def get_single(self, filt):
		assert(type(filt) is utils.filters.UserFilter)
		sql = 'SELECT * FROM users WHERE {}'.format(filt.get_sql())
		users = self._read(sql, filt.get_args())
		return None if len(users) == 0 else _from_db_format(users[0])

	def get_all(self):
		sql = 'SELECT * FROM users;'
		users = self._read(sql)
		return list(map(_from_db_format, users))

	def add_new(self, user):
		sql = 'INSERT INTO users(id, username, admin, state) VALUES (%s, %s, %s, %s);'
		self._write(sql, (user.userid, user.username, user.admin, user.state.value))

	def update(self, user):
		sql = 'UPDATE users SET username = %s, admin = %s, state = %s, changelog = %s, other = %s WHERE id = %s;'
		self._write(sql, (user.username, user.admin, user.state.value, user.changelog, user.other, user.userid))

	def set_all_changelog(self):
		sql = 'UPDATE users SET changelog = false;'
		self._write(sql)
