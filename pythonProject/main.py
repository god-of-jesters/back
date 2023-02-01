import telebot
import sqlite3
from db import *

TG_tok = '5911711127:AAFGMumhR-Jz1eIgb2tKhoIDWC7VmXhyaAk'
bot = telebot.TeleBot(TG_tok)
db = sqlite3.connect('serv.db' , check_same_thread=False)
cur = db.cursor()

@bot.message_handler(commands=['start'])

def start(message):
    id = message.chat.id
    bot.send_message(id, 'Приветики')

@bot.message_handler(commands=['register'])
def register(reg):
    if try_reg(reg.chat.id, cur):
        bot.send_message(reg.chat.id, 'Вы уже зарегистрированы')
    else:
        bot.send_message(reg.chat.id, 'Регистрация прошла успешно)')
        ins(reg.chat.id, reg.from_user.first_name, reg.from_user.last_name, db, cur)

bot.polling(none_stop=True)