# -*- coding: utf-8 -*-
# This file contains useful function to work with inventories

from .item import Item, is_item
import database.items
import database.users
import database.user_items
import utils
from utils.filters import UserFilter, ItemFilter
from utils.states import UserState, ItemState
import logging
logger = logging.getLogger(__name__)

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
	def ensure_data(self):
		# Reads the data from the DB
		dbitems = database.items.DbItems()
		dbusers = database.users.DbUsers()
		if self.user:
			self.user = dbusers.get_single(UserFilter(userid=self.user.userid))
		for i in range(len(self.items)):
			self.items[i] = dbitems.get_single(self.items[i].name)
	def filter_items(self, filt):
		assert(type(filt) is ItemFilter or callable(filt))
		if type(filt) is ItemFilter:
			filt = filt.get_lambda()
		items = list(filter(filt, self.items))
		return Inventory(items, self.user)
	@staticmethod
	def parse(text, *args, **kwargs):
		# Parses an inventory message
		def f(s):
			#num = s.rfind('x')
			#return s[1:num].strip()
			return s.strip()
		lines = map(f, text.split('\n'))
		items = []
		for line in lines:
			if is_item(line):
				items.append(Item.from_string(line))
		return Inventory(items, *args, **kwargs)
	def __sub__(self, other):
		if not type(other) is Inventory:
			return NotImplemented
		items = []
		for i in self.items:
			if i not in other.items:
				items.append(i)
		return Inventory(items, self.user)
def add(inv):
	# Adds a list of items to the database
	assert(type(inv) is Inventory)
	dbitems = database.items.DbItems()
	items = list(filter(lambda item: dbitems.get_single(item.name) is None, inv.items))
	items = []
	for item in inv.items:
		dbi = dbitems.get_single(item.name)
		if dbi is None:
			items.append(item)
		elif dbi != item:
			utils.send_admin('Errore:\nvecchio "{}"\nnuovo "{}"'.format(str(dbi), str(item)))
	dbitems.add(items)
	return len(items)

def add_user_items(inv, user_stateadding, item_state):
	dbusers = database.users.DbUsers()
	dbuseritems = database.user_items.DbUserItems()
	user_state = inv.user.state
	inv.user.state = user_stateadding
	dbusers.update(inv.user)
	dbuseritems.add_inventory(inv, item_state)
	inv.user.state = user_state
	dbusers.update(inv.user)
	return 'Ok. Usa /fine, /annulla o manda altri oggetti.'


def received(inv):
	# Function to call when an inventory is received from the user.
	# Then this function will choose what action to perform on that inventory
	assert(type(inv) is Inventory)
	count = add(inv)
	inv.ensure_data()
	try:
		if inv.user.state == UserState.NONE:
			logger.info('User {} added {} items'.format(inv.user.username, count))
			return f'Hai aggiunto {count} oggetti.'
		elif inv.user.state == UserState.CONFRONTA:
			logger.info('User {} added items to confronta'.format(inv.user.username))
			return add_user_items(inv, UserState.CONFRONTA_ADDING, ItemState.CONFRONTA)
		elif inv.user.state == UserState.CONTAINV:
			logger.info('User {} added item to containv'.format(inv.user.username))
			return add_user_items(inv, UserState.CONTAINV_ADDING, ItemState.CONTAINV)
		elif inv.user.state == UserState.CONFRONTAINV_A:
			logger.info('User {} added items to confrontainv_a'.format(inv.user.username))
			return add_user_items(inv, UserState.CONFRONTAINV_A_ADDING, ItemState.CONFRONTAINV_A)
		elif inv.user.state == UserState.CONFRONTAINV_B:
			logger.info('User {} added items to confrontainv_b'.format(inv.user.username))
			return add_user_items(inv, UserState.CONFRONTAINV_B_ADDING, ItemState.CONFRONTAINV_B)
		elif inv.user.state in [UserState.CONFRONTA_ADDING, UserState.CONTAINV_ADDING, UserState.CONFRONTAINV_A_ADDING, UserState.CONFRONTAINV_B_ADDING]:
			return 'Aspetta il messaggio di conferma!'
	except Exception as ex:
		print(ex, flush=True)
