import os
from dotenv import load_dotenv
import telegram
from telegram.ext import Updater

load_dotenv()

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
MY_TELEGRAM_CHAT_ID = os.getenv('MY_TELEGRAM_CHAT_ID')

BOT = telegram.Bot(token=TELEGRAM_TOKEN)
UPDATER = Updater(token=TELEGRAM_TOKEN, use_context=True)
