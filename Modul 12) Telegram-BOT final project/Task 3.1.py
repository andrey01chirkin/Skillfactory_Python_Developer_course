import telebot

bot = telebot.TeleBot("7904619954:AAEIHV4ORrwdRxa0aDCrFV-3biaXAZ45eJA")

@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    bot.send_message(message.chat.id, f"Привет {message.chat.username}")

@bot.message_handler(content_types=['document', 'audio'])
def handle_docs_audio(message):
    pass


bot.polling(none_stop=True)