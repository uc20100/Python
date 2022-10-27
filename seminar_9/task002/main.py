from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler
from telegram.ext import CommandHandler, MessageHandler, filters
from bot_command import *
from spy import log_on, log_off



# Укажите TOKEN бота
app = ApplicationBuilder().token('YOUR TOKEN HERE').build()

app.add_handler(CommandHandler("sum", sum_command))
app.add_handler(CommandHandler("dif", dif_command))
app.add_handler(CommandHandler("mul", mul_command))
app.add_handler(CommandHandler("div", div_command))
app.add_handler(CommandHandler("sqrt", sqrt_command))
app.add_handler(CommandHandler("deg", deg_command))
app.add_handler(CommandHandler("start", start_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(MessageHandler(filters.Text('Вести log чата'), log_on))
app.add_handler(MessageHandler(filters.Text('Без записи log чата'), log_off))
app.run_polling()