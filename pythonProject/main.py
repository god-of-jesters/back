import telebot
from telebot import types
import sqlite3
from comands import *
from db import *

TG_tok = '5911711127:AAFGMumhR-Jz1eIgb2tKhoIDWC7VmXhyaAk'
bot = telebot.TeleBot(TG_tok)
db = sqlite3.connect('serv.db' , check_same_thread=False)
cur = db.cursor()

@bot.message_handler(commands= ['start', 'menu'])
def user_text(message):
    menu(bot, message)

@bot.callback_query_handler(func = lambda call:True)
def re(call):
    if call.data == 'yes':
        mar = types.ReplyKeyboardMarkup(resize_keyboard= True)
        item = types.KeyboardButton('Мой ID')
        item2 = types.KeyboardButton('Ник')
        mar.add(item, item2)

        bot.send_message(call.message.chat.id, 'Перейдите', reply_markup= mar)
    else:
        bot.send_message(call.message.chat.id, 'Покеда')

@bot.message_handler(content_types= ['text'])
def cal(mes):
    processor(mes, bot)
#     if mes.text == 'Мой ID':
#         bot.send_message(mes.chat.id, f'ID: {mes.from_user.id}')
bot.polling(none_stop=True)