import database
from utils.filters import ItemFilter
from utils.inventory import get_messages

def run(bot, update, args):
	filters = ItemFilter.from_list(args)
	items = database.get_items(filters)
	items.sort()
	messages = get_messages(items, head='Ci sono {} oggetti che corrispondono alla tua ricerca:'.format(len(items)))
	for msg in messages:
		update.message.reply_text(msg)
