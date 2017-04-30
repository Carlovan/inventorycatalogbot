# -*- coding: utf-8 -*-

from . import _read, _write

import utils.user
import utils.inventory
import database.items

def clear(user):
	# Clears all the records with the given user
	assert(type(user) is utils.user.User)
	sql = 'DELETE FROM confronta_items WHERE userid = %s;'
	_write(sql, (user.userid,))

def add_inventory(inv):
	assert(type(inv) is utils.inventory.Inventory)
	sql = 'INSERT INTO confronta_items(userid, itemid) VALUES (%s, %s) ON CONFLICT DO NOTHING;'
	for item in inv.items:
		_write(sql, (inv.user.userid, item.itemid))

def get(user):
	assert(type(user) is utils.user.User)
	sql = 'SELECT * FROM confronta_items INNER JOIN items ON itemid = id WHERE userid = %s;'
	items = _read(sql, (user.userid, ))
	items = list(map(database.items._from_db_format, items))
	return utils.inventory.Inventory(items, user)
