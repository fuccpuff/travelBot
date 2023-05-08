# main.py

import telebot
from telebot import types
import config
from create_profile import create_profile

# Создаем экземпляр бота
bot = telebot.TeleBot(config.TOKEN)


# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start(message):
    # Создаем клавиатуру
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

    # Добавляем кнопки на клавиатуру
    keyboard.add('Создать профиль')
    keyboard.add('Редактировать профиль')
    keyboard.add('Поиск попутчиков')
    keyboard.add('Мои попутчики')
    keyboard.add('Удалить профиль')
    keyboard.add('Создать групповой чат')

    # Отправляем приветственное сообщение с клавиатурой
    bot.send_message(
        message.chat.id,
        "Привет! Я Travel Buddy, твой путешественный помощник. "
        "Выбери действие с помощью кнопок ниже:",
        reply_markup=keyboard
    )


@bot.message_handler(content_types=['text'])
def handle_text_messages(message):
    if message.text == 'Создать профиль':
        create_profile(message, bot)
    # Добавьте обработчики для других функций бота здесь


# Запускаем бота
if __name__ == '__main__':
    bot.infinity_polling()
