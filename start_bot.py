import telebot
from  decouple import  config
from telebot import  types


bot = telebot.TeleBot(config("TOKEN_BOT"))

@bot.message_handler(commands=["start","hi"])
def get_start_message(message):
    full_name = f" {message.from_user.first_name} !!!"
    text = f"Welcom {full_name}"
    #bot.send_message(message.chat.id, text)
    bot.reply_to(message, text)


@bot.message_handler(content_types=["text"])
def get_message(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    #full_name = f" {message.from_user.first_name} !!!"
    if message.text.lower() == "меню":
        text = "Выберите пожалуйста: "
        btn1 = types.InlineKeyboardButton("Tea", callback_data="tea")
        #btn1 = types.InlineKeyboardButton("Tea", url="https://en.wikipedia.org/wiki/Tea")
        btn2 = types.InlineKeyboardButton("Cofe", callback_data="cofe")
        markup.add(btn1, btn2)
    bot.send_message(message.chat.id, text, reply_markup=markup)
    #bot.reply_to(message, text)



@bot.callback_query_handler(func=lambda call: True)
def get_callback_data(call):
    murkup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    text = ""
    if call.data == "tea":
        text = "tea"
        btn1 = types.KeyboardButton("Black")
        btn2 = types.KeyboardButton("Green")
        btn3 = types.KeyboardButton("Yellow")
        murkup.add(btn1, btn2, btn3)

    if call.data == "cofe":
        text = "coffe"
        btn1 = types.KeyboardButton("Late")
        btn2 = types.KeyboardButton("Capuchino")
        btn3 = types.KeyboardButton("Arabica")
        btn4 = types.KeyboardButton("Americano")
        murkup.add(btn1, btn2, btn3, btn4)
    bot.send_message(call.message.chat.id, f" Choose {text} please: ", reply_markup=murkup)


bot.polling()