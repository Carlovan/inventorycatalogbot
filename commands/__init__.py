import importlib
from telegram.ext import CommandHandler

cmd_list = ['echo', 'conta', 'inventario']

handlers = []
for c in cmd_list:
	m = importlib.import_module('.'+c, __name__)
	args = m.run.__code__.co_argcount == 3 # If the run function takes 3 arguments, the args from the command are required
	handlers.append(CommandHandler(c, m.run, pass_args=args))
