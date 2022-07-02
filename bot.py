import logging
import os
from random import randint

from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
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
    try:
        del context.user_data['digit']
    except KeyError:
        pass
    reply_keyboard = [['1', '2', '3', '4', '5', '6', '7', '8', '9']]
    update.message.reply_text('Выбери цифру',
                              reply_markup=ReplyKeyboardMarkup(
                                            reply_keyboard,
                                            resize_keyboard=True,
                                            one_time_keyboard=True))
    return 'new_task'


def new_task(update, context):
    logging.info('Вызов функции "new_task"')
    try:
        user_digit = context.user_data['digit']
    except KeyError:
        user_digit = int(update.message.text)
        context.user_data['digit'] = user_digit

    task_text = f'{user_digit} * {randint(2,9)}'
    context.user_data['task_text'] = task_text
    correct_answer = eval(task_text)
    context.user_data['correct_answer'] = str(correct_answer)
    context.user_data['user_answer'] = update.message.text
    context.user_data['fails'] = 0
    message_text = f'Сколько будет {task_text}? Напиши ответ'
    update.message.reply_text(message_text,
                              reply_markup=ReplyKeyboardRemove())
    return 'check_answer'


def check_answer(update, context):
    logging.info('Вызов функции "check_answer".')
    correct_answer = context.user_data['correct_answer']
    task_text = context.user_data['task_text']
    if update.message.text == correct_answer:
        context.bot.send_sticker(
            update.effective_chat.id,
            'CAACAgIAAxkBAAIb12LATcTAOGI1loMSNtyn4R75IUAMAAI' +
            'lAwACz7vUDn72oSUPiLS8KQQ')
        update.message.reply_text('Молодец! Правильный ответ!\n' +
                                  f'{task_text} = {correct_answer}.',
                                  reply_markup=task_keyboard())
        context.user_data['fails'] = 0
        return 'new_task'
    else:
        if context.user_data['fails'] < 1:
            context.bot.send_sticker(
                update.effective_chat.id,
                'CAACAgIAAxkBAAIb2WLAtBJV6j-rJWDszaGGlcXlEeEnAAIWAwACz7vUDu' +
                'Uef92K6MHnKQQ')
            update.message.reply_text('Не правильный ответ:(\n' +
                                      'Подумай еще и напиши сколько будет ' +
                                      f'{task_text}?')
            context.user_data['fails'] += 1
            return 'check_answer'
        else:
            update.message.reply_text(
                'С этим примером пока не удается справиться.\n' +
                f'Подскажу тебе правильный ответ {task_text} = ' +
                f'{correct_answer}', reply_markup=task_keyboard())
            context.user_data['fails'] = 0
            return 'new_task'


def show_keyboard(update, context):
    update.message.reply_text(
        'Чтобы начать занятие нажми кнопку "Позаниматься"',
        reply_markup=main_keyboard)


def end_class(update, context):
    update.message.reply_text('Отлично позанимались!\n' +
                              'Возвращайся поскорее:)',
                              reply_markup=main_keyboard())
    return ConversationHandler.END


def main():
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CommandHandler('change_digit', change_digit))
    dp.add_handler(ConversationHandler(
        entry_points=[MessageHandler(Filters.regex('^(Позаниматься)$'),
                                     change_digit)],
        states={
            'new_task': [MessageHandler(Filters.regex(r'^(\d+)$'),
                                        new_task),
                         MessageHandler(Filters.regex(r'^(Еще пример)$'),
                                        new_task),
                         MessageHandler(Filters.regex(r'^(Завершить)$'),
                                        end_class),
                         MessageHandler(Filters.regex(r'^(Другая цифра)$'),
                                        change_digit)],
            'check_answer': [MessageHandler(Filters.text, check_answer)],},
        fallbacks=[]
    ))
    dp.add_handler(MessageHandler(Filters.text, show_keyboard))
    logging.info('Бот стартовал')
    my_bot.start_polling()
    my_bot.idle()


if __name__ == "__main__":
    main()
