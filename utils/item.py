# -*- coding: utf-8 -*-
# This file contains a class to represent an item and some extension function to check if a string represents an item

import re

_rarity_regex_text =  r'(?P<rarity>[CNRSM]\+?|X|L[0-9]{1,2})'
_item_regex_text   = fr'(?P<name>.*?)\s+\[{_rarity_regex_text}\](?P<usable> \[usabile\])?'
_rarity_regex = re.compile(_rarity_regex_text)
_item_regex   = re.compile(_item_regex_text)

class Item:
	def __init__(self, name, rarity, usable):
		assert(type(name) is str)
		assert(type(rarity) is str)
		assert(type(usable) is bool)
		self.name = name
		self.rarity = rarity
		self.usable = usable

	def __str__(self):
		return f'{self.name} [{self.rarity}]{{}}'.format(' [usabile' if self.usable else '')

def is_rarity(text):
	# Checks if the given string is a valid rarity
	return _rarity_regex.fullmatch(text) is not None

def is_item(text):
	# Checks if the given string is a valid item
	return _item_regex.fullmatch(text) is not None

def str2item(text):
	match = _item_regex.fullmatch(text)
	return Item(match.group('name'), match.group('rarity'), match.group('usable') is not None)
