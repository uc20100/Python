from tkinter import SEPARATOR
import view_data as vd

ERROR_RETURN = -1
OK_RETURN = 1
TXT_TYPE_DATA = 'txt'
CSV_TYPE_DATA = 'csv'
SEPARATOR_CHAR_CSV = ';'
TXT_PATH = 'data_phone.txt' # расположение TXT файла
CSV_PATH = 'data_phone.csv' # расположение CSV файла
ONE_RECORD_SIZE = 4

def load_data_phone(data_path=TXT_PATH, type_data=TXT_TYPE_DATA):
    """
    Загружает БД телефонной книги, отфильтровывая 
    данные заполненные не по правилам 
    :param data_path: название и расположение файла БД
    :param type_data: тип файла TXT или CSV
    :return: list БД/ERROR_RETURN
    """
    try:
        list_out = []
        with open(data_path, 'r') as dp:
            read_data = dp.read()
        if type_data == TXT_TYPE_DATA:
            temp_list = read_data.split('\n\n')
            temp_list = [i.split('\n') for i in temp_list]
        elif type_data == CSV_TYPE_DATA:
            temp_list = read_data.split('\n')
            temp_list = [i.split(SEPARATOR_CHAR_CSV) for i in temp_list]
        else:
            return ERROR_RETURN
        for i in range(len(temp_list)):
            if ONE_RECORD_SIZE == len(temp_list[i]):
                list_out.append(temp_list[i])
        return list_out
    except Exception as e:   
        vd.print_message(e)
        return ERROR_RETURN


def save_data_phone(data: list, data_path: str,  type_data: str):
    """
    Сохраняет данные в БД телефонной книги
    :param data: данные телефонной книги
    :param data_path: название и расположение файла БД
    :param type_data: тип файла TXT или CSV
    :return: OK_RETURN/ERROR_RETURN
    """
    try:
        write_string = ''
        for i in range(len(data)):
            if type_data == TXT_TYPE_DATA:
                for j in range(ONE_RECORD_SIZE):
                    write_string += data[i][j] + '\n'
            else:
                for j in range(ONE_RECORD_SIZE):
                    if j < ONE_RECORD_SIZE-1:
                        write_string += data[i][j] + SEPARATOR_CHAR_CSV
                    else:
                        write_string += data[i][j]
            write_string += '\n'
        with open(data_path, 'w') as dp:
            dp.writelines(write_string)
        return OK_RETURN
    except Exception as e:
        vd.print_message(e)
        return ERROR_RETURN


def save_all_format(data: list):
    """
    Сохраняет данные в БД телефонной книги 
    в формате TXT и CSV
    :param data: данные телефонной книги
    :return: OK_RETURN/ERROR_RETURN
    """
    ret1 = save_data_phone(data,TXT_PATH,TXT_TYPE_DATA)
    ret2 = save_data_phone(data,CSV_PATH,CSV_TYPE_DATA)
    if ret1==ret2==OK_RETURN:
        return OK_RETURN
    else:
        return ERROR_RETURN

