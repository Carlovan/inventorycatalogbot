# -*- coding: utf-8 -*-

import utils.user
import utils.inventory
from database import Database
import database.items

class DbConfrontaItems(Database):
	def clear(self, user):
		# Clears all the records with the given user
		assert(type(user) is utils.user.User)
		sql = 'DELETE FROM confronta_items WHERE userid = %s;'
		self._write(sql, (user.userid,))

	def add_inventory(self, inv):
		assert(type(inv) is utils.inventory.Inventory)
		sql = 'INSERT INTO confronta_items(userid, itemid) SELECT %s, %s WHERE NOT EXISTS (SELECT 1 FROM confronta_items WHERE userid = %s AND itemid = %s);'
		for item in inv.items:
			self._write(sql, (inv.user.userid, item.itemid)*2)

	def get(self, user):
		assert(type(user) is utils.user.User)
		sql = 'SELECT * FROM confronta_items INNER JOIN items ON itemid = id WHERE userid = %s;'
		items = self._read(sql, (user.userid, ))
		items = list(map(database.items._from_db_format, items))
		return utils.inventory.Inventory(items, user)
