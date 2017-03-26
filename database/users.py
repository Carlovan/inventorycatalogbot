# -*- coding: utf-8 -*-

from . import _read, _write
import utils.user
import utils.filters

def get_multiple(filt):
	assert(type(filt) is utils.filters.UserFilter)
	sql = 'SELECT * FROM users WHERE {}'.format(filt.get_sql())
	users = _read(sql, filt.get_args())
	return None if len(users) == 0 else utils.user.User(users[0]['id'], users[0]['username'], users[0]['admin'])
