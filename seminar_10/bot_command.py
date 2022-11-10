
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ContextTypes, CallbackContext
import requests
import logging

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


# Глобальная переменная текста предыдущего сообщения
past_message = ''

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Функция start
    """
    reply_keyboard = [['Калькулятор', 'Искусственный интеллект']]
    await update.message.reply_text(
        'Калькулятор или искусственный интеллект?',
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, resize_keybord=True, input_field_placeholder='Сделайте свой выбор'
        ))


async def calc_select(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Функция выбора калькулятора
    """
    reply_keyboard = [['Сумма', 'Разность','Умножение'],['Деление', 'Степень','Корень'],['Назад']]
    await update.message.reply_text(
        'Введите числа разделенные пробелом, и выбирайте операции над ними (сумма, умножение и т.д.). Операции можно выбирать без повторного ввода чисел. ',
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=False, resize_keybord=True, input_field_placeholder='Введите числа разделенные пробелом'
        ))


async def artificial_intelligence_select(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Функция выбора искусственный интеллект 
    """
    reply_keyboard = [['Ответы на вопросы по Википедии'],['Анализ тональности'],['Назад']]
    await update.message.reply_text(
        'Введите любую фразу или вопрос',
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=False, resize_keybord=True, input_field_placeholder='Например: Как отводятся излишки тепла у млекопитающих?'
        ))


async def sentiment_analysis(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Функция анализ тональности
    """
    global past_message
    data = {'x':  [past_message]}
    res = requests.post('https://7015.deeppavlov.ai/model', json=data, verify=False).json()
    logger.info("Пользователь: %s, фраза: %s, проверка: %s, ответ: %s", update.effective_user.first_name, past_message, update.message.text, res[0][0])
    await update.message.reply_text(f'{res[0][0]}')



async def answers_on_questions_wikipedia(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Функция ответа на вопросы по википедии 
    """
    global past_message
    data = {'question_raw':  [past_message]}
    res = requests.post('https://7012.deeppavlov.ai/model', json=data, verify=False).json()
    logger.info("Пользователь: %s, фраза: %s, проверка: %s, ответ: %s", update.effective_user.first_name, past_message, update.message.text, res[0][0])
    await update.message.reply_text(f'{res[0][0]}')


async def copy_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Функция копирования сообщения
    """
    global past_message
    past_message = update.message.text
 

async def sum_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Функция сложения, вводимых через пробел чисел
    """
    global past_message
    logger.info("Пользователь: %s, числа: %s, операция: %s", update.effective_user.first_name, past_message, update.message.text)
    in_string = past_message.rstrip()
    in_list = in_string.split()
    try:
        float_list = [float(in_list[i]) for i in range(len(in_list))]
    except:
        await update.message.reply_text('Не верный формат числа')
        return None
    if len(float_list)<2:
        await update.message.reply_text('Задайте больше одного значения')
        return None
    out_string = f'{float_list[0]}'
    out_mul = float_list[0]
    for i in range(1,len(float_list)):
        if float_list[i] >= 0:
            out_string += f'+{float_list[i]}'
        else:
            out_string += f'{float_list[i]}'
        out_mul += float_list[i]
    await update.message.reply_text(f'Результат: {out_string}={out_mul}')


async def dif_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Функция вычитания, вводимых через пробел чисел
    """
    global past_message
    logger.info("Пользователь: %s, числа: %s, операция: %s", update.effective_user.first_name, past_message, update.message.text)
    in_string = past_message.rstrip()
    in_list = in_string.split()
    try:
        float_list = [float(in_list[i]) for i in range(len(in_list))]
    except:
        await update.message.reply_text('Не верный формат числа')
        return None
    if len(float_list)<2:
        await update.message.reply_text('Задайте больше одного значения')
        return None
    out_string = f'{float_list[0]}'
    out_mul = float_list[0]
    for i in range(1,len(float_list)):
        if float_list[i] >= 0:
            out_string += f'-{float_list[i]}'
        else:
            out_string += f'-({float_list[i]})'
        out_mul -= float_list[i]
    await update.message.reply_text(f'Результат: {out_string}={out_mul}')


async def sqrt_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Функция квадратного корня
    """
    global past_message
    logger.info("Пользователь: %s, числа: %s, операция: %s", update.effective_user.first_name, past_message, update.message.text)
    in_string = past_message.rstrip()
    in_list = in_string.split()
    try:
        float_value = float(in_list[0])
    except:
        await update.message.reply_text('Не верный формат числа')
        return None
    if len(in_list)>1:
        await update.message.reply_text('Нужно задать одно число')
        return None
    await update.message.reply_text(f'Результат: sqrt({float_value})={float_value**0.5}')


async def deg_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Функция степени числа
    """
    global past_message
    logger.info("Пользователь: %s, числа: %s, операция: %s", update.effective_user.first_name, past_message, update.message.text)
    in_string = past_message.rstrip()
    in_list = in_string.split()
    try:
        float_value = float(in_list[0])
        degrees_value = float(in_list[1])
        if len(in_list)!=2:
            await update.message.reply_text('Нужно задать число и степень')
            return None  
    except:
        if len(in_list)!=2:
            await update.message.reply_text('Нужно задать число и степень')
        else:
            await update.message.reply_text('Не верный формат числа')
        return None   
    await update.message.reply_text(f'Результат: {float_value}^{degrees_value}={float_value**degrees_value}')


async def mul_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Функция умножения, вводимых через пробел чисел
    """
    global past_message
    logger.info("Пользователь: %s, числа: %s, операция: %s", update.effective_user.first_name, past_message, update.message.text)
    in_string = past_message.rstrip()
    in_list = in_string.split()
    try:
        float_list = [float(in_list[i]) for i in range(len(in_list))]
    except:
        await update.message.reply_text('Не верный формат числа')
        return None
    if len(float_list)<2:
        await update.message.reply_text('Задайте больше одного значения')
        return None
    out_string = f'{float_list[0]}'
    out_mul = float_list[0]
    for i in range(1,len(float_list)):
        if float_list[i] >= 0:
            out_string += f'*{float_list[i]}'
        else:
            out_string += f'*({float_list[i]})'
        out_mul *= float_list[i]
    await update.message.reply_text(f'Результат: {out_string}={out_mul}')


async def div_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Функция деления, вводимых через пробел чисел
    """
    global past_message
    logger.info("Пользователь: %s, числа: %s, операция: %s", update.effective_user.first_name, past_message, update.message.text)
    in_string = past_message.rstrip()
    in_list = in_string.split()
    try:
        float_list = [float(in_list[i]) for i in range(len(in_list))]
    except:
        await update.message.reply_text('Не верный формат числа')
        return None
    if len(float_list)<2:
        await update.message.reply_text('Задайте больше одного значения')
        return None
    out_string = f'{float_list[0]}'
    out_div = float_list[0]
    for i in range(1,len(float_list)):
        if float_list[i] >= 0:
            out_string += f'/{float_list[i]}'
        else:
            out_string += f'/({float_list[i]})'
        out_div /= float_list[i]
    await update.message.reply_text(f'Результат: {out_string}={out_div}')


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Функция функция показывает команды бота
    """
    help_info = '''/start (старт бота)
/help (команды бота)'''           
    await update.message.reply_text(help_info)