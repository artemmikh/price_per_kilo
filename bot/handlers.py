from bot.test import message
from bot.utils import check_message, parse_message
from utils import send_message

INFO_MESSAGE = ('Пожалуйста, отправьте в чат две цифры через пробел, '
                'напишите сначала вес в граммах, затем сумму. '
                'Используйте целые числа. Например "820 370".')


def wake_up(update, context):
    send_message(update, context,
                 # TODO При добавлении float изменить сообщение
                 message=(f'Добро пожаловать! {INFO_MESSAGE}'))


def price_per_kilo(update, context):
    message = update.message.text
    if check_message(message) is None:
        send_message(update, context, f'Проверьте сообщение. {INFO_MESSAGE}')
        return
    grams, price = parse_message(message)
    send_message(update, context, message=f'Цена за килограмм – {int(price / (grams / 1000))} рублей')
