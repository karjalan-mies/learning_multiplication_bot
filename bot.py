import logging
import os

from telegram.ext import (CommandHandler, ConversationHandler, Filters,
                          MessageHandler, Updater)

from handlers import (change_digit, check_answer, end_class, greet_user,
                      new_task, show_keyboard, wrong_answer)

logging.basicConfig(filename='bot.log', level=logging.INFO)

API_TOKEN = os.environ.get('API_TOKEN')
my_bot = Updater(API_TOKEN, use_context=True)
dp = my_bot.dispatcher


def main():
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CommandHandler('change_digit', change_digit))
    dp.add_handler(ConversationHandler(
        entry_points=[MessageHandler(Filters.regex('^(Позаниматься)$'),
                                     change_digit)],
        states={
            'new_task': [MessageHandler(Filters.regex(
                                        r'^(\d+|Еще пример|X)$'),
                                        new_task),
                         MessageHandler(Filters.regex(r'^(Завершить)$'),
                                        end_class),
                         MessageHandler(Filters.regex(r'^(Выбрать цифру)$'),
                                        change_digit)],
            'check_answer': [MessageHandler(Filters.text, check_answer)]},
        fallbacks=[
            MessageHandler(Filters.text | Filters.photo | Filters.video |
                       Filters.document | Filters.location, wrong_answer)
        ]
    ))
    dp.add_handler(MessageHandler(Filters.text, show_keyboard))
    logging.info('Бот стартовал')
    my_bot.start_polling()
    my_bot.idle()


if __name__ == "__main__":
    main()
