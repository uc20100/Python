import data_interface as di


ID_PEOPLE = 0   # id сотрудника
SECOND_NAME = 1 # номер поля в списке переменных
FIRST_NAME = 2  # номер поля в списке переменных
POSITION = 3    # номер поля в списке переменных
PHONE = 4       # номер поля в списке переменных
SALARY = 5      # номер поля в списке переменных
NO_VALUE = ''
NO_VALUE_SALARY = -1

def find(data: list, second_name=NO_VALUE, first_name=NO_VALUE, phone=NO_VALUE, position=NO_VALUE, salary_min=NO_VALUE_SALARY, salary_max=NO_VALUE_SALARY) -> list:
    """
    Функция выполняет запрос (фильтрацию) данных в соответствии с параметрами
    фильтрация данных только по одному из параметров (фамилия, имя, телефон, должность, зарплата)
    :param data: телефонный список (фамилия, имя, телефон, комментарий)
    :param second_name: фамилия
    :param first_name: имя
    :param phone: телефон
    :param position: должность
    :param salary_min: минимальный порог зарплаты
    :param salary_max: максимальный порог зарплаты
    :return list: отфильтрованный список
    """
    find_list = []
    for i in range(len(data)):
        if second_name!=NO_VALUE and data[i][SECOND_NAME].find(second_name)==0 and first_name==phone==position==NO_VALUE and salary_min==salary_max==NO_VALUE_SALARY:
            find_list.append(data[i])  
        elif first_name!=NO_VALUE and data[i][FIRST_NAME].find(first_name)==0 and second_name==phone==position==NO_VALUE and salary_min==salary_max==NO_VALUE_SALARY:
            find_list.append(data[i])
        elif phone!=NO_VALUE and data[i][PHONE].find(phone)==0 and second_name==first_name==position==NO_VALUE and salary_min==salary_max==NO_VALUE_SALARY:
            find_list.append(data[i])
        elif position!=NO_VALUE and data[i][POSITION].find(position)==0 and second_name==first_name==phone==NO_VALUE and salary_min==salary_max==NO_VALUE_SALARY:
            find_list.append(data[i]) 
        elif (salary_min!=NO_VALUE_SALARY and salary_max!=NO_VALUE_SALARY) and salary_min<=float(data[i][SALARY])<=salary_max:
            find_list.append(data[i])
    return find_list


import copy
def request_list(data: list, second_name=NO_VALUE, first_name=NO_VALUE, phone=NO_VALUE, position=NO_VALUE, salary_min=NO_VALUE_SALARY, salary_max=NO_VALUE_SALARY) -> list:
    """
    Функция выполняет запрос (фильтрацию) данных в соответствии с параметрами (фамилия, имя, телефон, должность, зарплата)
    :param data: список данных (фамилия, имя, телефон, должность, зарплата)
    :param second_name: фамилия
    :param first_name: имя
    :param phone: телефон
    :param position: должность
    :param salary_min: минимальный порог зарплаты
    :param salary_max: максимальный порог зарплаты
    :return list: отфильтрованный список
    """
    return_list = copy.deepcopy(data)
    if second_name != NO_VALUE:
        return_list = find(return_list,second_name=second_name)
    if first_name != NO_VALUE:
        return_list = find(return_list,first_name=first_name)
    if phone != NO_VALUE:
        return_list = find(return_list,phone=phone)
    if position != NO_VALUE:
        return_list = find(return_list,position=position)
    if salary_min!=NO_VALUE_SALARY and salary_max!=NO_VALUE_SALARY:
        return_list = find(return_list,salary_min=salary_min,salary_max=salary_max)
    return return_list


def del_data(data: list, value: list):
    """
    Функция удаляет заданный элемент из файлов БД
    :param data: телефонный список (фамилия, имя, телефон, комментарий)
    :param value: список переменных (фамилия, имя, телефон, комментарий)
    :return: OK_RETURN/ERROR_RETURN
    """
    for i in range(len(data)):
        if data[i][SECOND_NAME]==value[SECOND_NAME] and data[i][FIRST_NAME]==value[FIRST_NAME] and data[i][PHONE]==value[PHONE] and data[i][POSITION]==value[POSITION]:
            data.pop(i)
            if di.save_all_format(data) == di.OK_RETURN:
                return di.OK_RETURN
            else:
                return di.ERROR_RETURN
    return di.ERROR_RETURN


def add_data(data: list, value: list):
    """
    Функция добавляет заданный элемент в файлы БД
    :param data: телефонный список (id, фамилия, имя, телефон, должность, оклад)
    :param value: список переменных (фамилия, имя, телефон, должность, оклад)
    :return: OK_RETURN/ERROR_RETURN
    """
    id_list =[int(i[ID_PEOPLE]) for i in data]
    data_value = []
    id = max(id_list)+1
    data_value.append(str(id))
    data_value.append(value[SECOND_NAME-1])
    data_value.append(value[FIRST_NAME-1])
    data_value.append(value[PHONE-1])
    data_value.append(value[POSITION-1])
    data_value.append(value[SALARY-1])
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
        if data[i][SECOND_NAME]==find_data[SECOND_NAME] and data[i][FIRST_NAME]==find_data[FIRST_NAME] and data[i][PHONE]==find_data[PHONE] and data[i][POSITION]==find_data[POSITION]:
            if update_data[SECOND_NAME-1] != NO_VALUE:
                data[i][SECOND_NAME] = update_data[SECOND_NAME-1]
            if update_data[FIRST_NAME-1] != NO_VALUE:
                data[i][FIRST_NAME] = update_data[FIRST_NAME-1]
            if update_data[PHONE-1] != NO_VALUE:
                data[i][PHONE] = update_data[PHONE-1]
            if update_data[POSITION-1] != NO_VALUE:
                data[i][POSITION] = update_data[POSITION-1]
            if update_data[SALARY-1] != NO_VALUE:
                data[i][SALARY] = update_data[SALARY-1]
            if di.save_all_format(data) == di.OK_RETURN:
                return di.OK_RETURN
            else:
                return di.ERROR_RETURN
    else:
        return di.ERROR_RETURN

