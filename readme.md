# Learning_multiplication_bot

## Это TelegramBot-помощник для малышей, изучающих таблицу умножения

## Что он умеет?
* Бот задает примеры на умножение для выбранной цифры или по всей таблице умножения
* Проверяет ответы пользователя и сообщает результат проверки
* В случае правильного ответа Бот предлагает перейти к следующему примеру, выбору цифр или завершить занятие
* В случае двух неправильных ответов подряд Бот сообщает правильный ответ и предлагает перейти к следующему примеру, выбору цифр или завершить занятие
* При выборе цифры в диапазоне от 2 до 9 Бот задает примеры, в которых в качестве первого множителя используется выбранная цифра, а второй множитель выбирается в случайном порядке в диапазоне от 2 до 9
* Бот запоминает какие примеры он уже задавл и до тех пор пока не будут использованы в качестве второго множителя все цифры в диапазоне от 2 до 9 - примеры не будут повторяться
* При выборе в качестве первого множителя буквы "X" Бот задает примеры, в которых оба множителя выбираются в случайном порядке в диапазоне от 2 до 9

![Screenshot 1](https://github.com/karjalan-mies/learning_multiplication_bot/blob/master/images/001.png)

![Screenshot 2](https://github.com/karjalan-mies/learning_multiplication_bot/blob/master/images/002.png)

![Screenshot 3](https://github.com/karjalan-mies/learning_multiplication_bot/blob/master/images/003.png)

![Screenshot 4](https://github.com/karjalan-mies/learning_multiplication_bot/blob/master/images/004.png)

![Screenshot 5](https://github.com/karjalan-mies/learning_multiplication_bot/blob/master/images/005.png)

![Screenshot 6](https://github.com/karjalan-mies/learning_multiplication_bot/blob/master/images/006.png)

![Screenshot 7](https://github.com/karjalan-mies/learning_multiplication_bot/blob/master/images/007.png)

[Проверить свои силы в умножении](https://t.me/learning_multiplication_bot)

## Сборка репозитория и локальный запуск
1. Запустите консоль
2. Перейдите в каталог с проектами или создайте его при необходимости
3. Выполните команду:

    ```
    git clone https://github.com/karjalan-mies/learning_multiplication_bot
    ```
4. Перейдите в каталог **"learning_multiplication_bot"**
5. Создайте виртуальное окружение командой:
    ```
    python3 -m venv env
    ```
6. Добавьте переменные окружения

    6.1. Для Windows:

    6.1.1 Откройте файл ```"\env\Scripts\activate.bat"``` и добавте в него строку:
    ```
    set API_TOKEN=ваш_токет_для_телеграм
    ```
    6.1.2 Откройте файл ```"\env\Scripts\activate"``` и добавьте в него строки:
    ```
    set API_TOKEN='ваш_токет_для_телеграм'
    export API_TOKEN
    ```
    6.2 Для Linux:
    
    6.2.1 Откройте файл ```/env/bin/activate``` и добавьте в него строку:
    ```
    API_TOKEN='ваш_токет_для_телеграм'
    export API_TOKEN
    ```

7. Активируйте виртульаное окружение:

    7.1 Для Windows:
    ```
    env\Scripts\activate
    ```

    7.2 Для Linux:
    ```
    Source /env/bin/activate
    ```

8. Установите зависимости командой:
    ```
    pip install -r requirements.txt
    ```

9. Запустите бота командой:
    ```
    python3 bot.py
    ```
