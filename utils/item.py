# -*- coding: utf-8 -*-
# This file contains a class to represent an item and some extension function to check if a string represents an item

import re
from utils.states import ItemState

_rarities = ['U', 'X', 'L11', 'L10', 'L9', 'L8', 'L7', 'L6', 'L5', 'L4', 'L3', 'L2', 'L1', 'M+', 'M', 'S+', 'S', 'R+', 'R', 'N+', 'N', 'C+', 'C']
_articles = ['un ', 'uno ', 'una ', 'un\'', 'il ', 'lo ', 'la ', 'i ', 'gli ', 'le ', 'l\'']

_rarity_regex_text =  r'(?P<rarity>{})'.format('|'.join(_rarities).replace('+', r'\+'))
_item_regex_text   = fr'(- *)?(?P<name>.*?)\s+\[{_rarity_regex_text}\](?P<usable> \[usabile\])?( *x *(?P<quantity>\d+))?'
_rarity_regex = re.compile(_rarity_regex_text)
_item_regex   = re.compile(_item_regex_text)
_name_exceptions = {re.compile('^un po\' di Pongo.*'): 'un po\' di Pongo',
                    re.compile('^il Libro degli Ospiti.*'): 'il Libro degli Ospiti',
                    re.compile('^un Pakkomon di nome.*'): 'un Pakkomon'}

class Item:
	def __init__(self, name, rarity, usable, itemid=None, quantity=0, state=ItemState.NONE):
		assert(type(name) is str)
		assert(type(rarity) is str)
		assert(type(usable) is bool)
		assert(type(itemid) is int or itemid is None)
		assert(type(quantity) is int)
		assert(type(state) is ItemState)
		assert(is_rarity(rarity))
		self.name = name.replace('\xa0', ' ')
		self.rarity = rarity
		self.usable = usable
		self.itemid = itemid
		self.quantity = quantity
		self.state = state

	def __str__(self):
		values = {'name': self.name,
		          'rarity': self.rarity,
				  'usable': ' [usabile]' if self.usable else '',
				  'quantity': ' x{}'.format(self.quantity) if self.quantity > 0 else ''
				 }
		return '{name} [{rarity}]{usable}{quantity}'.format(**values)

	def __lt__(self, other):
		assert(type(other) is Item)
		if self.rarity != other.rarity:
			return _rarities.index(self.rarity) < _rarities.index(other.rarity)
		# Check quantity
		if self.quantity != other.quantity:
			return self.quantity < other.quantity
		# Remove articles
		name1 = self.name.lower()
		name2 = other.name.lower()
		for art in _articles:
			if name1.find(art) == 0:
				name1 = name1[len(art):]
			if name2.find(art) == 0:
				name2 = name2[len(art):]
		return name1 < name2

	def __eq__(self, other):
		return type(other) is Item and self.name == other.name and self.rarity == other.rarity and self.usable == other.usable

	@staticmethod
	def from_string(text):
		match = _item_regex.fullmatch(text)
		name = match.group('name')
		for ex in _name_exceptions:
			if ex.match(name) != None:
				name = _name_exceptions[ex]
				break
		rarity = match.group('rarity')
		usable = match.group('usable') is not None
		quantity = int(match.group('quantity') or 0)
		return Item(name, rarity, usable, quantity=quantity)

def is_rarity(text):
	# Checks if the given string is a valid rarity
	return _rarity_regex.fullmatch(text) is not None

def is_item(text):
	# Checks if the given string is a valid item
	return _item_regex.fullmatch(text) is not None
