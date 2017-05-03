# -*- coding: utf-8 -*-

from database import Database
import utils.inventory
import utils.item
import utils.filters
import logging

logger = logging.getLogger(__name__)

def _from_db_format(item):
	return utils.item.Item(item['name'], item['rarity'], item['usable'], item['id'])

class DbItems(Database):
	def count(self, filt):
		assert(type(filt) is utils.filters.ItemFilter)
		sql = 'SELECT COUNT(*) AS total FROM items WHERE {}'.format(filt.get_sql())
		return self._read(sql, filt.get_args())[0]['total']

	def get_single(self, name):
		# Returns the item with the given name
		assert(type(name) is str)
		sql = 'SELECT * FROM items WHERE name = %s'
		item = self._read(sql, (name,))
		return None if len(item) == 0 else _from_db_format(item[0])

	def get_multiple(self, filt):
		assert(type(filt) is utils.filters.ItemFilter)
		sql = 'SELECT * FROM items WHERE {}'.format(filt.get_sql())
		items = self._read(sql, filt.get_args())
		items = list(map(_from_db_format, items))
		return utils.inventory.Inventory(items)

	def get_last(self, count):
		assert(type(count) is int)
		sql = 'SELECT * FROM items ORDER BY id DESC LIMIT %s'
		items = self._read(sql, (count,))
		items = list(map(_from_db_format, items))
		return utils.inventory.Inventory(items)

	def add(self, items):
		assert(all(map(lambda x: type(x) is utils.item.Item, items)))
		sql = 'INSERT INTO items(name, rarity, usable) VALUES (%s, %s, %s)'
		for item in items:
			self._write(sql, (item.name, item.rarity, item.usable))

	def delete(self, itemid):
		# Deletes the item with the given id
		sql = 'DELETE FROM items WHERE id = %s'
		self._write(sql, (itemid,))
