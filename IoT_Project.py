
#*** SENDING DATA TO ADAFRUIT ****

import os

ADAFRUIT_IO_USERNAME = os.getenv('ADAFRUIT_IO_USERNAME')  #Use your own ADAFRUIT_IO_USERNAME
ADAFRUIT_IO_KEY = os.getenv('ADAFRUIT_IO_KEY')            #Use your own Adafruit Active Key

from Adafruit_IO import Client, Feed
from Adafruit_IO import Data

aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

from Adafruit_IO import Client,Data

#*** TELEGRAM BOT ****

from telegram.ext import Updater,CommandHandler
from telegram.ext import MessageHandler, Filters           
import logging

u = Updater('1361391561:AAHH1-JmCX0-QWWDvmXrSZGZz5lIPY9jiBQ')   #Use your Telegram Token HTTP API
dp = u.dispatcher 

logging.basicConfig(format='%(asctime)s - %(time)s - %(levelname)s - %(message)s', level=logging.INFO)

# for introduction
def start(bot, update):
    chat_id=update.message.chat_id
    bot.send_message(chat_id, text="I'm a bot, please talk to me!")

start_handler = CommandHandler('start', start)
dp.add_handler(start_handler)

#for switching on lights
def on(bot,update):
      value = Data(value=1)
      send_value = aio.create_data('bot',value)
      chat_id = update.message.chat_id
      bot.send_message(chat_id,text="Okay! Lights turned on.")
      bot.send_photo(chat_id, photo = 'https://woodbineia.com/wp-content/uploads/2017/10/Light-bulb-vector-210x300.jpg')
      
dp.add_handler(CommandHandler('on',on))

#for switching off lights
def off(bot,update):
      value = Data(value=0)
      send_value = aio.create_data('bot',value)
      chat_id = update.message.chat_id
      bot.send_message(chat_id,text="Okay! Lights turned off.")
      bot.send_photo(chat_id, photo = 'https://image.shutterstock.com/image-illustration/3d-rendering-clear-light-bulb-260nw-699554389.jpg')

dp.add_handler(CommandHandler('off',off))

# for unknown commands
def unknown(bot,update):
      chat_id = update.message.chat_id
      bot.send_message(chat_id,text="Sorry, I didn't understand that command.")

dp.add_handler(MessageHandler(Filters.command, unknown))

u.start_polling()  # To start the bot, run.
u.idle() 


 
