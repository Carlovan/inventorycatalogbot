import database.items
from utils.filters import ItemFilter
from telegram.ext.dispatcher import run_async
import logging
logger = logging.getLogger(__name__)

pass_args = True

@run_async
def run(bot, update, args):
	logger.info('User {} -> ({})'.format(update.message.from_user.username, ' '.join(args)))
	dbitems = database.items.DbItems()
	filt = ItemFilter.from_list(args)
	inv = dbitems.get_multiple(filt)
	inv.items.sort()
	messages = inv.get_messages(head='Ci sono {} oggetti che corrispondono alla tua ricerca:'.format(len(inv.items)))
	for msg in messages:
		update.message.reply_text(msg)
