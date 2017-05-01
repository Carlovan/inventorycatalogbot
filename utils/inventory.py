# -*- coding: utf-8 -*-
# This file contains useful function to work with inventories

from .item import Item, is_item
import database.items
import database.users
from utils.filters import UserFilter
from utils.states import UserState

class Inventory:
	def __init__(self, items, user=None):
		self.user = user
		self.items = items
	def get_messages(self, head='', show_id=False):
		# Creates the list of items and splits it in string max 4096 char long
		items = self.items
		res = [head+'\n']
		for item in items:
			item = '-{1} {0}\n'.format(item, item.itemid if show_id else '')
			if len(res[-1]) + len(item) > 4096:
				res.append('')
			res[-1] += item
		return res
	def ensure_data(self):
		# Reads the data from the DB
		if self.user:
			self.user = database.users.get_single(UserFilter(userid=self.user.userid))
		for i in range(len(self.items)):
			self.items[i] = database.items.get_single(self.items[i].name)
	@staticmethod
	def parse(text, *args, **kwargs):
		# Parses an inventory message
		def f(s):
			num = s.rfind('x')
			return s[1:num].strip()
		lines = map(f, text.split('\n'))
		items = []
		for line in lines:
			if is_item(line):
				items.append(Item.from_string(line))
		return Inventory(items, *args, **kwargs)
	def __sub__(self, other):
		if not type(other) is Inventory:
			return NotImplemented
		items = []
		for i in self.items:
			if i not in other.items:
				items.append(i)
		return Inventory(items, self.user)
def add(inv):
	# Adds a list of items to the database
	assert(type(inv) is Inventory)
	items = list(filter(lambda item: database.items.get_single(item.name) is None, inv.items))
	database.items.add(items)
	return len(items)

def received(inv):
	# Function to call when an inventory is received from the user.
	# Then this function will choose what action to perform on that inventory
	assert(type(inv) is Inventory)
	count = add(inv)
	inv.ensure_data()
	if inv.user.state == UserState.NONE:
		return count
	elif inv.user.state == UserState.CONFRONTA:
		database.confronta_items.add_inventory(inv)
		return count
