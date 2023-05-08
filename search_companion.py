import sqlite3
from telebot import types

def search_companions(chat_id, criteria):
    conn = sqlite3.connect('travel_buddy.db')
    cursor = conn.cursor()

    # Отладочный код
    cursor.execute('SELECT * FROM users')
    all_users = cursor.fetchall()
    print("Все пользователи:")
    for user in all_users:
        print(user)
    # Конец отладочного кода

    cursor.execute('''
        SELECT * FROM users
        WHERE travel_type = ? AND chat_id != ?
    ''', (criteria['travel_type'], chat_id))
    companions = cursor.fetchall()
    conn.close()
    return companions



def search_companion_handler(message, bot):
    chat_id = message.chat.id

    # Создаем инлайн-клавиатуру для выбора типа отдыха
    keyboard = types.InlineKeyboardMarkup()
    travel_types = ['Активный отдых', 'Пляжный отдых', 'Городской туризм', 'Культурный туризм', 'Экскурсии']
    for t_type in travel_types:
        keyboard.add(types.InlineKeyboardButton(text=t_type, callback_data=f"search_criteria:travel_type:{t_type}"))

    bot.send_message(chat_id, 'Выберите тип отдыха, по которому хотите найти попутчика:', reply_markup=keyboard)