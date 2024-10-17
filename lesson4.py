import telebot
import random
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

bot = telebot.TeleBot("")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.send_message(message.chat.id, "Нажми на кнопку", reply_markup=gen_markup())
	
@bot.message_handler(commands=['mon'])
def send_welcome(message):
	bot.send_message(message.chat.id, 'расписание')
	
@bot.message_handler(commands=['dice'])
def dice(message):
	s = bot.send_dice(message.chat.id, '🎳')
	print(s.dice.value)

def gen_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(
		InlineKeyboardButton("🌚", callback_data="1"),
		InlineKeyboardButton("🌚", callback_data="2"))
    return markup

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
	print(call)
	bot.edit_message_text('1', call.message.chat.id, call.message.id)
	r = random.randint(1, 2)
	if call.data == str(r):
		bot.answer_callback_query(call.id, "Answer is Yes",show_alert=True)
	else:
		bot.answer_callback_query(call.id, "Answer is No",show_alert=True)

@bot.message_handler(content_types=['text'])
def func(message):
	if message.text == 'hello':
		bot.send_message(message.chat.id, 'hi')
	else:
		bot.send_message(message.chat.id, message.text)

bot.infinity_polling()
