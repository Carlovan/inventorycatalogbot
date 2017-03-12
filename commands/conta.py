import database
import utils

def run(bot, update, args):
	filters = utils.gen_filters(args)
	count = database.count_items(filters)
	update.message.reply_text('Ci sono {} oggetti che corrispondono alla tua ricerca.'.format(count))
