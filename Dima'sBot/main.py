import telebot
from telebot import types
import sqlite3
from telebot import types as ty

TG_tok = '5911711127:AAFGMumhR-Jz1eIgb2tKhoIDWC7VmXhyaAk'
bot = telebot.TeleBot(TG_tok)
db = sqlite3.connect('serv.db', check_same_thread=False)
cur = db.cursor()


class Persone:

    def __init__(self, lvl, exp, max_hp, armor, at, bag):
        self.lvl = lvl
        self.exp = exp
        self.hp = max_hp
        self.max_hp = max_hp
        self.armor = armor
        self.at = at
        self.bag = bag


class Bag:
    def __init__(self, money, seed_1, seed_2, seed_3, seed_1_planted, seed_2_planted, seed_3_planted):
        self.money = money
        self.seed_1 = seed_1
        self.seed_2 = seed_2
        self.seed_3 = seed_3
        self.seed_1_planted = seed_1_planted
        self.seed_2_planted = seed_2_planted
        self.seed_3_planted = seed_3_planted


class Enemy:
    def __init__(self, hp, armor, seed_level, money, at):
        self.hp = hp
        self.armor = armor
        self.seed_level = seed_level
        self.at = at
        self.money = money


def processor(mes, bot):
    global cur

    pers = try_reg(mes.from_user.id, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, db, cur)
    if mes.text.isdigit():

    else:
        if mes.text == 'Информация':
            bot.send_message(mes.chat.id, f'ID: {mes.from_user.id}')

        elif mes.text == 'Играть':
            ty.ReplyKeyboardRemove()
            mar = ty.ReplyKeyboardMarkup(resize_keyboard=True)
            find_enemy = ty.KeyboardButton('Найти врага')
            market = ty.KeyboardButton('Магазин')
            posadka = ty.KeyboardButton('Посадить растение')
            inventory = ty.KeyboardButton('Сумка')
            back = ty.KeyboardButton('Меню')
            mar.add(find_enemy, market, inventory, posadka, back)

            bot.send_message(mes.chat.id, 'Сейчас поиграем в игру)', reply_markup=mar)

        elif mes.text == 'Меню':
            menu(bot, mes)

        elif mes.text == 'Найти врага':
            fight(pers, Enemy(1, 1, 1, 1, 1), bot, mes)

        elif mes.text == 'Сумка':
            bag_def(pers, mes, bot)

        elif mes.text == 'Магазин':
            market(bot, mes)

        elif mes.text == 'Продать':
            market(bot, mes)

def menu(bot, message):
    global cur

    pers = try_reg(message.from_user.id, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, db, cur)
    mar = ty.ReplyKeyboardMarkup(resize_keyboard=True)
    info = ty.KeyboardButton('Информация')
    game = ty.KeyboardButton('Играть')
    table = ty.KeyboardButton('Таблица лидеров')
    profile = ty.KeyboardButton('Профиль')
    mar.add(info, game, table, profile)
    bot.send_message(message.chat.id, f'{message.chat.id}')
    bot.send_message(message.chat.id, 'Добро пожаловать в главное меню:\n', reply_markup=mar)


def insert(mes: int, cur):
    cur.execute("CREATE TABLE IF NOT EXISTS users(id INT, lvl INT, exp INT, hp INT, armor INT, at INT, money INT"
                ", seed_1 INT, seed_2 INT, seed_3 INT, seed_1_planted INT, seed_2_planted INT, seed_3_planted INT)")

    pers = cur.execute(
        f"SELECT id INT, lvl INT, exp INT, hp INT, armor INT, at INT, money INT, seed_1 INT, seed_2 INT, seed_3 INT,"
        f" seed_1_planted INT, seed_2_planted INT, seed_3_planted INT FROM USERS WHERE id={mes}"
    ).fetchall()[0]
    return Persone(pers[1], pers[2], pers[3], pers[4], pers[5], Bag(pers[6], pers[7], pers[8], pers[9], pers[10],
                                                                    pers[11], pers[12]))


def try_reg(mes: int, lvl, exp, hp, armor, at, money, seed_1, seed_2, seed_3,
            seed_1_planted, seed_2_planted, seed_3_planted, d, cur):
    cur.execute("CREATE TABLE IF NOT EXISTS users(id INT, lvl INT, exp INT, hp INT, armor INT, at INT, money INT"
                ", seed_1 INT, seed_2 INT, seed_3 INT, seed_1_planted INT, seed_2_planted INT, seed_3_planted INT)")
    d.commit()

    ids = [item[0] for item in cur.execute("SELECT id FROM users").fetchall()]
    print(ids)
    if mes not in ids:
        cur.execute(
            f"INSERT INTO users VALUES({mes}, {lvl}, {exp}, {hp}, {armor}, {at}, {money}, {seed_1}, {seed_2}, {seed_3},"
            f" {seed_1_planted}, {seed_2_planted}, {seed_3_planted})")
        d.commit()
        return Persone(1, 1, 1, 1, 1, Bag(1, 1, 1, 1, 1, 1, 1))
    else:
        return insert(mes, cur)


def bag_def(pers, mes, bot):
    bag = pers.bag
    bot.send_message(mes.chat.id, f'      Сумка      \nМонет: {bag.money}\n Семян 1 ур: {bag.seed_1}\n Семян 2 ур: {bag.seed_2}\n Семян 3 ур: {bag.seed_3}')


def save_battle(pers, mes):
    global cur, db

    cur.execute(f'UPDATE users SET lvl = {pers.lvl}, exp = {pers.exp}, money = {pers.bag.money}, seed_1 = {pers.bag.seed_1}, seed_1 = {pers.bag.seed_2}, seed_1 = {pers.bag.seed_3} WHERE id = {mes.from_user.id}')
    db.commit()


def market(bot, mes):
    if mes.text == 'Магазин':
        ty.ReplyKeyboardRemove()
        mar = ty.ReplyKeyboardMarkup()
        buy = ty.KeyboardButton('Купить')
        sel = ty.KeyboardButton('Продать')
        mar.add(buy, sel)
        bot.send_message(mes.chat.id, 'Добро пожаловать в магазин', reply_markup=mar)

    else:
        ty.ReplyKeyboardRemove()
        mar = ty.ReplyKeyboardMarkup()
        s_1 = ty.KeyboardButton('Семя 1 ур')
        s_2 = ty.KeyboardButton('Семя 2 ур')
        s_3 = ty.KeyboardButton('Семя 3 ур')
        mar.add(s_1, s_3, s_2)
        if mes.text == 'Купить':
            market_op = 'Купить'
        else:
            market_op = 'Продать'



def fight(pers, en, bot, mes):
    while True:
        if pers.hp > 0 and en.hp > 0:
            damage = pers.at * (1 - en.armor // 100)
            en.hp -= round(damage)
            bot.send_message(mes.chat.id, f'Вы нанесли {damage} урона!\n'
                                          f'Здоровье противника: {en.hp}\n')
            if en.hp > 0:
                damage = en.at * (1 - pers.armor // 100)
                pers.hp -= round(damage)
                bot.send_message(mes.chat.id, f'Вам нанесли {damage} урона!\n'
                                              f'Ваше здоровье: {pers.hp}\n')
        elif en.hp <= 0:
            bot.send_message(mes.chat.id, f'Победа!\n'
                                          f'Вы получили:\n'
                                          f'Монеты: {en.money}\n'
                                          f'Саженец {en.seed_level} уровня\n')
            bag = pers.bag
            bag.money += en.money
            if en.seed_level == 1:
                bag.seed_1 += 1
            elif en.seed_level == 2:
                bag.seed_2 += 1
            elif en.seed_level == 3:
                bag.seed_3 += 1
            pers.bag = bag
            break
        elif pers.hp <= 0:
            bot.send_message(mes.chat.id, f'Вы погибли!\n'
                                          f'Саженцы и монеты из вашего рюкзака потеряны!')
            bag = pers.bag
            bag.money = 0
            bag.seed_1 = 0
            bag.seed_2 = 0
            bag.seed_3 = 0
            pers.bag = bag
            break

    save_battle(pers, mes)

@bot.message_handler(commands=['start', 'menu'])
def user_text(message):
    menu(bot, message)


@bot.message_handler(content_types=['text'])
def cal(mes):
    processor(mes, bot)


@bot.message_handler(commands=['market'])
def cal_m(mes):
    market(bot, mes)


bot.polling(none_stop=True)
