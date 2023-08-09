import telebot
import sqlite3
from  telebot import types as ty

bot = telebot.TeleBot('6131885047:AAG80IIrvKZpC4FGiszDV-hdIanxtcGTpag')
db = sqlite3.connect('persone.db', check_same_thread=False)
cur = db.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS persons (id int, max_hp int, power int, money int, money_cost int)')

class Persone:
    def __init__(self, id, max_hp, hp, pow):
        self.id = id
        self.max_hp = max_hp
        self.hp = hp
        self.pow = pow
        self.money = 10
        self.money_cost = 1

class en:
    def __init__(self, max_hp, hp, pow, money):
        self.max_hp = max_hp
        self.hp = hp
        self.pow = pow
        self.money = money

def reg(id, pers):
    cur.execute(f'INSERT INTO persons VALUES({id}, {pers.max_hp}, {pers.pow}, {pers.money}, {pers.money_cost})')
    print("Ну зареган")

def take_id():
    cur.execute('SELECT id FROM persons')
    return cur.fetchall()

@bot.message_handler(commands= ['start', 'menu'])
def main_menu(message):
    mar = ty.ReplyKeyboardMarkup(resize_keyboard=True)
    info = ty.KeyboardButton('Игроки')
    game = ty.KeyboardButton('Играть')
    mar.add(game, info)
    print("Я дошел до этого")
    bot.send_message(message.chat.id, 'Главное меню', reply_markup= mar)

@bot.message_handler()
def game(message):
    print("И до этого")
    ids = take_id()
    if message.text == 'Играть' and message.from_user.id in ids:
        mar = ty.ReplyKeyboardMarkup(resize_keyboard=True)
        atac = ty.KeyboardButton('Драться')
        hil = ty.KeyboardButton('Захилиться')
        upgrade = ty.KeyboardButton('Улучшиться')
        mar.add(atac, hil, upgrade)
        bot.send_message(message.chat.id, 'Главное меню', reply_markup=mar)
    else:
        reg(message.from_user.id, Persone(message.from_user.id, 100, 100, 5))
bot.polling(none_stop= True)
