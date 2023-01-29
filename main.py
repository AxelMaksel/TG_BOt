from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import bot_commands as bcom



app = ApplicationBuilder().token("5847923715:AAHsw73o0MojGoOAjmOySYMwvEVrMNii6QI").build()


app.add_handler(CommandHandler("hello", bcom.hello))
app.add_handler(CommandHandler("time", bcom.time_command))
app.add_handler(CommandHandler("joke", bcom.joke_command))
app.add_handler(CommandHandler("hi", bcom.hi_command))
app.add_handler(CommandHandler("sum", bcom.sum_command))
app.add_handler(CommandHandler("help", bcom.help_command))

app.run_polling()