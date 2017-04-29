# -*- coding: utf-8 -*-
# This file contains useful function to work with inventories

from .item import Item, is_item
import database.items

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

def add(inv):
	# Adds a list of items to the database
	assert(type(inv) is Inventory)
	items = list(filter(lambda item: database.items.get_single(item.name) is None, inv.items))
	database.items.add(items)
	return len(items)
