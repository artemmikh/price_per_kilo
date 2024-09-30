from dotenv import load_dotenv
from telegram.ext import CommandHandler, MessageHandler, Filters

import const
from check_environment_variables import check_tokens
from handlers import wake_up, price_per_kilo
from logger import logger

load_dotenv()


def main():
    """Основная логика работы бота."""

    logger.info('Провеверка переменных окружения')
    check_tokens()

    try:
        logger.info('Регистрация обработчиков')
        const.UPDATER.dispatcher.add_handler(CommandHandler('start', wake_up))
        const.UPDATER.dispatcher.add_handler(MessageHandler(Filters.text, price_per_kilo))

        logger.info('запуск процесса polling')
        const.UPDATER.start_polling()
        const.UPDATER.idle()

    except Exception as error:
        message = f'Сбой в работе программы: {error}'
        logger.error(message)
        # TODO тут должна быть защита от спама ошибками


if __name__ == '__main__':
    main()
