from telegram.ext import CommandHandler
from dotenv import load_dotenv

import const
from logger import logger
from check import check_tokens
from handlers import comands

load_dotenv()


def main():
    """Основная логика работы бота."""

    logger.info('Провеверка переменных окружения')
    check_tokens()

    try:
        logger.info('Регистрация обработчиков')
        for comand in comands.keys():
            const.UPDATER.dispatcher.add_handler(
                CommandHandler(comand, comands[comand]))

        logger.info('запуск процесса polling')
        const.UPDATER.start_polling()
        const.UPDATER.idle()

    except Exception as error:
        message = f'Сбой в работе программы: {error}'
        logger.error(message)
        # тут должна быть защита от спама ошибками


if __name__ == '__main__':
    main()
