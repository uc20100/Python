
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ContextTypes, CallbackContext
from spy import log


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Функция start
    """
    reply_keyboard = [['Вести log чата', 'Без записи log чата']]
    await update.message.reply_text(
        'Вы хотите записывать log чата?',
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, resize_keybord=True, input_field_placeholder='Сделайте свой выбор'
        ))


async def sum_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Функция сложения, вводимых через пробел чисел
    """
    log(update, context)
    in_string = update.message.text
    in_string = in_string.rstrip()
    in_list = in_string.split()
    try:
        float_list = [float(in_list[i]) for i in range(1,len(in_list))]
    except:
        await update.message.reply_text('Не верный формат числа')
        return None
    out_string = f'{float_list[0]}'
    out_mul = float_list[0]
    for i in range(1,len(float_list)):
        if float_list[i] >= 0:
            out_string += f'+{float_list[i]}'
        else:
            out_string += f'{float_list[i]}'
        out_mul += float_list[i]
    await update.message.reply_text(f'{out_string}={out_mul}')



async def dif_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Функция вычитания, вводимых через пробел чисел
    """
    log(update, context)
    in_string = update.message.text
    in_string = in_string.rstrip()
    in_list = in_string.split()
    try:
        float_list = [float(in_list[i]) for i in range(1,len(in_list))]
    except:
        await update.message.reply_text('Не верный формат числа')
        return None
    out_string = f'{float_list[0]}'
    out_mul = float_list[0]
    for i in range(1,len(float_list)):
        if float_list[i] >= 0:
            out_string += f'-{float_list[i]}'
        else:
            out_string += f'-({float_list[i]})'
        out_mul -= float_list[i]
    await update.message.reply_text(f'{out_string}={out_mul}')


async def sqrt_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Функция квадратного корня
    """
    log(update, context)
    in_string = update.message.text
    in_string = in_string.rstrip()
    in_list = in_string.split()
    try:
        float_value = float(in_list[1])
    except:
        await update.message.reply_text('Не верный формат числа')
        return None
    if len(in_list)>2:
        await update.message.reply_text('Нужно задать одно число')
        return None
    await update.message.reply_text(f'sqrt({float_value})={float_value**0.5}')


async def deg_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Функция степени числа
    """
    log(update, context)
    in_string = update.message.text
    in_string = in_string.rstrip()
    in_list = in_string.split()
    try:
        float_value = float(in_list[1])
        degrees_value = float(in_list[2])
    except:
        if len(in_list)!=3:
            await update.message.reply_text('Нужно задать число и степень')
        else:
            await update.message.reply_text('Не верный формат числа')
        return None   
    await update.message.reply_text(f'{float_value}^{degrees_value}={float_value**degrees_value}')


async def mul_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Функция умножения, вводимых через пробел чисел
    """
    log(update, context)
    in_string = update.message.text
    in_string = in_string.rstrip()
    in_list = in_string.split()
    try:
        float_list = [float(in_list[i]) for i in range(1,len(in_list))]
    except:
        await update.message.reply_text('Не верный формат числа')
        return None
    out_string = f'{float_list[0]}'
    out_mul = float_list[0]
    for i in range(1,len(float_list)):
        if float_list[i] >= 0:
            out_string += f'*{float_list[i]}'
        else:
            out_string += f'*({float_list[i]})'
        out_mul *= float_list[i]
    await update.message.reply_text(f'{out_string}={out_mul}')


async def div_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Функция деления, вводимых через пробел чисел
    """
    log(update, context)
    in_string = update.message.text
    in_string = in_string.rstrip()
    in_list = in_string.split()
    try:
        float_list = [float(in_list[i]) for i in range(1,len(in_list))]
    except:
        await update.message.reply_text('Не верный формат числа')
        return None
    out_string = f'{float_list[0]}'
    out_div = float_list[0]
    for i in range(1,len(float_list)):
        if float_list[i] >= 0:
            out_string += f'/{float_list[i]}'
        else:
            out_string += f'/({float_list[i]})'
        out_div /= float_list[i]
    await update.message.reply_text(f'{out_string}={out_div}')


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Функция функция показывает команды бота
    """
    help_info = '''/sum (сумма /sum 2 2)
/dif (разность /dif 5 3)
/sqrt (корень квадратный /sqrt 25)
/deg (возведение в степень /deg 2 3)
/mul (умножение /mul 2 5)
/div (деление /div 8 4)'''
              
    await update.message.reply_text(help_info)