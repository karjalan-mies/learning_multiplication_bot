from telegram import ReplyKeyboardMarkup


def main_keyboard():
    return ReplyKeyboardMarkup(
        [['Позаниматься']],
        resize_keyboard=True
        )


def task_keyboard():
    return ReplyKeyboardMarkup(
        [['Еще пример', 'Выбрать цифру', 'Завершить']],
        resize_keyboard=True
    )


def change_digit_keyboard():
    return ReplyKeyboardMarkup(
        [['2', '3', '4', '5', '6', '7', '8', '9', 'X']],
        resize_keyboard=True,
        one_time_keyboard=True
    )
