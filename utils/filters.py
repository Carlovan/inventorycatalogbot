# -*- coding: utf-8 -*-
# Filter classes

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

