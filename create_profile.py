from telebot import types
import sqlite3

# Вспомогательный класс для хранения данных профиля пользователя
class UserProfile:
    def __init__(self):
        self.name = None
        self.age = None
        self.gender = None
        self.countries_cities = None
        self.travel_type = None
        self.phone_number = None
        self.email = None

# Вспомогательный словарь для хранения состояний пользователей
user_states = {}

# Функция для сохранения данных профиля в базе данных
def save_user_profile(profile):
    conn = sqlite3.connect('travel_buddy.db')
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO users (name, age, gender, countries_cities, travel_type, phone_number, email)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (profile.name, profile.age, profile.gender, profile.countries_cities, profile.travel_type, profile.phone_number, profile.email))

    conn.commit()
    conn.close()

# Функция для создания профиля пользователя
def create_profile(message, bot):
    chat_id = message.chat.id

    # Если пользователь не в словаре состояний, добавляем его и начинаем процесс создания профиля
    if chat_id not in user_states:
        user_states[chat_id] = {'state': 'GET_NAME', 'profile': UserProfile()}
        bot.send_message(chat_id, 'Пожалуйста, введите ваше имя и фамилию:')
    else:
        # Обрабатываем состояние пользователя и запрашиваем следующую информацию
        state = user_states[chat_id]['state']
        profile = user_states[chat_id]['profile']

        if state == 'GET_NAME':
            profile.name = message.text
            user_states[chat_id]['state'] = 'GET_AGE'
            bot.send_message(chat_id, 'Пожалуйста, введите ваш возраст:')

        elif state == 'GET_AGE':
            profile.age = message.text
            user_states[chat_id]['state'] = 'GET_GENDER'
            bot.send_message(chat_id, 'Пожалуйста, введите ваш пол:')

        elif state == 'GET_GENDER':
            profile.gender = message.text
            user_states[chat_id]['state'] = 'GET_COUNTRIES_CITIES'
            bot.send_message(chat_id, 'Пожалуйста, введите страны или города, в которых вы были или хотите посетить (через запятую):')

        elif state == 'GET_COUNTRIES_CITIES':
            profile.countries_cities = message.text
            user_states[chat_id]['state'] = 'GET_TRAVEL_TYPE'
            bot.send_message(chat_id, 'Пожалуйста, введите ваш предпочитаемый тип отдыха:')

        elif state == 'GET_TRAVEL_TYPE':
            profile.travel_type = message.text
            user_states[chat_id]['state'] = 'GET_PHONE_NUMBER'
            bot.send_message(chat_id, 'Пожалуйста, введите ваш номер телефона:')

        elif state == 'GET_PHONE_NUMBER':
            profile.phone_number = message.text
            user_states[chat_id]['state'] = 'GET_EMAIL'
            bot.send_message(chat_id, 'Пожалуйста, введите вашу почту:')
        elif state == 'GET_EMAIL':
            profile.email = message.text
            # Сохраняем данные профиля в базе данных
            save_user_profile(profile)

            # Завершаем процесс создания профиля и удаляем пользователя из словаря состояний
            del user_states[chat_id]
            bot.send_message(chat_id, 'Ваш профиль успешно создан!')
