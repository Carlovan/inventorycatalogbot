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
		rar = ' OR '.join(['{} = %s'.format(rar_field)] * len(self.rarity))
		nam = ' AND '.join(['LOWER({}) LIKE LOWER(%s)'.format(nam_field)] * len(self.name))
		sql = ''
		if rar == '' and nam == '':
			sql = '1 = 1'
		elif rar == '':
			sql = nam
		elif nam == '':
			sql = rar
		else:
			sql = '{} AND ({})'.format(nam, rar)
		if self.usable == True:
			sql += ' AND usable = true'
		elif self.usable == False:
			sql += ' AND usable = false'
		return sql

	def get_args(self):
		return tuple(list(map(lambda x: '%{}%'.format(x), self.name)) + self.rarity)

	def get_lambda(self):
		if self.rarity == []:
			return lambda item: all([x.lower() in item.name.lower() for x in self.name])
		else:
			return lambda item: item.rarity in self.rarity and all([x.lower() in item.name.lower() for x in self.name])

	@staticmethod
	def from_list(args):
		# Separates the rarity from the name filters in the given list and builds a new filter
		args = map(str.strip, args) # Strip every arg
		rarity = []
		name = []
		usable = None
		still_rarity = True
		for a in args:
			a = a.upper()
			if still_rarity:
				if is_rarity(a):
					rarity.append(a)
				elif a.upper() in ItemFilter._rarity_exceptions:
					rarity += ItemFilter._rarity_exceptions[a]
				else:
					still_rarity = False
			if not still_rarity:
				if a == '[USABILE]': # This is uppercase due to a = a.upper()
					usable = True
				else:
					name.append(a)  # The filter is case insensitive
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
