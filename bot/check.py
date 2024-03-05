import const
from logger import logger
from exceptions import (
    NoEnvironmentVariables
)


def check_tokens():
    environment_variables = [
        const.TELEGRAM_TOKEN,
        const.MY_TELEGRAM_CHAT_ID]

    for variable in environment_variables:
        if not variable:
            message = (
                f'Обязательная переменная окружения {variable} недоступна')
            logger.critical(message)
            raise NoEnvironmentVariables(message)
