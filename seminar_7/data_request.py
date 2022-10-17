import data_interface as di


SECOND_NAME = 0 # номер поля в списке переменных
FIRST_NAME = 1  # номер поля в списке переменных
PHONE = 2       # номер поля в списке переменных
COMMIT = 3      # номер поля в списке переменных
NO_VALUE = ''

def find(data: list, second_name=NO_VALUE, first_name=NO_VALUE, phone=NO_VALUE, commit=NO_VALUE):
    """
    Функция выполняет запрос (фильтрацию) данных в соответствии с параметрами
    фильтрация данных только по одному из параметров (фамилия, имя, телефон, комментарий)
    :param data: телефонный список (фамилия, имя, телефон, комментарий)
    :param value: список переменных (фамилия, имя, телефон, комментарий)
    :return list: отфильтрованный телефонный список
    """
    find_list = []
    for i in range(len(data)):
        if second_name!=NO_VALUE and data[i][SECOND_NAME].find(second_name)==0 and first_name==phone==commit==NO_VALUE:
            find_list.append(data[i])
        elif first_name!=NO_VALUE and data[i][FIRST_NAME].find(first_name)==0 and second_name==phone==commit==NO_VALUE:
            find_list.append(data[i])
        elif phone!=NO_VALUE and data[i][PHONE].find(phone)==0 and second_name==first_name==commit==NO_VALUE:
            find_list.append(data[i])
        elif commit!=NO_VALUE and data[i][COMMIT].find(commit)==0 and second_name==first_name==phone==NO_VALUE:
            find_list.append(data[i]) 
    return find_list


import copy
def request_list(data: list, value: list):
    """
    Функция выполняет запрос (фильтрацию) данных в соответствии с параметрами
    :param data: телефонный список (фамилия, имя, телефон, комментарий)
    :param value: список переменных (фамилия, имя, телефон, комментарий)
    :return list: отфильтрованный телефонный список
    """
    return_list = copy.deepcopy(data)
    if value[SECOND_NAME] != NO_VALUE:
        return_list = find(return_list,second_name=value[SECOND_NAME])
    if value[FIRST_NAME] != NO_VALUE:
        return_list = find(return_list,first_name=value[FIRST_NAME])
    if value[PHONE] != NO_VALUE:
        return_list = find(return_list,phone=value[PHONE])
    if value[COMMIT] != NO_VALUE:
        return_list = find(return_list,commit=value[COMMIT])
    return return_list


def del_data(data: list, value: list):
    """
    Функция удаляет заданный элемент из файлов БД
    :param data: телефонный список (фамилия, имя, телефон, комментарий)
    :param value: список переменных (фамилия, имя, телефон, комментарий)
    :return: OK_RETURN/ERROR_RETURN
    """
    for i in range(len(data)):
        if data[i][SECOND_NAME]==value[SECOND_NAME] and data[i][FIRST_NAME]==value[FIRST_NAME] and data[i][PHONE]==value[PHONE] and data[i][COMMIT]==value[COMMIT]:
            data.pop(i)
            if di.save_all_format(data) == di.OK_RETURN:
                return di.OK_RETURN
            else:
                return di.ERROR_RETURN
    return di.ERROR_RETURN


def add_data(data: list, value: list):
    """
    Функция добавляет заданный элемент в файлы БД
    :param data: телефонный список (фамилия, имя, телефон, комментарий)
    :param value: список переменных (фамилия, имя, телефон, комментарий)
    :return: OK_RETURN/ERROR_RETURN
    """
    data_value = []
    data_value.append(value[SECOND_NAME])
    data_value.append(value[FIRST_NAME])
    data_value.append(value[PHONE])
    data_value.append(value[COMMIT])
    data.append(data_value)
    if di.save_all_format(data) == di.OK_RETURN:
        return di.OK_RETURN
    else:
        return di.ERROR_RETURN


def edit_data(data: list, find_data: list, update_data: list):
    """
    Функция редактирует заданный элемент в файлах БД
    :param data: телефонный список (фамилия, имя, телефон, комментарий)
    :param find_data: список переменных (фамилия, имя, телефон, комментарий)
    :param update_data: обновленные переменные (фамилия, имя, телефон, комментарий)
    :return: OK_RETURN/ERROR_RETURN
    """
    for i in range(len(data)):
        if data[i][SECOND_NAME]==find_data[SECOND_NAME] and data[i][FIRST_NAME]==find_data[FIRST_NAME] and data[i][PHONE]==find_data[PHONE] and data[i][COMMIT]==find_data[COMMIT]:
            if update_data[SECOND_NAME] != NO_VALUE:
                data[i][SECOND_NAME] = update_data[SECOND_NAME]
            if update_data[FIRST_NAME] != NO_VALUE:
                data[i][FIRST_NAME] = update_data[FIRST_NAME]
            if update_data[PHONE] != NO_VALUE:
                data[i][PHONE] = update_data[PHONE]
            if update_data[COMMIT] != NO_VALUE:
                data[i][COMMIT] = update_data[COMMIT]
            if di.save_all_format(data) == di.OK_RETURN:
                return di.OK_RETURN
            else:
                return di.ERROR_RETURN
    else:
        return di.ERROR_RETURN