# -*- coding: utf-8  -*-
# A bunch of useful functions

import re
from .item import is_rarity
from .filters import ItemFilter

def gen_filters(args):
	args = map(str.strip, args)
	args = list(filter(lambda x: x != '', args))
	tmp = list(map(is_rarity, map(str.upper, args)))
	name_ind = tmp.index(False) if False in tmp else len(tmp)
	rarity = list(map(str.upper, args[:name_ind]))
	name = args[name_ind:]
	return ItemFilter(rarity=rarity, name=name)
