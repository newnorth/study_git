import telebot
import random
from telebot import types

token = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

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

# добавление в список
def add_todo(date, task):
    if date in tasks:
        tasks[date].append(task)
    else:
        tasks[date] = []
        tasks[date].append(task)

# кнопки
@bot.message_handler(commands=['start'])
def start(message):
  markup = types.ReplyKeyboardMarkup()
  buttonA = types.KeyboardButton('/help')
#  buttonB = types.KeyboardButton('/add')
  markup.row(buttonA)
#  markup.row(buttonB)

#  markup = types.InlineKeyboardMarkup()
#  buttonA = types.InlineKeyboardButton('Помощь', callback_data=str(help))
#  buttonB = types.InlineKeyboardButton('Добавить задачу', callback_data='/add')
#  buttonC = types.InlineKeyboardButton('Просмотреть задачи', callback_data='/show')
#  markup.row(buttonA)
#  markup.row(buttonC)

#  buttonC = types.KeyboardButton('/exit')
#  buttonD = types.KeyboardButton('/show')
#  markup.row(buttonA, buttonB)
#  markup.row(buttonC, buttonD)
  bot.send_message(message.chat.id, 'Здравсвуйте! Рады видеть вас в нашей задачнице.', reply_markup=markup)

# вывод списка команд
@bot.message_handler(commands=['help'])
def help(message):
    print(message.text)
    bot.send_message(message.chat.id, help_list)


@bot.message_handler(commands=['add'])
def add(message):
    print(message.text)
    command = message.text.split(maxsplit=2)
    if len(command) == 1:
        output = 'Укажите дату и задачу.'
    elif len(command) == 2:
        output = 'Укажите задачу.'
    else:
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

@bot.message_handler(commands=['exit'])
def escape(message):
    print(message.text)
    text = 'Будем рады увидеть вас еще раз, не забывайте про задачи!'
    bot.send_message(message.chat.id, text)
    exit
    bot.stop_polling()


# Постоянное обращение к серверам телеграмма
bot.polling(none_stop=True)
