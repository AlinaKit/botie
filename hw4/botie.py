from datetime import datetime
import telebot
import random
from telebot.util import quick_markup
from telebot import types
import HELP

token = ''

bot = telebot.TeleBot(token)
my_name = 'Al'
tasks = {}

greet_txt = """\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
Use /name yourname to introduce yourself or /help to view all commands
"""

# markup = quick_markup({'help': {'callback_data': 'whatever'}})

@bot.message_handler(commands=['open_keyboard'])
def button_message(message):
    markup = bot.types.InlineKeyboardButton(resize_keyboard=True)
    item1 = bot.types.KeyboardButton("help")
    markup.add(item1)
    bot.send_message(message.chat.id, HELP.HELP)

# def welcomed(txt):
#     bot.send_message(chat_id, txt)
#
# bot.register_chat_join_request_handler(welcomed(greet_txt))

def addie(day_check, task):
    if day_check not in tasks:
      tasks[day_check] = [task]
    else:
      tasks[day_check].append(task)
    return f"Задача {task} добавлена на дату {day_check}."

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, greet_txt)

@bot.message_handler(commands=['name'])
def send_intro(message):
    global my_name
    _, my_name = str(message.text).split(maxsplit=1)
    txt = f"Nice to meet you, {my_name}!"
    bot.send_message(message.chat.id, txt)

@bot.message_handler(commands=['help'])
def help_com(message):
    bot.send_message(message.chat.id, HELP.HELP)

@bot.message_handler(commands=['add'])
def help_com(message):
    try:
        _, day_check, task = str(message.text).split(maxsplit=2)
        day_check = day_check.lower()
    except ValueError:
        txt = 'Необходимы команда, дата и задача, отделенные пробелом'
    else:
        txt = addie(day_check.lower(), task)
    bot.send_message(message.chat.id, txt)

@bot.message_handler(commands=['show'])
def help_com(message):
    try:
        _, day_check = str(message.text).split(maxsplit=1)
    except ValueError:
        txt = 'Общий список задач:'
        for day in tasks:
            if datetime.strptime(day, "%d.%m.%Y").date() == datetime.today().date():  # если сегодняшняя дата - вывести вместо числа сегодня
                txt += '\nсегодня:'
            else:
                txt += f'\n{day}:'
            for task in tasks[day]:
                txt += f'\n-{task}'
    else:
        txt = f'Задачи на {day_check}:'
        if day_check in tasks:
          for task in tasks[day_check]:
            txt = txt + '\n-' + task
        else:
            txt = 'Нет задач на этой дате.'
    bot.send_message(message.chat.id, txt)

@bot.message_handler(commands=['random'])
def help_com(message):
    try:
        _, day_check = str(message.text).split(maxsplit=1)
    except ValueError:
        txt = 'Необходима дата, отделенная от команды пробелом'
    else:
        task = HELP.randomtask()
        txt = addie(day_check, task)
    bot.send_message(message.chat.id, txt)

@bot.message_handler(commands=['stop'])
def help_com(message):
    txt = ':)'
    bot.send_message(message.chat.id, txt)

@bot.message_handler(content_types=['text'])  # принимает любой текст формата текст
def echo(message):
    if my_name in str(message.text).split():
        text = f'Я помню, что тебя зовут {my_name}'
    else:
        text = message.text
    bot.send_message(message.chat.id, text)  #  чат - текущий, текст - текст сообщения пользователя

@bot.message_handler(content_types=['animation', 'sticker', 'dice', 'audio', 'document', 'photo', 'story', 'video', 'video_note', 'voice', 'contact', 'game', 'poll', 'venue', 'location', 'invoice', 'successful_payment', 'connected_website', 'passport_data', 'web_app_data'])
def cant_hear(message):
    txt = 'Я пока умею только читать('
    bot.send_message(message.chat.id, txt)

bot.polling(non_stop=True)  # постоянно обращаться к серверу тг и не стопить программу при ошибках
