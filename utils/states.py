# -*- coding: utf-8 -*-

import enum

class UserState(enum.Enum):
	NONE = None
	CONFRONTA = 'confronta'
	CONFRONTA_ADDING = 'confadding'
	CONTAINV = 'containv'
	CONTAINV_ADDING = 'containvadding'
	CONFRONTAINV_A = 'confrontainva'
	CONFRONTAINV_A_ADDING = 'confrontainvaddinga'
	CONFRONTAINV_B = 'confrontainvb'
	CONFRONTAINV_B_ADDING = 'confrontainvaddingb'

class ItemState(enum.Enum):
	NONE = None
	CONFRONTA = 'confronta'
	CONTAINV = 'containv'
	CONFRONTAINV_A = 'confrontainva'
	CONFRONTAINV_B = 'confrontainvb'
