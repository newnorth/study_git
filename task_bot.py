import telebot
import random

token = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, help_list)

@bot.message_handler(commands=['add'])
def add(message):
    command = message.text.split(maxsplit=2)
    date = command[1].lower()
    task = command[2]
    todo_list(date, task)
    text = 'Задача ' + task + ' добавлена на дату ' + date
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['random'])
def random_add(message):
    date = 'сегодня'
    task = random.choice(random_list)
    todo_list(date, task)
    text = 'Задача ' + task + ' добавлена на дату ' + date
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['show', 'print'])
def show(message):
    command = message.text.split(maxsplit=1)
    date = command[0].lower()
    text = ''
    if date in tasks:
        text = date.upper() + '\n'
        for task in tasks[date]:
            text = text + '[]' + task + '\n'
    else:
        text = 'Задач на эту дату нет.'
    bot.send_message(message.chat.id, text)

def todo_list(time_date, task):
    if time_date in tasks:
        tasks[time_date].append(task)
    else:
        tasks[time_date] = []
        tasks[time_date].append(task)

help_list = """ 
/help - напечатать справку по программе
/show - показать задачи на день
/add - добавить задачу
/random - добавляет случайную задачу текущий день
/exit - выход
"""
random_list = ['Изучить алгоритмы', 'Выучить SQL', 'Найти работу']

tasks = {}

bot.polling(none_stop=True)
