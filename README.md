   - ***TG BOT IN PYTHON***
 
 
 

 
 
 
 
 
 This tg bot is made on the basis of python, the telebot library was used
 
 if there are any errors that you have noticed give feedback

- [**The pyTelegramBotAPI documentation**](https://pytba.readthedocs.io/ru/latest/index.html)
- [**Python Telegram bot api**](https://pythonrepo.com/repo/eternnoir-pyTelegramBotAPI-python-third-party-apis-wrappers)

- __My Discord - 12veseliy12__ 




![2024-10-20_13-05-11](https://github.com/user-attachments/assets/c1081add-3742-45df-96e0-7a205f9925b0)














## 🔨 Installation

```
pip install telebot
```



## 🕹 Usage

Import `telebot` module and create a new bot object:

```js
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")
```
