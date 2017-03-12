import database
import utils

def run(bot, update, args):
	filters = utils.gen_filters(args)
	items = database.get_items(filters)
	items = utils.sort_items(items)
	items = map(str, items)
	outputs = utils.split_list(head='Ci sono {} oggetti che corrispondono alla tua ricerca'.format(len(items)))
	for out in outputs:
		update.message.reply_text(out)
