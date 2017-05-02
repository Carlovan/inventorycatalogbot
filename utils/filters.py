# -*- coding: utf-8 -*-
# Filter classes

from .item import is_rarity, _rarities

class ItemFilter:
	_rarity_exceptions = {'L': list(filter(lambda x: x[0] == 'L', _rarities)),
	                      '+': list(filter(lambda x: x[-1] == '+', _rarities))}
	def __init__(self, rarity=[], name=[], usable=None):
		assert(isinstance(rarity, (tuple, list)))
		assert(isinstance(name, (tuple, list)))
		assert(type(usable) is bool or usable is None)
		self.rarity = rarity
		self.name = name
		self.usable = usable
	
	def get_sql(self, rar_field='rarity', nam_field='name'):
		rar = ' OR '.join([f'{rar_field} = %s'] * len(self.rarity))
		nam = ' AND '.join([f'LOWER({nam_field}) LIKE %s'] * len(self.name))
		sql = ''
		if rar == '' and nam == '':
			sql = '1 = 1'
		elif rar == '':
			sql = nam
		elif nam == '':
			sql = rar
		else:
			sql = f'{nam} AND ({rar})'
		if self.usable == True:
			sql += ' AND usable = true'
		elif self.usable == False:
			sql += ' AND usable = false'
		return sql

	def get_args(self):
		return tuple(list(map(lambda x: f'%{x}%', self.name)) + self.rarity)

	@staticmethod
	def from_list(args):
		# Separates the rarity from the name filters in the given list and builds a new filter
		args = map(str.strip, args) # Strip every arg
		args = list(set(args)) # Remove duplicates
		if '' in args:
			args.remove('') # Remove empty args
		tmp = list(map(is_rarity, map(str.upper, args)))
		name_ind = tmp.index(False) if False in tmp else len(tmp)
		rarity = list(map(str.upper, args[:name_ind]))
		name = args[name_ind:]
		usable = None
		if '[usabile]' in name:
			usable = True
			name.remove('[usabile]')
		for x in name:
			if x in ItemFilter._rarity_exceptions:
				name.remove(x)
				rarity += ItemFilter._rarity_exceptions[x]
		return ItemFilter(rarity=rarity, name=name, usable=usable)

class UserFilter:
	def __init__(self, username=None, userid=None):
		assert((username is not None) != (userid is not None))
		assert(username is None or type(username) is str)
		assert(userid is None or type(userid) is int)
		self.username = username
		self.userid = userid

	def get_sql(self):
		if self.username is not None:
			return 'username = %s'
		elif self.userid is not None:
			return 'id = %s'

	def get_args(self):
		if self.username is not None:
			return (self.username,)
		elif self.userid is not None:
			return (self.userid,)
