from random import randint

for_correct = [
    'Верно!',
    'Отлично!',
    'Молодец!',
    'Так держать!'
]

for_wrong = [
    'Не правильно'
]


def get_message_text(correct_answer):
    if correct_answer:
        return for_correct[randint(1, len(for_correct)-1)]
    else:
        return for_wrong[randint(1, len(for_wrong)-1)]
