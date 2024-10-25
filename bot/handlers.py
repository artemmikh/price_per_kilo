from const import INFO_MESSAGE, GRAMS_PER_KILO
from utils import check_message, parse_message, send_message


def wake_up(update, context):
    """Обработчик команды /start. Отправляет приветственное сообщение с
    информацией."""
    send_message(update, context, message=f'Добро пожаловать! {INFO_MESSAGE}')


def price_per_kilo(update, context):
    """Обрабатывает сообщение о цене и отправляет цену за килограмм."""
    message = update.message.text
    if check_message(message) is None:
        send_message(update, context,
                     message=(
                         'Проверьте сообщение. '
                         'Каждое число должно быть не длиннее 15 символов. '
                         f'{INFO_MESSAGE}'))
        return
    grams, price = parse_message(message)
    send_message(update, context, message=(
        'Цена за килограмм или литр – '
        f'{int(price / (grams / GRAMS_PER_KILO))} рублей'))
