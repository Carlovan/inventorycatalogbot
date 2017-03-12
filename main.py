from telegram.ext import CommandHandler, Updater
import logging

import settings

# Setting up the logger
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

def echo(bot, update, args):
	update.message.reply_text(' '.join(args))

def main():
	updater = Updater(settings.token)
	dp = updater.dispatcher

	dp.add_handler(CommandHandler('echo', echo, pass_args=True))

	updater.start_polling()
	updater.idle()

if __name__ == '__main__':
	main()
