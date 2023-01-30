import telebot
import sqlite3
from db import ins

TG_tok = '5911711127:AAFGMumhR-Jz1eIgb2tKhoIDWC7VmXhyaAk'
d = sqlite3.connect('serv.db')
cur = d.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS users(int id, string name)")
bot = telebot.TeleBot(TG_tok)

@bot.message_handler(commands=['start'])

def start(message):
    id = message.chat.id
    bot.send_message(id, 'Приветики')
    print(id)
    print(ins(id))

bot.polling(none_stop=True)