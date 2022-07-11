import telebot
import random
import time
from telebot import types

TOKEN="5372125273:AAGUk_sqGfdmdklL0bdpxgNijDUPQ8MmVnM"
bot=telebot.TeleBot(TOKEN)
markup1 = telebot.types.InlineKeyboardMarkup()
markup1_item1 = telebot.types.InlineKeyboardButton('1️⃣', callback_data='1')
markup1_item2 = telebot.types.InlineKeyboardButton('2️⃣', callback_data='2')
markup1_item3 = telebot.types.InlineKeyboardButton('3️⃣', callback_data='3')
markup1_item4 = telebot.types.InlineKeyboardButton('4️⃣', callback_data='4')
markup1_item5 = telebot.types.InlineKeyboardButton('5️⃣', callback_data='5')
markup1_item6 = telebot.types.InlineKeyboardButton('6️⃣', callback_data='6')
markup1.add(markup1_item1,markup1_item2,markup1_item3, markup1_item4,markup1_item5,markup1_item6) 

@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("🔪Украинская рулетка🔪")
    item2 = types.KeyboardButton("Ben🐶")
    item3 = types.KeyboardButton("Удача🍀")
    markup.add(item1, item2,item3)
    markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item_1 = types.KeyboardButton("⚽️")
    item_2 = types.KeyboardButton("🏀")
    item_3 = types.KeyboardButton("🎲")
    markup2.add(item_1, item_2,item_3)
    bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот.".format(message.from_user, bot.get_me()),
        parse_mode='html', reply_markup=markup)
    
@bot.message_handler(content_types=['text'])
def lalala(message):
     if message.chat.type=='private':
        def answer(message):
                if message.text=="Путин хуйло?":
                    gif_ben_yes = open("elements/ben_yes.gif", 'rb')
                    bot.send_animation(message.chat.id, gif_ben_yes)
                    audio_yes = open('elements/say_yes.mp3', 'rb')
                    bot.send_audio(message.chat.id, audio_yes)
                    return 1
                answer_ben=random.choice(["yes","no"])
                if answer_ben=="yes":
                    gif_ben_yes = open("elements/ben_yes.gif", 'rb')
                    bot.send_animation(message.chat.id, gif_ben_yes)
                    audio_yes = open('elements/say_yes.mp3', 'rb')
                    bot.send_audio(message.chat.id, audio_yes)
                else:
                    gif_ben_no = open("elements/ben_no.gif", 'rb')
                    bot.send_animation(message.chat.id, gif_ben_no)
                    audio_no = open('elements/say_no.mp3', 'rb')
                    bot.send_audio(message.chat.id, audio_no)
                
                
        if "?" in message.text:
            answer(message)
        if message.text =="Ben🐶":
            question=bot.send_message(message.chat.id, "Задайте вопрос, обьязательно со знаком впроса в конце")
            gif_ben = open("elements/ben_ben.gif", 'rb')
            bot.send_animation(message.chat.id, gif_ben)
            audio_ben = open('elements/say_ben.mp3', 'rb')
            bot.send_audio(message.chat.id, audio_ben)
            bot.register_next_step_handler(question, answer)
            
        if message.text=="Удача🍀":
            bot.send_message(message.chat.id, "В разработке...")
        if message.text=="🔪Украинская рулетка🔪":
            bot.send_message(message.chat.id, "Игра началась👀")
            gif = open("elements/photo.gif", 'rb')
            bot.send_animation(message.chat.id, gif)
            bot.send_message(message.chat.id, "Выбери одну из кнопок", reply_markup=markup1)
            
@bot.callback_query_handler(func=lambda call: True)
def callback_func(call):
    if call.message:
                
        while True:
            ran_num=str(random.randint(1,6))
            if call.data!=ran_num:
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="💥")
                time.sleep(2.5)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Бум, тебя убили, ты проиграл")
                break
            else:
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="🎉")
                time.sleep(2.5)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="На этот раз тебе повезло")
                break

bot.polling(none_stop=True, interval=0)
