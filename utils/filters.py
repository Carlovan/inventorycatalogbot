# -*- coding: utf-8 -*-
# Filter classes

from .item import is_rarity

class ItemFilter:
	def __init__(self, rarity=[], name=[]):
		assert(isinstance(rarity, (tuple, list)))
		assert(isinstance(name, (tuple, list)))
		self.rarity = rarity
		self.name = name
	
	def get_sql(self, rar_field='rarity', nam_field='name'):
		rar = ' OR '.join([f'{rar_field} = %s'] * len(self.rarity))
		nam = ' AND '.join([f'LOWER({nam_field}) LIKE %s'] * len(self.name))
		if rar == '' and nam == '':
			return '1 = 1'
		elif rar == '':
			return nam
		elif nam == '':
			return rar
		else:
			return f'{nam} AND ({rar})'

	def get_args(self):
		return tuple(list(map(lambda x: f'%{x}%', self.name)) + self.rarity)

	@staticmethod
	def from_list(args):
		# Separates the rarity from the name filters in the given list and builds a new filter
		args = map(str.strip, args)
		args = list(filter(lambda x: x != '', args))
		tmp = list(map(is_rarity, map(str.upper, args)))
		name_ind = tmp.index(False) if False in tmp else len(tmp)
		rarity = list(map(str.upper, args[:name_ind]))
		name = args[name_ind:]
		return ItemFilter(rarity=rarity, name=name)
