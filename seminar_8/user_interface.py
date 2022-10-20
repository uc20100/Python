import data_request as dr
import data_interface as di
import view_data as vd
import random

COMMAND_SIZE = 5    # размер списка команды
PARAM_SIZE = 2      # размер списка параметров



def get_command_str(message) -> str:
    """
    Производит ввод номера команды с консоли
    :param message: информация при вводе команды и параметров
    :return: вводимая строка
    """
    while True:
        in_string = input(message)
        if not in_string in ('1','2','3','4','5','6','7','8'):
            vd.print_inp_err()
        else:
            return in_string


def get_param_list(message) -> list:
    """
    Производит ввод параметров с консоли (фамилия, имя)
    :param message: информация при вводе параметров
    :return: list (фамилия, имя)
    """
    while True:
        in_string = input(message)
        in_list = in_string.split(',')
        if len(in_list) != PARAM_SIZE:
            vd.print_inp_err()
        else:
            return in_list


def get_param_list_all(message) -> list:
    """
    Производит ввод параметров с консоли (фамилия, имя, телефон, должность, оклад)
    :param message: информация при вводе параметров
    :return: list (фамилия, имя, телефон, должность, оклад)
    """
    while True:
        in_string = input(message)
        in_list = in_string.split(',')
        if len(in_list) != PARAM_SIZE+3:
            vd.print_inp_err()
        else:
            return in_list


def get_param(message) -> str:
    """
    Производит ввод параметра с консоли (одиночный параметр)
    :param message: информация при вводе параметров
    :return: str (одиночный параметр)
    """
    in_string = input(message)
    return in_string


def view_request(second_name=dr.NO_VALUE, first_name=dr.NO_VALUE, phone=dr.NO_VALUE, position=dr.NO_VALUE, salary_min=dr.NO_VALUE_SALARY, salary_max=dr.NO_VALUE_SALARY):
    """
    Показывает все записи в соответствии с введенными параметрами
    :param second_name: фамилия
    :param first_name: имя
    :param phone: телефон
    :param position: должность
    :param salary_min: минимальный порог зарплаты
    :param salary_max: максимальный порог зарплаты
    """
    request_list = dr.request_list(di.load_data(),second_name, first_name, phone, position, salary_min, salary_max)
    if len(request_list) == 0:
        vd.print_message('НИЧЕГО НЕ НАЙДЕНО')
    else:
        vd.print_data(request_list)


def del_request(value: str):
    """
    Создает диалог с пользователем, для удаления
    выбранной записи 
    :param value: фамилия
    :return: OK_RETURN/ERROR_RETURN
    """
    request_list = dr.request_list(di.load_data(),second_name=value)
    if len(request_list) == 0:
        vd.print_message('НИЧЕГО НЕ НАЙДЕНО')
        return di.OK_RETURN
    else:
        vd.print_data(request_list)
    while True:
        del_number = int(input('Введите номер записи которую нужно удалить: '))
        if 1<=del_number<=len(request_list):
            return dr.del_data(di.load_data(),request_list[del_number-1])
        else:
            vd.print_inp_err()


def add_request(value: list):
    """
    Добавляет новую запись в телефонную книгу
    :param value: список переменных (фамилия, имя, телефон, должность, оклад)
    :return: OK_RETURN/ERROR_RETURN
    """
    return dr.add_data(di.load_data(),value)


def edit_request(value: str):
    """
    Создает диалог с пользователем, для редактирования
    выбранной записи 
    :param value: список переменных (фамилия, имя, должность, телефон, оклад)
    :return: OK_RETURN/ERROR_RETURN
    """
    request_list = dr.request_list(di.load_data(),second_name=value)
    if len(request_list) == 0:
        vd.print_message('НИЧЕГО НЕ НАЙДЕНО')
        return di.OK_RETURN
    else:
        vd.print_data(request_list)
    while True:
        edit_number = int(input('Введите номер записи которую нужно отредактировать: '))
        if 1<=edit_number<=len(request_list):
            param_list = get_param_list_all('\nФормат данных: Фамилия,Имя,Должность,Телефон,Оклад - например:\n'
                                      + ',,,+7(963)333-1234, - изменим только телефон, другие данные останутся прежними\n\n'
                                      + 'Введите новые значения записи: ')
            return dr.edit_data(di.load_data(),request_list[edit_number-1],param_list)
        else:
            vd.print_inp_err()
    