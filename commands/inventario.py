import database.items
from utils.filters import ItemFilter

def run(bot, update, args):
	filt = ItemFilter.from_list(args)
	inv = database.items.get_multiple(filt)
	inv.items.sort()
	messages = inv.get_messages(head='Ci sono {} oggetti che corrispondono alla tua ricerca:'.format(len(inv.items)))
	for msg in messages:
		update.message.reply_text(msg)
