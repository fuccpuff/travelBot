# create_profile.py
import sqlite3

class UserProfile:
    def __init__(self):
        self.name = None
        self.age = None
        self.gender = None
        self.countries_cities = None
        self.travel_type = None
        self.contact_info = None

# Функция для сохранения профиля в базу данных
def save_profile_to_db(profile, chat_id):
    conn = sqlite3.connect('travel_buddy.db')
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO users (chat_id, name, age, gender, countries_cities, travel_type, contact_info)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (chat_id, profile.name, profile.age, profile.gender, profile.countries_cities, profile.travel_type, profile.contact_info))

    conn.commit()
    conn.close()

# Функция для обработки шагов создания профиля
def process_create_profile_step(user_states, message, bot):
    chat_id = message.chat.id
    state = user_states[chat_id]['state']
    profile = user_states[chat_id]['profile']

    if state == 'GET_NAME':
        profile.name = message.text
        user_states[chat_id]['state'] = 'GET_AGE'
        bot.send_message(chat_id, 'Введите ваш возраст:')
    elif state == 'GET_AGE':
        profile.age = int(message.text)
        user_states[chat_id]['state'] = 'GET_GENDER'
        bot.send_message(chat_id, 'Введите ваш пол (М/Ж):')
    elif state == 'GET_GENDER':
        profile.gender = message.text
        user_states[chat_id]['state'] = 'GET_COUNTRIES_CITIES'
        bot.send_message(chat_id, 'Введите страны или города, в которых вы были или хотите посетить:')
    elif state == 'GET_COUNTRIES_CITIES':
        profile.countries_cities = message.text
        user_states[chat_id]['state'] = 'GET_TRAVEL_TYPE'
        bot.send_message(chat_id, 'Введите предпочитаемый тип отдыха:')
    elif state == 'GET_TRAVEL_TYPE':
        profile.travel_type = message.text
        user_states[chat_id]['state'] = 'GET_CONTACT_INFO'
        bot.send_message(chat_id, 'Введите контактную информацию (номер телефона, электронная почта):')
    elif state == 'GET_CONTACT_INFO':
        profile.contact_info = message.text

        # Сохраняем профиль в базу данных и удаляем состояние пользователя
        save_profile_to_db(profile, chat_id)
        del user_states[chat_id]

        bot.send_message(chat_id, 'Ваш профиль успешно создан!')

# Функция для начала создания профиля
def create_profile(user_states, message, bot):
    chat_id = message.chat.id

    # Создаем профиль пользователя и сохраняем его состояние
    user_states[chat_id] = {
        'state': 'GET_NAME',
        'profile': UserProfile()
    }

    bot.send_message(chat_id, 'Введите ваше имя и фамилию:')
