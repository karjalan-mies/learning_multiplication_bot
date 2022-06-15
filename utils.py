from telegram import ReplyKeyboardMarkup


def main_keyboard():
    return ReplyKeyboardMarkup(
        [['Позаниматься']],
        resize_keyboard=True
        )


def task_keyboard():
    return ReplyKeyboardMarkup(
        [['Еще пример', 'Другая цифра', 'Завершить']],
        resize_keyboard=True
    )
