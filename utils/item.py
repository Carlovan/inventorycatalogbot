# -*- coding: utf-8 -*-
# This file contains a class to represent an item and some extension function to check if a string represents an item

import re

_rarities = ['X', 'L10', 'L9', 'L8', 'L7', 'L6', 'L5', 'L4', 'L3', 'L2', 'L1', 'U', 'M+', 'M', 'S+', 'S', 'R+', 'R', 'N+', 'N', 'C+', 'C']
_articles = ['un ', 'uno ', 'una ', 'un\'', 'il ', 'lo ', 'la ', 'i ', 'gli ', 'le ', 'l\'']

_rarity_regex_text =  r'(?P<rarity>{})'.format('|'.join(_rarities).replace('+', r'\+'))
_item_regex_text   = fr'(?P<name>.*?)\s+\[{_rarity_regex_text}\](?P<usable> \[usabile\])?'
_rarity_regex = re.compile(_rarity_regex_text)
_item_regex   = re.compile(_item_regex_text)

class Item:
	def __init__(self, name, rarity, usable):
		assert(type(name) is str)
		assert(type(rarity) is str)
		assert(type(usable) is bool)
		assert(is_rarity(rarity))
		self.name = name
		self.rarity = rarity
		self.usable = usable

	def __str__(self):
		return f'{self.name} [{self.rarity}]{{}}'.format(' [usabile]' if self.usable else '')

	def __lt__(self, other):
		assert(type(other) is Item)
		if self.rarity != other.rarity:
			return _rarities.index(self.rarity) < _rarities.index(other.rarity)
		# Remove articles
		name1 = self.name.lower()
		name2 = other.name.lower()
		for art in _articles:
			if name1.find(art) == 0:
				name1 = name1[len(art):]
			if name2.find(art) == 0:
				name2 = name2[len(art):]
		return name1 < name2

	@staticmethod
	def from_string(text):
		match = _item_regex.fullmatch(text)
		self.name = match.group('name')
		self.rarity = match.group('rarity')
		self.usable = match.group('usable') is not None

def is_rarity(text):
	# Checks if the given string is a valid rarity
	return _rarity_regex.fullmatch(text) is not None

def is_item(text):
	# Checks if the given string is a valid item
	return _item_regex.fullmatch(text) is not None

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
