import sqlite3
from telebot import types

def edit_profile(message, user_data, bot):
    chat_id = message.chat.id
    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    markup.add('Имя', 'Возраст', 'Пол', 'Страны и города', 'Тип отдыха', 'Контактная информация', 'Готово')
    msg = bot.send_message(chat_id, 'Выберите поле, которое хотите изменить:', reply_markup=markup)
    bot.register_next_step_handler(msg, process_edit_choice, user_data, bot)


def process_edit_choice(message, user_data, bot):
    chat_id = message.chat.id
    choice = message.text
    if choice == 'Имя':
        msg = bot.send_message(chat_id, 'Введите ваше новое имя:')
        bot.register_next_step_handler(msg, process_new_name, user_data, bot)
    elif choice == 'Возраст':
        msg = bot.send_message(chat_id, 'Введите ваш новый возраст:')
        bot.register_next_step_handler(msg, process_new_age)
    elif choice == 'Пол':
        msg = bot.send_message(chat_id, 'Введите ваш новый пол (Мужской/Женский):')
        bot.register_next_step_handler(msg, process_new_gender)
    elif choice == 'Страны и города':
        msg = bot.send_message(chat_id, 'Введите страны и города, в которых вы были или хотите посетить (через '
                                        'запятую):')
        bot.register_next_step_handler(msg, process_new_countries_cities)
    elif choice == 'Тип отдыха':
        msg = bot.send_message(chat_id, 'Введите ваш предпочитаемый тип отдыха:')
        bot.register_next_step_handler(msg, process_new_vacation_type)
    elif choice == 'Контактная информация':
        msg = bot.send_message(chat_id, 'Введите вашу новую контактную информацию (телефон и/или email):')
        bot.register_next_step_handler(msg, process_new_contact_info)
    elif choice == 'Готово':
        bot.send_message(chat_id, 'Ваши изменения сохранены.')

def process_new_name(message, user_data, bot):
    chat_id = message.chat.id
    new_name = message.text
    save_name_to_db(chat_id, new_name)
    bot.send_message(chat_id, 'Ваше имя успешно обновлено.')
    edit_profile(message, user_data, bot)

def process_new_age(message, user_data, bot):
    chat_id = message.chat.id
    new_age = message.text
    save_age_to_db(chat_id, new_age)
    bot.send_message(chat_id, 'Ваш возраст успешно обновлен.')
    edit_profile(message, user_data, bot)

def process_new_gender(message, user_data, bot):
    chat_id = message.chat.id
    new_gender = message.text
    save_gender_to_db(chat_id, new_gender)
    bot.send_message(chat_id, 'Ваш пол успешно обновлен.')
    edit_profile(message, user_data, bot)

def process_new_countries_cities(message, user_data, bot):
    chat_id = message.chat.id
    new_countries_cities = message.text
    save_countries_cities_to_db(chat_id, new_countries_cities)
    bot.send_message(chat_id, 'Ваши страны и города успешно обновлены.')
    edit_profile(message, user_data, bot)

def process_new_vacation_type(message, user_data, bot):
    chat_id = message.chat.id
    new_vacation_type = message.text
    save_vacation_type_to_db(chat_id, new_vacation_type)
    bot.send_message(chat_id, 'Ваш тип отдыха успешно обновлен.')
    edit_profile(message, user_data, bot)

def process_new_contact_info(message, user_data, bot):
    chat_id = message.chat.id
    new_contact_info = message.text
    save_contact_info_to_db(chat_id, new_contact_info)
    bot.send_message(chat_id, 'Ваша контактная информация успешно обновлена.')
    edit_profile(message, user_data, bot)

def save_name_to_db(chat_id, name):
    conn = sqlite3.connect('travel_buddy.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET name=? WHERE chat_id=?", (name, chat_id))
    conn.commit()
    conn.close()

def save_age_to_db(chat_id, age):
    conn = sqlite3.connect('travel_buddy.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET age=? WHERE chat_id=?", (age, chat_id))
    conn.commit()
    conn.close()

def save_gender_to_db(chat_id, gender):
    conn = sqlite3.connect('travel_buddy.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET gender=? WHERE chat_id=?", (gender, chat_id))
    conn.commit()
    conn.close()

def save_countries_cities_to_db(chat_id, countries_cities):
    conn = sqlite3.connect('travel_buddy.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET countries_cities=? WHERE chat_id=?", (countries_cities, chat_id))
    conn.commit()
    conn.close()

def save_vacation_type_to_db(chat_id, vacation_type):
    conn = sqlite3.connect('travel_buddy.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET vacation_type=? WHERE chat_id=?", (vacation_type, chat_id))
    conn.commit()
    conn.close()

def save_contact_info_to_db(chat_id, contact_info):
    conn = sqlite3.connect('travel_buddy.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET contact_info=? WHERE chat_id=?", (contact_info, chat_id))
    conn.commit()
    conn.close()

