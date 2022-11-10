from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler
from telegram.ext import CommandHandler, MessageHandler, filters
from bot_command import *
from TOKEN import TOKEN_BOT


# Укажите TOKEN бота
app = ApplicationBuilder().token(TOKEN_BOT).build()

app.add_handler(CommandHandler("start", start_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(MessageHandler(filters.Text('Калькулятор'), calc_select))
app.add_handler(MessageHandler(filters.Text('Сумма'), sum_command))
app.add_handler(MessageHandler(filters.Text('Разность'), dif_command))
app.add_handler(MessageHandler(filters.Text('Умножение'), mul_command))
app.add_handler(MessageHandler(filters.Text('Деление'), div_command))
app.add_handler(MessageHandler(filters.Text('Степень'), deg_command))
app.add_handler(MessageHandler(filters.Text('Корень'), sqrt_command))
app.add_handler(MessageHandler(filters.Text('Назад'), start_command))
app.add_handler(MessageHandler(filters.Text('Искусственный интеллект'), artificial_intelligence_select))
app.add_handler(MessageHandler(filters.Text('Анализ тональности'), sentiment_analysis))
app.add_handler(MessageHandler(filters.Text('Ответы на вопросы по Википедии'), answers_on_questions_wikipedia))
app.add_handler(MessageHandler(filters.Text(), copy_message))
app.run_polling()