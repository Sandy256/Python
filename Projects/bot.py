import telebot
import config
from telebot import types


bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('welcome.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)

    #keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Кнопка 1 👻")
    item2 = types.KeyboardButton("Кнопка 2 👹")

    markup.add(item1, item2)

    bot.send_message(message.chat.id, "Привет {0.first_name}!\nЯ - {1.first_name}\nКакой то текст"
                     .format(message.from_user, bot.get_me()), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def Reackt(message):
    if message.chat.type == 'private':
        if message.text == 'Кнопка 1 👻':
            bot.send_message(message.chat.id, "Вы нажали кнопку 1")
        elif message.text == 'Кнопка 2 👹':
            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("inline кнопка 1", callback_data='1')
            item2 = types.InlineKeyboardButton("inline кнопка 2", callback_data='2')

            markup.add(item1, item2)

            bot.send_message(message.chat.id, 'Вы нажали кнопку 2', reply_markup=markup)
        else:
            bot.send_message(message.chat.id, "Ну все, ты огребаешь 😡")


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == '1':
                bot.send_message(call.message.chat.id, 'Вы нажали Inline кнопку 1')
            elif call.data == '2':
                bot.send_message(call.message.chat.id, 'Вы нажали Inline кнопку 2')

            # remove inline buttons
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Кнопка 2 👹",
                                  reply_markup=None)

            # show alert
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="ТЕСТОВОЕ УВЕДОМЛЕНИЕ!")

    except Exception as e:
        print(repr(e))

#RUN
bot.polling(none_stop=True)