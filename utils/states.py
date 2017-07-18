# -*- coding: utf-8 -*-

import enum

class UserState(enum.Enum):
	NONE = None
	CONFRONTA = 'confronta'
	CONFRONTA_ADDING = 'confadding'
	CONTAINV = 'containv'
	CONTAINV_ADDING = 'containvadding'

class ItemState(enum.Enum):
	NONE = None
	CONFRONTA = 'confronta'
	CONTAINV = 'containv'
