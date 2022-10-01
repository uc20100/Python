# Задача 4. Задайте список из произвольных вещественных чисел, количество задает пользователь. 
# Напишите программу, которая найдет разницу между максимальным и минимальным значением дробной части элементов.
# in >> 3
# out >> [2.84, 9.42, 1.87]
#     >> "Min: 0.42, Max: 0.87, Difference: 0.45


import random
MIN_RANDOM_VALUE = 0
MAX_RANDOM_VALUE = 10
ROUNDING_SING = 2


input_string = input('Введите количество вещественных чисел: ')
while input_string.isdigit() == False:
    print('Ошибка ввода.')
    input_string = input('Введите количество вещественных чисел: ')

list_random_value = [round(random.uniform(MIN_RANDOM_VALUE, MAX_RANDOM_VALUE), ROUNDING_SING) for i in range(int(input_string))]
print(list_random_value)
list_remainder_value = [round((list_random_value[i]-list_random_value[i]//1), ROUNDING_SING) for i in range(len(list_random_value))]
max_value = max(list_remainder_value) 
min_value = min(list_remainder_value)
difference_value = round((max_value - min_value), ROUNDING_SING)
print(f'Min: {min_value}, Max: {max_value}, Difference: {difference_value}')

