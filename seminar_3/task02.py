# Задача 2. Напишите программу, которая найдет произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.  
# in >> 4  
# out >> [8, 9, 10, 10]  
#     >> [80, 90]  
# in >> 5  
# out >> [3, 3, 6, 8, 4]  
#     >> [12, 24, 6]  

MIN_VALUE = 1
MAX_VALUE = 10

import random
def get_list (size_list, min_value, max_value):
    result_out = [random.randint(min_value, max_value) for i in range(size_list)]
    return result_out

def calculation_list(value):
    result_out = []
    for i in range (len(value)//2):
        result_out.append(value[i]*value[len(value)-i-1])
    else:
        if len(value)%2 > 0:
            result_out.append(value[i+1])  
    return result_out


input_string = input('Введите размер списка: ')
while input_string.isdigit() == False:
    print('Ошибка ввода.')
    input_string = input('Введите размер списка: ')

random_list = get_list(int(input_string), MIN_VALUE, MAX_VALUE)
print(f'Исходный список: {random_list}')
print(f'Вычисленный список: {calculation_list(random_list)}')



