from utils import send_message


def wake_up(update, context):
    send_message(update, context,
                 # TODO При добавлении float изменить сообщение
                 message=('Добро пожаловать! Пожалуйста, отправьте в чат две цифры через пробел, '
                          'напишите сначала вес в граммах, затем сумму. '
                          'Используйте целые числа. Например "820 370".'))


def price_per_kilo(update, context):
    # TODO добавить проверку соответствия патерну
    # TODO распарсить сообщение
    # TODO добавить обработку float
    # price = 0
    # grams = 0
    # text =  f'Цена за килограмм – {int(price / (grams / 1000))} руб'

    send_message(update, context, message='это текст из price_per_kilo')
