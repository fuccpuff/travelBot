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
        SELECT * FROM users WHERE travel_type = ? AND chat_id != ?''', (criteria['travel_type'], chat_id))
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

def select_companions(chat_id, companions, bot):
    if not companions:
        bot.send_message(chat_id, "К сожалению, не найдено подходящих попутчиков.")
        return

    keyboard = types.InlineKeyboardMarkup(row_width=1)
    for companion in companions:
        companion_name = f"{companion[2]}"
        callback_data = f"select_companion:{companion[0]}"
        keyboard.add(types.InlineKeyboardButton(text=companion_name, callback_data=callback_data))

    keyboard.add(types.InlineKeyboardButton(text="Готово", callback_data="finish_selecting_companions"))
    bot.send_message(chat_id, "Выберите попутчиков, с которыми хотите связаться:", reply_markup=keyboard)
