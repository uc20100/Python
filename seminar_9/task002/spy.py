from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ContextTypes, CallbackContext


log_write_status = False

def log(update: Update, context: CallbackContext) -> None:
    """
    Записываем log файл
    """
    global log_write_status
    if log_write_status:
        with open('log.csv', 'a') as log:
            log.write(f'{update.effective_user.first_name},{update.effective_user.id},{update.message.text}\n')



async def log_on(update: Update, context: CallbackContext) -> None:
    """
    Будем записывать чат в лог
    """
    global log_write_status 
    log_write_status = True
    await update.message.reply_text('Хорошо, будет записываться log чата') 
    


async def log_off(update: Update, context: CallbackContext) -> None:
    """
    Отключим запись лога
    """
    global log_write_status
    log_write_status = False
    await update.message.reply_text('Хорошо, log чата записываться не будет')