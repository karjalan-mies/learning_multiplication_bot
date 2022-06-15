import logging
import os
from random import randint

from telegram import ReplyKeyboardMarkup
from telegram.ext import (CommandHandler, ConversationHandler, Filters,
                          MessageHandler, Updater)

from utils import main_keyboard, task_keyboard

logging.basicConfig(filename='bot.log', level=logging.INFO)

API_TOKEN = os.environ.get('API_TOKEN')

my_bot = Updater(API_TOKEN, use_context=True)
dp = my_bot.dispatcher


def greet_user(update, context):
    update.message.reply_text(
        '''Привет! Чтобы проверить свои знания нажми кнопку "Позаниматься''',
        reply_markup=main_keyboard())


def change_digit(update, context):
    reply_keyboard = [['1', '2', '3', '4', '5', '6', '7', '8', '9']]
    update.message.reply_text('Выбери цифру',
                              reply_markup=ReplyKeyboardMarkup
                              (
                                reply_keyboard,
                                resize_keyboard=True,
                                one_time_keyboard=True
                              )
                              )
    return 'new_task'


def new_task(update, context):
    logging.info('Вызов функции "new_task"')
    user_digit = int(update.message.text)
    context.user_data['digit'] = user_digit
    task_text = f'{user_digit} * {randint(1,9)}'
    context.user_data['task_text'] = task_text
    correct_answer = eval(task_text)
    context.user_data['correct_answer'] = correct_answer
    message_text = f'Сколько будет {task_text}? Напиши ответ'
    update.message.reply_text(message_text, reply_markup=task_keyboard())
    return 'check_answer'


def check_answer(update, context):
    logging.info('Вызов функции "check_answer"')
    # print('correct_answer' + str(update.user_data['correct_answer']))
    # print('user_answer' + context.message.text)
    if str(context.user_data['correct_answer']) == str(update.message.text):
        update.message.reply_text('Правильный ответ!',
                                  reply_markup=task_keyboard())
        return 'new_task'
    else:
        update.message.reply_text(
            f'Неверно! Попробуй еше.\n{context.user_data["task_text"]}',
            reply_markup=task_keyboard())


def whats_next(update, context):
    logging.info('Вызов функции "whats_next"')
    if update.message.text == 'Еще пример':
        return 'new_task'


def main():
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CommandHandler('new_task', new_task))
    dp.add_handler(CommandHandler('change_digit', change_digit))
    dp.add_handler(ConversationHandler(
        entry_points=[MessageHandler(Filters.regex('^(Позаниматься)$'),
                                     change_digit)],
        states={'new_task': [MessageHandler(Filters.regex('^(\d)$'),
                                            new_task)],
                'check_answer': [MessageHandler(Filters.regex('^(\d{1,2})$'),
                                                check_answer)],
                'whats_next': [MessageHandler(Filters.text, whats_next)]},
        fallbacks=[]
    ))
    logging.info('Бот стартовал')
    my_bot.start_polling()
    my_bot.idle()


if __name__ == "__main__":
    main()
