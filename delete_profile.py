from telebot import types
from database import delete_profile_from_db


def delete_profile(message, bot):
    chat_id = message.chat.id
    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    markup.add('Да', 'Нет')
    msg = bot.send_message(chat_id, 'Вы уверены, что хотите удалить свой профиль? Все данные будут потеряны.', reply_markup=markup)
    bot.register_next_step_handler(msg, process_delete_profile_confirmation, bot)



def process_delete_profile_confirmation(message, bot):
    chat_id = message.chat.id
    if message.text == 'Да':
        delete_profile_from_db(chat_id)
        bot.send_message(chat_id, 'Ваш профиль успешно удален.')
    elif message.text == 'Нет':
        bot.send_message(chat_id, 'Отмена удаления профиля.')
    else:
        bot.send_message(chat_id, 'Неправильный выбор. Пожалуйста, выберите "Да" или "Нет".')
        delete_profile(message, bot)

