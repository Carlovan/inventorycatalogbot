from telegram.ext import CommandHandler, Updater
import logging

import commands as cmds
import messages as msgs
import settings

# Setting up the logger
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
	updater = Updater(settings.token)
	dp = updater.dispatcher

	for handler in cmds.handlers:
		dp.add_handler(handler)
	for handler in msgs.handlers:
		dp.add_handler(handler)

	updater.start_polling()
	logger.info('Bot started')
	updater.idle()

if __name__ == '__main__':
	main()
