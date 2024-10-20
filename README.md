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
import telebot 
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")
```



## 🌱 Quick examples

Send text on `/info` command:

```js
@bot.message_handler(commands=['info'])
def info(message:Message):
    if message.from_user.username in Pokemon.pokemons.keys():
        pok = Pokemon.pokemons[message.from_user.username]
        bot.send_message(message.chat.id, pok.info())
```


### Telegram methods:

TeleBot use standard [Telegram Bot API](https://core.telegram.org/bots/api#available-methods) method names.

##### `getMe()`

A simple method for testing your bot's auth token.

##### `answerQuery(<answerList>)`

Use this method to send `answerList` to an inline query.

##### `getFile(<file_id>)`

Use this method to get basic info about a file and prepare it for downloading.

##### `sendMessage(<chat_id>, <text>, {parseMode, replyToMessage, replyMarkup, notification, webPreview})`

Use this method to send text messages.

##### `forwardMessage(<chat_id>, <from_chat_id>, <message_id>, {notification})`

Use this method to forward messages of any kind.

##### `deleteMessage(<chat_id>, <from_message_id>)`

Use this method to delete a message. A message can only be deleted if it was sent less than 48 hours ago. Any such sent outgoing message may be deleted. Additionally, if the bot is an administrator in a group chat, it can delete any message. If the bot is an administrator of a supergroup or channel, it can delete ordinary messages from any other user, including service messages about people added or removed from the chat. Returns *True* on success.

##### `sendPhoto(<chat_id>, <file_id | path | url | buffer | stream>, {caption, fileName, serverDownload, replyToMessage, replyMarkup, notification})`

Use this method to send photos.

##### `sendAudio(<chat_id>, <file_id | path | url | buffer | stream>, {title, performer, duration, caption, fileName, serverDownload, replyToMessage, replyMarkup, notification})`

Use this method to send audio files, if you want Telegram clients to display the file as a playable voice message.

##### `sendDocument(<chat_id>, <file_id | path | url | buffer | stream>, {caption, fileName, serverDownload, replyToMessage, replyMarkup, notification})`

Use this method to send general files.

##### `sendAnimation(<chat_id>, <animation>, {caption, fileName, serverDownload, replyToMessage, replyMarkup, notification})`

Use this method to send animation files (GIF or H.264/MPEG-4 AVC video without sound).

##### `sendSticker(<chat_id>, <file_id | path | url | buffer | stream>, {fileName, serverDownload, replyToMessage, replyMarkup, notification})`

Use this method to send `.webp` stickers.

##### `sendVideo(<chat_id>, <file_id | path | url | buffer | stream>, {duration, width, height, caption, fileName, serverDownload, replyToMessage, replyMarkup, notification, supportsStreaming})`

Use this method to send video files, Telegram clients support `mp4` videos (other formats may be sent as `Document`).

##### `sendVideoNote(<chat_id>, <file_id | path | url | buffer | stream>, {duration, length, fileName, serverDownload, replyToMessage, replyMarkup, notification})`

Use this method to send video messages.

##### `sendMediaGroup(<chat_id>, <mediaList: InputMedia[]>)`

Use this method to send a group of photos or videos as an album. (Min. 2)

##### `sendVoice(<chat_id>, <file_id | path | url | buffer | stream>, {duration, caption, fileName, serverDownload, replyToMessage, replyMarkup, notification})`

Use this method to send audio files, if you want Telegram clients to display the file as a playable voice message.

##### `sendLocation(<chat_id>, [<latitude>, <longitude>], {replyToMessage, replyMarkup, notification})`

Use this method to send point on the map.

##### `sendLocation(<chat_id>, [<latitude>, <longitude>], {replyToMessage, replyMarkup, notification})`

Use this method to send point on the map.

##### `editMessageLiveLocation({chatId + messageId | inlineMessageId, latitude, longitude}, {replyMarkup})`

Use this method to edit live location messages sent by the bot or via the bot (for inline bots). A location can be edited until its live_period expires or editing is explicitly disabled by a call to stopMessageLiveLocation.

##### `stopMessageLiveLocation({chatId + messageId | inlineMessageId}, {replyMarkup})`

Use this method to stop updating a live location message sent by the bot or via the bot (for inline bots) before live_period expires.

##### `sendVenue(<chat_id>, [<latitude>, <longitude>], <title>, <address>, {foursquareId, foursquareType, replyToMessage, replyMarkup, notification})`

Use this method to send information about a venue.

##### `getStickerSet(<name>)`

Use this method to get a sticker set.

##### `uploadStickerFile(<user_id>, <file_id | path | url | buffer | stream>)`

Use this method to upload a .png file with a sticker for later use in createNewStickerSet and addStickerToSet methods (can be used multiple times).

##### `createNewStickerSet(<user_id>, <name>, <file_id | path | url | buffer | stream>, <emojis>, {containsMasks, maskPosition})`

Use this method to create new sticker set owned by a user. The bot will be able to edit the created sticker set.

##### `setChatStickerSet(<chat_id>, <sticker_set_name>)`

Use this method to set a new group sticker set for a supergroup. The bot must be an administrator in the chat for this to work and must have the appropriate admin rights.

##### `deleteChatStickerSet(<chat_id>)`

Use this method to delete a group sticker set from a supergroup. The bot must be an administrator in the chat for this to work and must have the appropriate admin rights.

##### `addStickerToSet(<user_id>, <name>, <file_id | path | url | buffer | stream>, <emojis>, {maskPosition})`

Use this method to add a new sticker to a set created by the bot.

##### `setStickerPositionInSet(<sticker>, <position>)`

Use this method to move a sticker in a set created by the bot to a specific position.

##### `deleteStickerFromSet(<sticker>)`

Use this method to delete a sticker from a set created by the bot.

##### `sendContact(<chat_id>, <number>, <firstName>, <lastName>, { replyToMessage, replyMarkup, notification})`

Use this method to send phone contacts.

##### `sendAction(<chat_id>, <action>)`

Use this method when you need to tell the user that something is happening on the bot's side. Choose one, depending on what the user is about to receive: *typing* for text messages, *upload_photo* for photos, *record_video* or *upload_video* for videos, *record_audio* or *upload_audio* for audio files, *upload_document* for general files, *find_location* for location data, *record_video_note* or *upload_video_note* for video notes.

##### `sendGame(<chat_id>, <game_short_name>, {notification, replyToMessage, replyMarkup})`

Use this method to send a game.

##### `setGameScore(<user_id>, <score>, {force, disableEditMessage, chatId, messageId, inlineMessageId})`

Use this method to set the score of the specified user in a game. On success, if the message was sent by the bot, returns the edited *Message*, otherwise returns *True*. Returns an error, if the new score is not greater than the user's current score in the chat and force is *False*.

##### `getGameHighScores(<user_id>, {chatId, messageId, inlineMessageId})`

Use this method to get data for high score tables. Will return the score of the specified user and several of his neighbours in a game. On success, returns an *Array* of *GameHighScore* objects.

##### `getUserProfilePhotos(<user_id>, {offset, limit})`

Use this method to get a list of profile pictures for a user.

##### `getFile(<file_id>)`

Use this method to get basic info about a file and prepare it for downloading.

##### `sendInvoice(<chat_id>, {title, description, payload, providerToken, startParameter, currency, sendPhoneNumberToProvider, sendEmailToProvider, prices, providerData, photo: {url, width, height}, need: {name, phoneNumber, email, shippingAddress}, isFlexible, notification, replyToMessage, replyMarkup})`

Use this method to send invoices.

##### `getChat(<chat_id>)`

Use this method to get up to date information about the chat.

##### `leaveChat(<chat_id>)`

Use this method for your bot to leave a group, supergroup or channel.

##### `getChatAdministrators(<chat_id>)`

Use this method to get a list of administrators in a chat.

##### `getChatMembersCount(<chat_id>)`

Use this method to get the number of members in a chat.

##### `getChatMember(<chat_id>, <user_id>)`

Use this method to get information about a member of a chat.

##### `kickChatMember(<chat_id>, <user_id>, {untilDate})`

Use this method to kick a user from a group or a supergroup.

##### `unbanChatMember(<chat_id>, <user_id>)`

Use this method to unban a previously kicked user in a supergroup.

##### `restrictChatMember(<chat_id>, <user_id>, {untilDate, canSendMessages, canSendMediaMessages, canSendOtherMessages, canAddWebPagePreviews})`

Use this method to restrict a user in a supergroup. The bot must be an administrator in the supergroup for this to work and must have the appropriate admin rights.

##### `promoteChatMember(<chat_id>, <user_id>, {canChangeInfo, canPostMessages, canEditMessages, canDeleteMessages, canInviteUsers, canRestrictMembers, canPinMessages, canPromoteMembers})`

Use this method to promote or demote a user in a supergroup or a channel. The bot must be an administrator in the chat for this to work and must have the appropriate admin rights.

##### `exportChatInviteLink(<chat_id>)`

Use this method to export an invite link to a supergroup or a channel. The bot must be an administrator in the chat for this to work and must have the appropriate admin rights.

##### `setChatPhoto(<chat_id>, <file_id | path | url | buffer | stream>)`

Use this method to set a new profile photo for the chat. Photos can't be changed for private chats. The bot must be an administrator in the chat for this to work and must have the appropriate admin rights.

##### `deleteChatPhoto(<chat_id>)`

Use this method to delete a chat photo. Photos can't be changed for private chats. The bot must be an administrator in the chat for this to work and must have the appropriate admin rights.

##### `setChatTitle(<chat_id>, <title>)`

Use this method to change the title of a chat. Titles can't be changed for private chats. The bot must be an administrator in the chat for this to work and must have the appropriate admin rights.

##### `setChatDescription(<chat_id>, <description>)`

Use this method to change the description of a supergroup or a channel. The bot must be an administrator in the chat for this to work and must have the appropriate admin rights.

##### `pinChatMessage(<chat_id>, <message_id>)`

Use this method to pin a message in a supergroup. The bot must be an administrator in the chat for this to work and must have the appropriate admin rights.

##### `editMessageText({chatId & messageId | inlineMsgId}, <text>)`

Use this method to edit text messages sent by the bot or via the bot (for inline bots).

##### `editMessageMedia({chatId | messageId | inlineMessageId, media: InputMedia, replyMarkup: inlineKeyboard})`

Use this method to edit animation, audio, document, photo, or video messages.

##### `editMessageCaption({chatId & messageId | inlineMsgId}, <caption>)`

Use this method to edit captions of messages sent by the bot or via the bot (for inline bots).

##### `editMessageReplyMarkup({chatId & messageId | inlineMsgId}, <replyMarkup>)`

Use this method to edit only the reply markup of messages sent by the bot or via the bot (for inline bots).

##### `answerCallbackQuery(<callback_query_id>, {text, url, showAlert, cacheTime})`

Use this method to send answers to callback queries sent from inline keyboards.

##### `answerShippingQuery(<shipping_query_id>, <ok> {shippingOptions, errorMessage})`

Use this method to reply to shipping queries.

##### `answerPreCheckoutQuery(<pre_checkout_query_id>, <ok> {errorMessage})`

Use this method to respond to such pre-checkout queries.

##### `setWebhook(<url>, <certificate>, <allowed_updates>, <max_connections>)`

Use this method to specify a url and receive incoming updates via an outgoing webhook.

##### `getWebhookInfo()`

Use this method to get current webhook status.

##### `deleteWebhook()`

Use this method to remove webhook integration if you decide to switch back to getUpdates. Returns `True` on success.

##### `sendDice(<chatId>, <emoji>)`

Use this method to send a dynamic emoji. Examples: 🎲 (default), 🎯 or 🏀.



