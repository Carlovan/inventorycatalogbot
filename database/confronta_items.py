# -*- coding: utf-8 -*-

import utils.user
import utils.item
import utils.inventory
from database import Database
import database.items
import logging

logger = logging.getLogger(__name__)

class DbConfrontaItems(Database):
	def clear(self, user):
		# Clears all the records with the given user
		assert(type(user) is utils.user.User)
		sql = 'DELETE FROM confronta_items WHERE userid = %s;'
		self._write(sql, (user.userid,))

	def add_inventory(self, inv):
		assert(type(inv) is utils.inventory.Inventory)
		sql = 'INSERT INTO confronta_items(userid, itemid) VALUES (%s, %s);'
		for item in inv.items:
			if not self.exists(item, inv.user):
				self._write(sql, (inv.user.userid, item.itemid))

	def get(self, user):
		assert(type(user) is utils.user.User)
		sql = 'SELECT * FROM confronta_items INNER JOIN items ON itemid = id WHERE userid = %s;'
		items = self._read(sql, (user.userid, ))
		items = list(map(database.items._from_db_format, items))
		return utils.inventory.Inventory(items, user)
	
	def exists(self, item, user):
		assert(type(item) is utils.item.Item)
		assert(type(user) is utils.user.User)
		sql = 'SELECT * FROM confronta_items WHERE itemid = %s AND userid = %s;'
		res = self._read(sql, (item.itemid, user.userid))
		return len(res) > 0
