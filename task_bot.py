import telebot
import random

token = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

bot = telebot.TeleBot(token)

help_list = """ 
/help - напечатать справку по программе
/show - показать задачи на день
/add - добавить задачу
/random - добавляет случайную задачу текущий день
/exit - выход
"""

random_list = ['Изучить алгоритмы', 'Выучить SQL', 'Найти работу']

tasks = {}


def add_todo(date, task):
    if date in tasks:
        tasks[date].append(task)
    else:
        tasks[date] = []
        tasks[date].append(task)


# вывод списка команд
@bot.message_handler(commands=['help'])
def help(message):
    print(message.text)
    bot.send_message(message.chat.id, help_list)


@bot.message_handler(commands=['add'])
def add(message):
    print(message.text)
    command = message.text.split(maxsplit=2)
    date = command[1].lower()
    task = command[2]
    add_todo(date, task)
    output = 'Задача ' + task + ' добавлена на дату ' + date
    bot.send_message(message.chat.id, output)


@bot.message_handler(commands=['random'])
def random_add(message):
    print(message.text)
    date = 'сегодня'
    task = random.choice(random_list)
    add_todo(date, task)
    output = 'Задача ' + task + ' добавлена на дату ' + date
    bot.send_message(message.chat.id, output)


@bot.message_handler(commands=['show'])
def show(message):
    print(message.text)
    command = message.text.split(maxsplit=1)
    text = ''
    if len(command) == 1:
        text = 'Укажите дату.'
    else:
        date = command[1].lower()
        if date in tasks:
            text = date.upper() + '\n'
            for task in tasks[date]:
                text = text + '[]' + task + '\n'
        else:
            text = 'Задач на эту дату нет.'
    bot.send_message(message.chat.id, text)

# Постоянное обращение к серверам телеграмма
bot.polling(none_stop=True)
