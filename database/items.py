# -*- coding: utf-8 -*-

from . import _read, _write
import utils.item
import utils.filters

def count(filt):
	assert(type(filt) is utils.filters.ItemFilter)
	sql = 'SELECT COUNT(*) AS total FROM items WHERE {}'.format(filt.get_sql())
	return _read(sql, filt.get_args())[0]['total']

def get_single(name):
	# Returns the item with the given name
	assert(type(name) is str)
	sql = 'SELECT * FROM items WHERE name = %s'
	item = _read(sql, (name,))
	return None if len(item) == 0 else utils.item.Item(item[0]['name'], item[0]['rarity'], item[0]['usable'])

def get_multiple(filt):
	assert(type(filt) is utils.filters.ItemFilter)
	sql = 'SELECT * FROM items WHERE {}'.format(filt.get_sql())
	items = _read(sql, filt.get_args())
	items = map(lambda item: utils.item.Item(item['name'], item['rarity'], item['usable']), items)
	return list(items)

def add(items):
	assert(all(map(lambda x: type(x) is utils.item.Item, items)))
	sql = 'INSERT INTO items(name, rarity, usable) VALUES (%s, %s, %s)'
	for item in items:
		_write(sql, (item.name, item.rarity, item.usable))

