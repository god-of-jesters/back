from telebot import types as ty

def processor(mes, bot):
    if mes.text == 'Информация':
        bot.send_message(mes.chat.id, f'ID: {mes.from_user.id}')

def menu(bot, message):
    mar = ty.ReplyKeyboardMarkup(resize_keyboard=True)
    info = ty.KeyboardButton('Информация')
    game = ty.KeyboardButton('Играть')
    table = ty.KeyboardButton('Таблица лидеров')
    profile = ty.KeyboardButton('Профиль')
    mar.add(info, game, table, profile)

    bot.send_message(message.chat.id, 'Добро пожаловать в главное меню:\n', reply_markup= mar)
