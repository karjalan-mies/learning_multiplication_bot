import logging
from random import randint

from telegram import ReplyKeyboardRemove
from telegram.ext import ConversationHandler

from answers import get_message_text
from keyboards import main_keyboard, task_keyboard, change_digit_keyboard
from stickers import get_sticker
from utils import get_x


def greet_user(update, context):
    update.message.reply_text(
        'Привет! Чтобы проверить свои знания нажми кнопку "Позаниматься"',
        reply_markup=main_keyboard())


def change_digit(update, context):
    try:
        del context.user_data['digit']
    except Exception as e:
        logging.info(e)
    update.message.reply_text(
        'Нажми кнопку с цифрой, если хочешь решать ' +
        'примеры на одну цифру или нажми кнопку с ' +
        'буквой "X", чтобы решать примеры на разные цифры',
        reply_markup=change_digit_keyboard())
    return 'new_task'


def new_task(update, context):
    logging.info('Вызов функции "new_task"')
    try:
        list_of_numbers = context.user_data['list_of_numbers']
    except KeyError:
        list_of_numbers = []
        context.user_data['list_of_numbers'] = list_of_numbers

    try:
        user_digit = context.user_data['digit']
    except KeyError:
        user_digit = update.message.text
        context.user_data['digit'] = user_digit
    x2,  context.user_data['list_of_numbers'] = get_x(
                                        context.user_data['list_of_numbers'])
    
    task_text = f'{user_digit} * {x2}'
    if user_digit == 'X':
        task_text = f'{randint(2,9)} * {randint(2,9)}'

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
        context.bot.send_sticker(update.effective_chat.id, get_sticker(True))
        update.message.reply_text(get_message_text(True) +
                                  f'\n{task_text} = {correct_answer}.',
                                  reply_markup=task_keyboard())
        context.user_data['fails'] = 0
        return 'new_task'
    else:
        if context.user_data['fails'] < 1:
            context.bot.send_sticker(update.effective_chat.id,
                                     get_sticker(False))
            update.message.reply_text(get_message_text(False) +
                                      '\nПодумай еще и напиши сколько будет ' +
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
        reply_markup=main_keyboard())


def wrong_answer(update, context):
    update.message.reply_text('Я тебя не понимаю. Повтори ввод.')


def end_class(update, context):
    update.message.reply_text('Отлично позанимались!\n' +
                              'Возвращайся поскорее:)',
                              reply_markup=main_keyboard())
    return ConversationHandler.END
