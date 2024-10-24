import os

import telegram
from dotenv import load_dotenv
from telegram.ext import Updater

load_dotenv()

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
GRAMS_PER_KILO = 1000
BOT = telegram.Bot(token=TELEGRAM_TOKEN)
UPDATER = Updater(token=TELEGRAM_TOKEN, use_context=True)
INFO_MESSAGE = (
    'Пожалуйста, отправьте в чат две цифры через пробел: '
    'сначала вес в граммах или миллилитрах, затем сумму. '
    'Используйте целые числа. Например: "820 370".')
