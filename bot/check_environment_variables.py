import const
from exceptions import NoEnvironmentVariables
from logger import logger


def check_tokens():
    """Проверяет наличие обязательных переменных перед запуском бота."""
    environment_variables = [const.TELEGRAM_TOKEN]

    for variable in environment_variables:
        if not variable:
            message = (
                f'Обязательная переменная окружения {variable} недоступна')
            logger.critical(message)
            raise NoEnvironmentVariables(message)
