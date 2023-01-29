from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import datetime
from spy import *
import joke
from telegram.ext import ApplicationBuilder, ContextTypes

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def hi_command(update: Update, context: CallbackContext):
    await log(update, context)
    await update.message.reply_text(f'Hi {update.effective_user.first_name}!')

async def help_command(update: Update, context: CallbackContext):
    await log(update, context)
    await update.message.reply_text('/hi\n'
                                    '/time\n'
                                    '/joke\n'
                                    '/sum\n'
                                    '/help\n')

async def joke_command(update: Update, context: CallbackContext):
    await log(update, context)
    await update.message.reply_text(f'{await joke.Gen_Smile()}')



async def time_command(update: Update, context: CallbackContext):
    log(update, context)
    await update.message.reply_text(f'{datetime.datetime.now().time()}')


async def sum_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split() # /sum 123 534543
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'{x} + {y} = {x+y}')