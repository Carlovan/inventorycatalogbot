# -*- coding: utf-8 -*-
# This file contains a class to represent an item and some extension function to check if a string represents an item

import re

_rarities = ['U', 'X', 'L11', 'L10', 'L9', 'L8', 'L7', 'L6', 'L5', 'L4', 'L3', 'L2', 'L1', 'M+', 'M', 'S+', 'S', 'R+', 'R', 'N+', 'N', 'C+', 'C']
_articles = ['un ', 'uno ', 'una ', 'un\'', 'il ', 'lo ', 'la ', 'i ', 'gli ', 'le ', 'l\'']

_rarity_regex_text =  r'(?P<rarity>{})'.format('|'.join(_rarities).replace('+', r'\+'))
_item_regex_text   = fr'(?P<name>.*?)\s+\[{_rarity_regex_text}\](?P<usable> \[usabile\])?'
_rarity_regex = re.compile(_rarity_regex_text)
_item_regex   = re.compile(_item_regex_text)
_name_exceptions = {re.compile('^un po\' di Pongo.*'): 'un po\' di Pongo',
                    re.compile('^il Libro degli Ospiti.*'): 'il Libro degli Ospiti',
                    re.compile('^un Pakkomon di nome.*'): 'un Pakkomon'}

class Item:
	def __init__(self, name, rarity, usable, itemid=None):
		assert(type(name) is str)
		assert(type(rarity) is str)
		assert(type(usable) is bool)
		assert(type(itemid) is int or itemid is None)
		assert(is_rarity(rarity))
		self.name = name.replace('\xa0', ' ')
		self.rarity = rarity
		self.usable = usable
		self.itemid = itemid

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
		return Item(name, rarity, usable)

def is_rarity(text):
	# Checks if the given string is a valid rarity
	return _rarity_regex.fullmatch(text) is not None

def is_item(text):
	# Checks if the given string is a valid item
	return _item_regex.fullmatch(text) is not None
