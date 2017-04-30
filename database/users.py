# -*- coding: utf-8 -*-

from . import _read, _write
import utils.user
import utils.filters
import utils.states

def _from_db_format(user):
	return utils.user.User(user['id'], user['username'], user['admin'], utils.states.UserState(user['state']))

def get_single(filt):
	assert(type(filt) is utils.filters.UserFilter)
	sql = 'SELECT * FROM users WHERE {}'.format(filt.get_sql())
	users = _read(sql, filt.get_args())
	return None if len(users) == 0 else _from_db_format(users[0])

def get_all():
	sql = 'SELECT * FROM users;'
	users = _read(sql)
	return list(map(_from_db_format, users))

def add_new(user):
	sql = 'INSERT INTO users(id, username, admin, state) VALUES (%s, %s, %s, %s);'
	_write(sql, (user.userid, user.username, user.admin, user.state.value))
