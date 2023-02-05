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

# @bot.callback_query_handler(func = lambda call:True)
# def re(call):
# Вызов обработчика сообщений
@bot.message_handler(content_types= ['text'])
def cal(mes):
    processor(mes, bot)

bot.polling(none_stop = True)