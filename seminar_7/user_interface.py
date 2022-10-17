import data_request as dr
import data_interface as di
import view_data as vd
import random

COMMAND_SIZE = 5    # размер списка команды
PARAM_SIZE = 4      # размер списка параметров


def get_command_str(message):
    """
    Производит ввод команды и параметров с консоли (команда, фамилия, имя, телефон, комментарий)
    :param message: информация при вводе команды и параметров
    :return: list (команда, фамилия, имя, телефон, комментарий)
    """
    while True:
        in_string = input(message)
        in_list = in_string.split(',')
        if len(in_list) != COMMAND_SIZE and in_list[0] != 'init' and in_list[0] != 'q':
            vd.print_inp_err()
        else:
            return in_list


def get_param_list(message):
    """
    Производит ввод параметров с консоли (фамилия, имя, телефон, комментарий)
    :param message: информация при вводе параметров
    :return: list (фамилия, имя, телефон, комментарий)
    """
    while True:
        in_string = input(message)
        in_list = in_string.split(',')
        if len(in_list) != PARAM_SIZE:
            vd.print_inp_err()
        else:
            return in_list


def view_request(value: list):
    """
    Показывает все записи в соответствии с введенными параметрами
    :param value: список переменных (фамилия, имя, телефон, комментарий)
    :return: OK_RETURN/ERROR_RETURN
    """
    request_list = dr.request_list(di.load_data_phone(),value)
    if len(request_list) == 0:
        vd.print_message('НИЧЕГО НЕ НАЙДЕНО')
    else:
        vd.print_data(request_list)
    return di.OK_RETURN


def del_request(value: list):
    """
    Создает диалог с пользователем, для удаления
    выбранной записи 
    :param value: список переменных (фамилия, имя, телефон, комментарий)
    :return: OK_RETURN/ERROR_RETURN
    """
    request_list = dr.request_list(di.load_data_phone(),value)
    if len(request_list) == 0:
        vd.print_message('НИЧЕГО НЕ НАЙДЕНО')
        return di.OK_RETURN
    else:
        vd.print_data(request_list)
    while True:
        del_number = int(input('Введите номер записи которую нужно удалить: '))
        if 1<=del_number<=len(request_list):
            return dr.del_data(di.load_data_phone(),request_list[del_number-1])
        else:
            vd.print_inp_err()


def add_request(value: list):
    """
    Добавляет новую запись в телефонную книгу
    :param value: список переменных (фамилия, имя, телефон, комментарий)
    :return: OK_RETURN/ERROR_RETURN
    """
    return dr.add_data(di.load_data_phone(),value)


def edit_request(value: list):
    """
    Создает диалог с пользователем, для редактирования
    выбранной записи 
    :param value: список переменных (фамилия, имя, телефон, комментарий)
    :return: OK_RETURN/ERROR_RETURN
    """
    request_list = dr.request_list(di.load_data_phone(),value)
    if len(request_list) == 0:
        vd.print_message('НИЧЕГО НЕ НАЙДЕНО')
        return di.OK_RETURN
    else:
        vd.print_data(request_list)
    while True:
        edit_number = int(input('Введите номер записи которую нужно отредактировать: '))
        if 1<=edit_number<=len(request_list):
            param_list = get_param_list('\nФормат данных: Фамилия,Имя,Телефон,Комментарий - например:\n'
                                      + ',,+7(963)333-1234, - изменим только телефон, другие данные останутся прежними\n\n'
                                      + 'Введите новые значения записи: ')
            return dr.edit_data(di.load_data_phone(),request_list[edit_number-1],param_list)
        else:
            vd.print_inp_err()
    


def init_data():
    """
    Заполняет данными телефонной книги текстовые файлы, 
    избавляя от ручного ввода
    :return: OK_RETURN/ERROR_RETURN
    """
    NUMBER_WRITE = 100
    data = []
    for i in range(NUMBER_WRITE):
        data.append([])
        data[i].append(f'Ivanov_{i+1}')
        data[i].append(f'Ivan')
        data[i].append(f'+7(963)123-{1000+random.randint(1,8000)}')
        hw = lambda x : 'Home' if x==1 else 'Work'
        data[i].append(f'{hw(random.randint(0,1))}')
    for i in range(NUMBER_WRITE):
        data.append([])
        data[NUMBER_WRITE+i].append(f'Petrov_{i+1}')
        data[NUMBER_WRITE+i].append(f'Petor')
        data[NUMBER_WRITE+i].append(f'+7(917)123-{1000+random.randint(1,8000)}')
        hw = lambda x : 'Home' if x==1 else 'Work'
        data[NUMBER_WRITE+i].append(f'{hw(random.randint(0,1))}')
    for i in range(NUMBER_WRITE):
        data.append([])
        data[NUMBER_WRITE*2+i].append(f'Sidorov_{i+1}')
        data[NUMBER_WRITE*2+i].append(f'Vasy')
        data[NUMBER_WRITE*2+i].append(f'+7(902)123-{1000+random.randint(1,8000)}')
        hw = lambda x : 'Home' if x==1 else 'Work'
        data[NUMBER_WRITE*2+i].append(f'{hw(random.randint(0,1))}')
    for i in range(NUMBER_WRITE):
        data.append([])
        data[NUMBER_WRITE*3+i].append(f'Vasechkin_{i+1}')
        data[NUMBER_WRITE*3+i].append(f'Vova')
        data[NUMBER_WRITE*3+i].append(f'+7(900)123-{1000+random.randint(1,8000)}')
        hw = lambda x : 'Home' if x==1 else 'Work'
        data[NUMBER_WRITE*3+i].append(f'{hw(random.randint(0,1))}')
    return di.save_all_format(data)

