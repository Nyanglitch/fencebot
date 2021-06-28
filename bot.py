from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
#from telegram.ext import CommandHandler
import sys
import logging

with open('token.txt', 'r') as f:
    TOKEN = f.readline().strip()

updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm not working... aaaa, naibal))0)")

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

def make_a_fence(text):
    ftext = ""
    upperize = 0
    for char in text:
        if char == " ":
            ftext += char
            continue

        if upperize % 2 == 0:
            ftext += char.upper()
        else:
            ftext += char.lower()

        upperize += 1
    
    return ftext

def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
    text=make_a_fence(update.message.text))

echo_handler = MessageHandler(Filters.text & (~Filters.command),
    echo)

dispatcher.add_handler(echo_handler)

updater.start_polling()
