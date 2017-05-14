from telegram.ext import CommandHandler, Updater
import logging

import commands as cmds
import messages as msgs
import settings
import utils.user

# Setting up the logger
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
	updater = Updater(settings.token)
	dp = updater.dispatcher
	settings.bot = updater.bot

	dp.add_handler(utils.user.check_handler, group=0)

	for handler in cmds.handlers:
		dp.add_handler(handler, group=1)
	for handler in msgs.handlers:
		dp.add_handler(handler, group=1)

	if settings.webhook is None:
		updater.start_polling()
		updater.bot.set_webhook(url='')
	else:
		updater.bot.set_webhook(url=settings.webhook)
		updater.start_webhook()
	logger.info('Bot started')
	updater.idle()

if __name__ == '__main__':
	main()
