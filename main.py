import telebot 
import random
from config import token
from telebot.types import Message

from logic import Pokemon,Wizard,Fighter
#------------------------------------------
# tg token bot
bot = telebot.TeleBot(token) 
#------------------------------------------
#--------------------------------------------------------------------------------
#тг бот команда
@bot.message_handler(commands=['info'])
def info(message:Message):
    if message.from_user.username in Pokemon.pokemons.keys():
        pok = Pokemon.pokemons[message.from_user.username]
        bot.send_message(message.chat.id, pok.info())
    else:
        bot.reply_to('Для начала создайте покемона командо /go')
#---------------------------------------------------------------------------------
@bot.message_handler(commands=['feed'])
def feed(message:Message):
    if message.from_user.username in Pokemon.pokemons.keys():
        pok = Pokemon.pokemons[message.from_user.username]
        bot.send_message(message.chat.id, pok.feed())
    else:
        bot.reply_to('Для начала создайте покемона командо /go')

#-----------------------------------------------------------------------------------
@bot.message_handler(commands=['go'])
def go(message:Message):
    if message.from_user.username not in Pokemon.pokemons.keys():
        x = random.randint(1,3)
        if x == 1:
            pokemon = Pokemon(message.from_user.username)
        elif x == 2:
            pokemon = Wizard(message.from_user.username)
        elif x == 3:
            pokemon = Fighter(message.from_user.username)
        bot.send_message(message.chat.id, pokemon.info())
        bot.send_photo(message.chat.id, pokemon.show_img())
    else:
        bot.reply_to(message, "Ты уже создал себе покемона")

#------------------------------------------------------------------------------------
@bot.message_handler(commands=['attack'])
def attack(message:Message):
    if not message.reply_to_message:
        bot.reply_to(message,'надо отвечать на сообщения')
        return
    if message.from_user.username not in Pokemon.pokemons.keys():
        bot.reply_to(message,'у вас не созданий покемон')
        return
    if message.reply_to_message.from_user.username not in Pokemon.pokemons.keys():
        bot.reply_to(message,'у противника нету покемона')
        return
    enemy = Pokemon.pokemons[message.reply_to_message.from_user.username]
    pok = Pokemon.pokemons[message.from_user.username]
    res = pok.attack(enemy)
    bot.send_message(message.chat.id, res)

#-----------------------------------------------------------------------------------------
bot.infinity_polling(none_stop=True)
#-----------------------------------------------------------------------------------------
