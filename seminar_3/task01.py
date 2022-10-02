# Задача 1. Задайте список, состоящий из произвольных чисел, количество задает пользователь. 
# Напишите программу, которая найдет сумму элементов списка, стоящих на нечетных позициях (не индексах).  
# in >> 4  
# out >> [7, 9, 2, 3]  
#     >> 9  
# in >> 5  
# out >> [2, 5, 2, 7, 9]  
#     >> 13   

import random

MIN_VALUE = 1
MAX_VALUE = 10

input_string = input('Введите размер списка: ')
while input_string.isdigit() == False:
    print('Ошибка ввода.')
    input_string = input('Введите размер списка: ')

random_list = [random.randint(MIN_VALUE, MAX_VALUE) for i in range(int(input_string))]
print(f'Рандомный список: {random_list}')
sum_list_value = 0
for i in range (len(random_list)):
    if i%2==0:
        sum_list_value += random_list[i] 
else:
    print(f'Sum = {sum_list_value}')