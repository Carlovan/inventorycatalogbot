# A bunch of useful functions

import re

#from datatypes import Filter

def gen_filters(args):
	args = map(str.strip, args)
	args = filter(lambda x: x != '', args)
		
