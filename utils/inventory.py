# -*- coding: utf-8 -*-
# This file contains useful function to work with inventories

from .item import Item, is_item
import database.items

def get_messages(items, head=''):
	# Creates the list of items and splits it in string max 4096 char long
	items = map(str, items)
	res = [head+'\n']
	for item in items:
		item = f'- {item}\n'
		if len(res[-1]) + len(item) > 4096:
			res.append('')
		res[-1] += item
	return res

def parse(text):
	# Parses an inventory message
	def f(s):
		num = s.rfind('x')
		return s[1:num].strip()
	lines = map(f, text.split('\n'))
	items = []
	for line in lines:
		if is_item(line):
			items.append(Item.from_string(line))
	return items

def add(items):
	# Adds a list of items to the database
	assert(isinstance(items, (tuple, list)))
	items = list(filter(lambda item: database.items.get_single(item.name) is None, items))
	database.items.add(items)
	return len(items)
