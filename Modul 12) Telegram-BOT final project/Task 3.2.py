import telebot

bot = telebot.TeleBot("7904619954:AAEIHV4ORrwdRxa0aDCrFV-3biaXAZ45eJA")

@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    bot.reply_to(message, "Nice meme XDD")

bot.polling(none_stop=True)
