#!/usr/bin/env python3

import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext
from pdb import set_trace
# from asyncio import queue
import requests
import bittensorinfo
from dotenv import load_dotenv
import os

load_dotenv()
telegram_bot_token = os.getenv('TELEGRAM_BOT_TOKEN')

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

# Define your API endpoint
# API_ENDPOINT = 'https://api.example.com/data'

def start(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [InlineKeyboardButton("Node Status", callback_data='node_status')],
        [InlineKeyboardButton("Add Node", callback_data='add_node')],
        [InlineKeyboardButton("Home", callback_data='home')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Please choose:', reply_markup=reply_markup)

def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    
    if query.data == 'node_status':
#        response = requests.get(API_ENDPOINT)
        response = bittensorinfo.get_bittensor_info()
        if response:
#        if response.status_code == 200:
#            data = response.json()
            data = response
            query.edit_message_text(text=f'Nodes performance:\n {data}')
        else:
            query.edit_message_text(text="Failed to fetch node status.")
    elif query.data == 'add_node':
        query.edit_message_text(text="Add Node functionality is not implemented yet.")
    elif query.data == 'home':
        query.edit_message_text(text="Welcome to the home menu.")

def main() -> None:
    # Replace 'YOUR_TOKEN' with your bot's token
    updater = Updater(token=telegram_bot_token)

    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
