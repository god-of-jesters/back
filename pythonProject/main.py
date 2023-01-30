import telebot
import sqlite3
from db import ins

TG_tok = '5911711127:AAFGMumhR-Jz1eIgb2tKhoIDWC7VmXhyaAk'
bot = telebot.TeleBot(TG_tok)

@bot.message_handler(commands=['start'])

def start(message):
    id = message.chat.id
    bot.send_message(id, 'Приветики')
    print(id)
    print(ins(id))

bot.polling(none_stop=True)