import telebot
bot = telebot.TeleBot("7180354541:AAFcZXjOXDUCadf_MHV73gF-ttNq4gOTEDE")
@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "привет, я помогу тебе если не знаешь чем заняться с утра")
@bot.message_handler(commands=["чем_заняться"])
def things_to_do(message):
    bot.send_message(message.chat.id, "выпей чашечку чая")
bot.infinity_polling()