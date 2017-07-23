# -*- coding: utf-8 -*-

import utils.user
import utils.item
import utils.inventory
import utils.states
from database import Database
import database.items
import logging

logger = logging.getLogger(__name__)

class DbUserItems(Database):
	def clear(self, user):
		# Clears all the records with the given user
		assert(type(user) is utils.user.User)
		sql = 'DELETE FROM user_items WHERE userid = %s;'
		self._write(sql, (user.userid,))

	def add_inventory(self, inv, state):
		assert(type(inv) is utils.inventory.Inventory)
		assert(type(state) is utils.states.ItemState)
		sql = 'INSERT INTO user_items(userid, itemid, quantity, state) VALUES (%s, %s, %s, %s);'
		for item in inv.items:
			if not self.exists(item, inv.user, state):
				self._write(sql, (inv.user.userid, item.itemid, item.quantity, state.value))

	def get(self, user):
		assert(type(user) is utils.user.User)
		sql = 'SELECT * FROM user_items INNER JOIN items ON itemid = id WHERE userid = %s;'
		items = self._read(sql, (user.userid, ))
		items = list(map(database.items._from_db_format, items))
		return utils.inventory.Inventory(items, user)
	
	def exists(self, item, user, state):
		assert(type(item) is utils.item.Item)
		assert(type(user) is utils.user.User)
		sql = 'SELECT * FROM user_items WHERE itemid = %s AND userid = %s AND state = %s;'
		res = self._read(sql, (item.itemid, user.userid, state.value))
		return len(res) > 0
