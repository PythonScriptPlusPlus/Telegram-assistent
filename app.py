import telebot

with open('token.txt') as f:
    token = f.read()
    
bot = telebot.TeleBot(token)
print('started')

@bot.message_handler(content_types=['text'])
def replee(message):
    # bot.send_message(message.chat.id, message.text)
    # bot.send_photo(message.chat.id, photo=open('img.jpg', 'rb'))
    bot.send_document(message.chat.id,document=open('Articles_6_C.pdf','rb'))

bot.polling(non_stop=True)