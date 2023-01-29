from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import datetime

async def log(update: Update, context: CallbackContext):
    file = open('db.csv', 'a')
    file.write(f'{datetime.datetime.now()},{update.effective_user.first_name},{update.effective_user.id}, {update.message.text}\n')
    file.close()    

