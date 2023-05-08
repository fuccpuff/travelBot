import telebot
from telebot import types

# Импортируйте свои функции здесь, например:
# from create_profile import create_profile
# from edit_profile import edit_profile
# from delete_profile import delete_profile
# from find_companions import find_companions
# from create_group_chat import create_group_chat

from config import API_TOKEN
from database import init_database

bot = telebot.TeleBot(API_TOKEN)

def create_main_keyboard():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

    # Добавьте кнопки для всех функций
    keyboard.add(types.KeyboardButton('Создать профиль'))
    keyboard.add(types.KeyboardButton('Редактировать профиль'))
    keyboard.add(types.KeyboardButton('Поиск попутчиков'))
    keyboard.add(types.KeyboardButton('Мои попутчики'))
    keyboard.add(types.KeyboardButton('Удалить профиль'))
    keyboard.add(types.KeyboardButton('Создать групповой чат'))

    return keyboard

@bot.message_handler(commands=['start'])
def start(message):
    user = message.from_user
    bot.send_message(message.chat.id, f'Привет, {user.first_name}!\nЯ - твой бот для путешествий.')

# Здесь добавьте свои обработчики для функций бота, например:
# bot.message_handler(commands=['create_profile'])(create_profile)
# bot.message_handler(commands=['edit_profile'])(edit_profile)
# bot.message_handler(commands=['delete_profile'])(delete_profile)
# bot.message_handler(commands=['find_companions'])(find_companions)
# bot.message_handler(commands=['create_group_chat'])(create_group_chat)

if __name__ == '__main__':
    # Инициализация базы данных
    init_database()

    # Запуск бота
    bot.polling(none_stop=True)
